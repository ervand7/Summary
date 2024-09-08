// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

import { MerkleProof } from "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";
import { IERC20, SafeERC20 } from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import { EIP712 } from "@openzeppelin/contracts/utils/cryptography/EIP712.sol";
import { SignatureChecker } from "@openzeppelin/contracts/utils/cryptography/SignatureChecker.sol";
import { ECDSA } from "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import { MessageHashUtils } from "@openzeppelin/contracts/utils/cryptography/MessageHashUtils.sol";

/**
 * @title Merkle Airdrop - Airdrop tokens to users who can prove they are in a merkle tree
 * @author Ciara Nightingale
 * @author Patrick Collins
 * @author Cyfrin
 */
contract MerkleAirdrop is EIP712 {
    using ECDSA for bytes32;
    using SafeERC20 for IERC20; // Prevent sending tokens to recipients who can’t receive

    error MerkleAirdrop__InvalidProof();
    error MerkleAirdrop__AlreadyClaimed();
    error MerkleAirdrop__InvalidSignature();

    IERC20 private immutable i_airdropToken;
    bytes32 private immutable i_merkleRoot;
    mapping(address => bool) private s_hasClaimed;

    // MESSAGE_TYPEHASH — это хэш от описания структуры сообщения. Он используется
    // для обеспечения целостности и безопасности при подписании сообщений в
    // соответствии со стандартом EIP-712.
    bytes32 private constant MESSAGE_TYPEHASH = keccak256("AirdropClaim(address account,uint256 amount)");

    // define the message hash struct
    struct AirdropClaim {
        address account;
        uint256 amount;
    }

    event Claimed(address account, uint256 amount);
    event MerkleRootUpdated(bytes32 newMerkleRoot);

    constructor(bytes32 merkleRoot, IERC20 airdropToken) EIP712("Merkle Airdrop", "1.0.0") {
        i_merkleRoot = merkleRoot;
        i_airdropToken = airdropToken;
    }

    function claim(
        address account, // The address of the account attempting to claim the airdrop.
        uint256 amount, // The amount of tokens being claimed by the account.
        bytes32[] calldata merkleProof, // A proof (array of hashes) used to verify the account's presence in the Merkle
            // tree.
        uint8 v, // Part of the signature (EIP-712) for verifying the claim, representing the recovery id.
        bytes32 r, // Part of the signature (EIP-712), representing the first 32 bytes of the signature.
        bytes32 s // Part of the signature (EIP-712), representing the second 32 bytes of the signature.
    )
        external
    {
        // Check if the account has already claimed the airdrop by looking it up in the `s_hasClaimed` mapping.
        // If the account has already claimed (mapping value is true), revert the transaction with a custom error.
        if (s_hasClaimed[account]) {
            revert MerkleAirdrop__AlreadyClaimed(); // Error indicating that the user has already claimed the tokens.
        }

        // Verify that the signature is valid using the `_isValidSignature` function.
        // The function checks if the account has signed a valid message indicating they are entitled to claim tokens.
        // The message hash is generated with `getMessageHash(account, amount)`, and the signature is passed as `v`,
        // `r`, and `s`.
        if (!_isValidSignature(account, getMessageHash(account, amount), v, r, s)) {
            revert MerkleAirdrop__InvalidSignature(); // Error if the signature is not valid.
        }

        // Create a "leaf" in the Merkle tree by hashing the concatenated result of the account and amount.
        // This ensures the unique representation of the account and the amount they are claiming within the Merkle
        // tree.
        // The `abi.encode` function serializes the data, and `keccak256` creates a unique hash from it.
        bytes32 leaf = keccak256(bytes.concat(keccak256(abi.encode(account, amount))));

        // Verify that the leaf (account and amount) exists in the Merkle tree by checking the Merkle proof.
        // The `MerkleProof.verify` function ensures that the provided proof links the leaf to the root of the Merkle
        // tree.
        // If the verification fails, the transaction is reverted with an "Invalid Proof" error.
        if (!MerkleProof.verify(merkleProof, i_merkleRoot, leaf)) {
            revert MerkleAirdrop__InvalidProof(); // Error if the proof does not match the Merkle root.
        }

        // Mark the account as having claimed the airdrop by setting its value in the `s_hasClaimed` mapping to true.
        // This prevents the account from claiming more than once.
        s_hasClaimed[account] = true;

        // Emit the `Claimed` event to notify off-chain systems (like logs or dapps) that the account has successfully
        // claimed tokens.
        // The event logs the account and the amount claimed, which can be used for auditing or tracking.
        emit Claimed(account, amount);

        // Transfer the airdrop tokens from the contract to the account using the `safeTransfer` function.
        // `safeTransfer` from `SafeERC20` ensures that the transfer does not fail silently (e.g., if the recipient
        // cannot accept ERC20 tokens).
        i_airdropToken.safeTransfer(account, amount);
    }

    // message we expect to have been signed
    function getMessageHash(address account, uint256 amount) public view returns (bytes32) {
        // _hashTypedDataV4 is a helper function that applies the EIP-712 domain separator to the data.
        // This makes sure that the data (account and amount) is signed in a standard way using the EIP-712 scheme.
        // The domain separator uniquely identifies this contract and protects against replay attacks on other domains.
        return _hashTypedDataV4(
            // The keccak256 function is used to hash the encoded data.
            // Here, we are encoding the `MESSAGE_TYPEHASH` (a constant hash representing the structure of the message),
            // along with the `account` and `amount` parameters, as per the EIP-712 standard.
            // This forms the actual message that will be signed by the user and verified later.
            keccak256(
                abi.encode(
                    MESSAGE_TYPEHASH, // A predefined hash representing the type of message (AirdropClaim structure).
                    AirdropClaim({ // Struct-like encoding of the message data.
                        account: account, // Address of the user who is claiming the airdrop.
                        amount: amount // Amount of tokens being claimed.
                     })
                )
            )
        );
    }

    /*//////////////////////////////////////////////////////////////
                             VIEW AND PURE
    //////////////////////////////////////////////////////////////*/
    function getMerkleRoot() external view returns (bytes32) {
        return i_merkleRoot;
    }

    function getAirdropToken() external view returns (IERC20) {
        return i_airdropToken;
    }

    /*//////////////////////////////////////////////////////////////
                             INTERNAL
    //////////////////////////////////////////////////////////////*/

    // verify whether the recovered signer is the expected signer/the account to airdrop tokens for
    function _isValidSignature(
        address signer,
        bytes32 digest,
        uint8 _v,
        bytes32 _r,
        bytes32 _s
    )
        internal
        pure
        returns (bool)
    {
        // could also use SignatureChecker.isValidSignatureNow(signer, digest, signature)
        (
            address actualSigner,
            /*ECDSA.RecoverError recoverError*/
            ,
            /*bytes32 signatureLength*/
        ) = ECDSA.tryRecover(digest, _v, _r, _s);
        return (actualSigner == signer);
    }
}
