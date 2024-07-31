const { ethers } = require("hardhat");
const { expect, assert } = require("chai");

describe("SimpleStorage", function () {
  var simpleStorageFactory, simpleStorage;

  beforeEach(async function () {
    simpleStorageFactory = await ethers.getContractFactory("SimpleStorage");
    simpleStorage = await simpleStorageFactory.deploy();
  });

  it("Should stat with a favorite number of 0", async function () {
    const currentValue = await simpleStorage.retrieve();
    assert.equal(currentValue.toString(), "0");
  });

  it("Should update our favorite number when we call `store`", async function () {
    const expectedValue = 7;
    const transactionResponse = await simpleStorage.store(expectedValue);
    await transactionResponse.wait(1);

    const currentValue = await simpleStorage.retrieve();
    assert.equal(currentValue.toString(), expectedValue);
  });
});
