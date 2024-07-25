const ethers = require("ethers");
const fs = require("fs-extra");

async function main() {
  const provider = new ethers.providers.JsonRpcProvider(
    "HTTP://127.0.0.1:7545"
  );

  const wallet = new ethers.Wallet(
    "0xde214105a954750144d2c67452b04356aa4629289a0ffd0ccb76ed9273c62342",
    provider
  );

  const abi = fs.readFileSync("./SimpleStorage_sol_SimpleStorage.abi", "utf8");

  const binary = fs.readFileSync(
    "./SimpleStorage_sol_SimpleStorage.bin",
    "utf8"
  );

  const contractFactory = new ethers.ContractFactory(abi, binary, wallet);

  console.log("Deploying, please, wait...");

  const gasLimit = 5000000;

  // we can use `await` only inside async func
  const contract = await contractFactory.deploy({
    gasLimit: gasLimit,
  }); // await: STOP here, wait your contract to deploy

  // specify the number of block confirmation we want to wait
  const transactionReceipt = await contract.deployTransaction.wait(1);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
