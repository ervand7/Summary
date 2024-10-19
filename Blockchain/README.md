# README

## LiquidityManager Contract

### Overview

The `LiquidityManager` contract allows users to add liquidity to any Uniswap V3 pool by specifying:

- **Pool Address**: The address of the Uniswap V3 pool (`IUniswapV3Pool`).
- **Token Amounts**: The amounts of the two tokens to deposit (`amount0` and `amount1`).
- **Width Parameter**: A parameter that determines the width of the liquidity position based on the formula:

  \[
  \text{width} = \frac{(\text{upperPrice} - \text{lowerPrice}) \times 10000}{\text{lowerPrice} + \text{upperPrice}}
  \]

This contract dynamically retrieves token information from the provided pool, supports any tokens, and performs all calculations on-chain.

### Features

- **Flexible Pool Interaction**: Works with any Uniswap V3 pool regardless of the tokens involved.
- **Customizable Position Width**: Users can specify the width of their liquidity position.
- **On-Chain Calculations**: All computations, including price and tick calculations, are performed entirely on-chain.
- **Unused Token Refunds**: Automatically refunds any unused tokens back to the user after adding liquidity.

### Contract Components

- **LiquidityManager.sol**: The main contract for adding liquidity.
- **TickCalculator.sol**: A library for calculating tick bounds based on the specified width.
- **LiquidityManagerTest.sol**: A suite of tests covering various scenarios to ensure correct functionality.

### How to Use

1. **Deployment**:

   Deploy the `LiquidityManager` contract by providing:

   - The address of the `INonfungiblePositionManager` contract.
   - The address of the `IUniswapV3Pool` you wish to interact with.

2. **Adding Liquidity**:

   Call the `addLiquidity` function with the following parameters:

   - `pool`: The Uniswap V3 pool address.
   - `amount0`: The desired amount of token0 to add.
   - `amount1`: The desired amount of token1 to add.
   - `width`: The desired width of the liquidity position as per the formula.

   ```solidity
   (uint256 tokenId, uint128 liquidity, uint256 amount0Used, uint256 amount1Used) = liquidityManager.addLiquidity(
       poolAddress,
       amount0,
       amount1,
       width
   );
   ```

3. **Token Approvals**:

   Ensure that you have approved the `LiquidityManager` contract to spend your tokens before calling `addLiquidity`.

4. **Receiving Unused Tokens**:

   Any unused tokens after adding liquidity will be automatically refunded to your address.

### Testing

The `LiquidityManagerTest` contract includes multiple test cases covering different scenarios.

**To run the tests:**

1. **Install Foundry** (if not already installed):

   ```bash
   curl -L https://foundry.paradigm.xyz | bash
   foundryup
   ```

2. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Install Dependencies**:

   ```bash
   forge install
   ```

4. **Run Tests**:

   ```bash
   forge test
   ```

### Notes

- The contract is designed to work with Solidity version `0.7.6`.
- It uses OpenZeppelin's `ReentrancyGuard` to prevent reentrancy attacks.
- All interactions are performed on-chain without any off-chain computations.

### Security Considerations

- **Reentrancy Protection**: The contract includes measures to prevent reentrancy attacks.
- **Input Validation**: It validates inputs such as non-zero amounts and valid width parameters.
- **Token Refunds**: Unused tokens are safely returned to the user.

### License

This project is licensed under the MIT License.

---

**Disclaimer**: Always exercise caution and conduct thorough testing when interacting with smart contracts. Ensure you understand the code and its implications before deployment or use.