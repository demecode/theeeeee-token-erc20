// contracts/TheeToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TheeToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("TheeToken", "TT") {
        _mint(msg.sender, initialSupply);
    }
}