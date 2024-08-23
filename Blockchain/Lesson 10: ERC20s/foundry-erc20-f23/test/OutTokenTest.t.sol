//SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

import {Test} from "forge-std/Test.sol";
import {DeployOurToken} from "../script/DeployOurToken.s.sol";
import {OurToken} from "../src/OurToken.sol";

contract OurTokenTest is Test {
    OurToken public ourToken;
    DeployOurToken public deployer;

    address bob = makeAddr("bob");
    address alice = makeAddr("alice");

    uint256 public constant STARTING_BALANCE = 100 ether;

    function setUp() public {
        deployer = new DeployOurToken();
        ourToken = deployer.run();

        vm.prank(msg.sender);
        ourToken.transfer(bob, STARTING_BALANCE);
    }

    function testBobBalance() public {
        assertEq(STARTING_BALANCE, ourToken.balanceOf(bob));
    }

    function testAllowances() public {
        uint256 initialAllowance = 1000;

        // Bob approves Alice to spend tokens on his behalf
        vm.prank(bob); // the next transaction will be as if bob is msg.sender
        ourToken.approve(alice, initialAllowance); // bob calls
        uint256 transferAmount = 500;

        vm.prank(alice); // the next transaction will be as if alice is msg.sender
        ourToken.transferFrom(bob, alice, transferAmount); // alice calls
        assertEq(ourToken.balanceOf(alice), transferAmount);
        assertEq(ourToken.balanceOf(bob), STARTING_BALANCE - transferAmount);
    }
}
