const ethers = require("ethers");
const fs = require("fs-extra");

async function main() {
  const provider = new ethers.providers.JsonRpcProvider(
    "http://127.0.0.1:7545"
  );

  const wallet = new ethers.Wallet(
    "0xa78a186c58db50cbb15822332181a70878c1eecef7831dae71f83f35ad21669e",
    provider
  );

  const abi = fs.readFileSync("./SimpleStorage_sol_SimpleStorage.abi", "utf8");

  const binary = fs.readFileSync(
    "./SimpleStorage_sol_SimpleStorage.bin",
    "utf8"
  );

  const contractFactory = new ethers.ContractFactory(abi, binary, wallet);
  const nonce = await wallet.getTransactionCount();

  console.log("Let's create with only transaction data: ");
  tx = {
    nonce: nonce,
    gasPrice: 20000000000,
    gasLimit: 1000000,
    to: null,
    value: 0,
    // 0x + data from SimpleStorage_sol_SimpleStorage.bin
    data: "0x608060405234801561001057600080fd5b506105b3806100206000396000f3fe608060405234801561001057600080fd5b50600436106100575760003560e01c80632e64cec11461005c5780636057361d1461007a5780636f760f41146100a85780638bab8dd51461016d5780639e7a13ad1461023c575b600080fd5b6100646102ea565b6040518082815260200191505060405180910390f35b6100a66004803603602081101561009057600080fd5b81019080803590602001909291905050506102f3565b005b61016b600480360360408110156100be57600080fd5b81019080803590602001906401000000008111156100db57600080fd5b8201836020820111156100ed57600080fd5b8035906020019184600183028401116401000000008311171561010f57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290803590602001909291905050506102fd565b005b6102266004803603602081101561018357600080fd5b81019080803590602001906401000000008111156101a057600080fd5b8201836020820111156101b257600080fd5b803590602001918460018302840111640100000000831117156101d457600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f8201169050808301925050505050505091929192905050506103d8565b6040518082815260200191505060405180910390f35b6102686004803603602081101561025257600080fd5b8101908080359060200190929190505050610406565b6040518083815260200180602001828103825283818151815260200191508051906020019080838360005b838110156102ae578082015181840152602081019050610293565b50505050905090810190601f1680156102db5780820380516001836020036101000a031916815260200191505b50935050505060405180910390f35b60008054905090565b8060008190555050565b600160405180604001604052808381526020018481525090806001815401808255809150506001900390600052602060002090600202016000909190919091506000820151816000015560208201518160010190805190602001906103639291906104d2565b505050806002836040518082805190602001908083835b6020831061039d578051825260208201915060208101905060208303925061037a565b6001836020036101000a0380198251168184511680821785525050505050509050019150509081526020016040518091039020819055505050565b6002818051602081018201805184825260208301602085012081835280955050505050506000915090505481565b6001818154811061041657600080fd5b9060005260206000209060020201600091509050806000015490806001018054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156104c85780601f1061049d576101008083540402835291602001916104c8565b820191906000526020600020905b8154815290600101906020018083116104ab57829003601f168201915b5050505050905082565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282610508576000855561054f565b82601f1061052157805160ff191683800117855561054f565b8280016001018555821561054f579182015b8281111561054e578251825591602001919060010190610533565b5b50905061055c9190610560565b5090565b5b80821115610579576000816000905550600101610561565b509056fea264697066735822122035d4ef1895b71f28fd7d2165dbdfd00bdb3c214bb39f4ff46d85955b5cb6b33464736f6c63430007050033",
    // networkId from Ganache
    chainId: 1337,
  };

  const sentTxResponse = await wallet.sendTransaction(tx); // signing and sending
  await sentTxResponse.wait(1);
  console.log(sentTxResponse);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });