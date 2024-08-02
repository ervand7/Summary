const { network } = require("hardhat");

/*
This is the same if we say:
const helperConfig = require("../helper-hardhat-config")
const networkConfig = helperConfig.networkConfig
*/
const { networkConfig, developmentChains } = require("../helper-hardhat-config");

module.exports.default = async ({ getNamedAccounts, deployments }) => {
  const { deploy, log } = deployments;
  const {deployer} = await getNamedAccounts();
  const chainId = network.config.chainId;

  var ethUsdPriceFeedAddress;
  if (developmentChains.includes(network.name)) {
        const ethUsdAggregator = await deployments.get("MockV3Aggregator")
        ethUsdPriceFeedAddress = ethUsdAggregator.address
    } else {
        ethUsdPriceFeedAddress = networkConfig[chainId]["ethUsdPriceFeed"]
    }

  const fundMe = await deploy("FundMe", {
    from: deployer,
    args: [ethUsdPriceFeedAddress], 
    log: true,
  });

  log("FundMe deployed!");
  log("----------------------------------------------");
};

module.exports.tags = ["all", "fundme"]