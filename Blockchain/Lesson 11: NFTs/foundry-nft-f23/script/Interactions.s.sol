// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import {Script, console} from "forge-std/Script.sol";
import {DevOpsTools} from "lib/foundry-devops/src/DevOpsTools.sol";
import {BasicNft} from "../src/BasicNft.sol";

// import {MoodNft} from "../src/MoodNft.sol";

// we call this contract only after we deploy BasicNft
contract MintBasicNft is Script {
    string public constant PUG_URI =
        "ipfs://bafybeig37ioir76s7mg5oobetncojcm3c3hxasyd4rvid4jqhy4gkaheg4/?filename=0-PUG.json";

    function run() external {
        address mostRecentlyDeployedBasicNft = DevOpsTools
            .get_most_recent_deployment("BasicNft", block.chainid);
        mintNftOnContract(mostRecentlyDeployedBasicNft);
    }

    function mintNftOnContract(address basicNftAddress) public {
        vm.startBroadcast();
        // The constructor in the BasicNft contract does not require any input parameters.
        // However, when you use BasicNft(basicNftAddress), you're not calling the constructor;
        // instead, you're telling the script, "I know there's a contract of type BasicNft deployed at basicNftAddress. Let's interact with it."
        BasicNft(basicNftAddress).mintNft(PUG_URI);
        vm.stopBroadcast();
    }
}

// contract MintMoodNft is Script {
//     function run() external {
//         address mostRecentlyDeployedMoodNft = DevOpsTools.get_most_recent_deployment("MoodNft", block.chainid);
//         mintNftOnContract(mostRecentlyDeployedMoodNft);
//     }

//     function mintNftOnContract(address moodNftAddress) public {
//         vm.startBroadcast();
//         MoodNft(moodNftAddress).mintNft();
//         vm.stopBroadcast();
//     }
// }

// contract FlipMoodNft is Script {
//     uint256 public constant TOKEN_ID_TO_FLIP = 0;

//     function run() external {
//         address mostRecentlyDeployedMoodNft = DevOpsTools.get_most_recent_deployment("MoodNft", block.chainid);
//         flipMoodNft(mostRecentlyDeployedMoodNft);
//     }

//     function flipMoodNft(address moodNftAddress) public {
//         vm.startBroadcast();
//         MoodNft(moodNftAddress).flipMood(TOKEN_ID_TO_FLIP);
//         vm.stopBroadcast();
//     }
// }
