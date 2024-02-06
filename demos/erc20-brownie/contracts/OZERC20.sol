// contracts/GLDToken.sol
// SPDX-License-Identifier: MIT
pragma solidity >=0.4.0 <0.9.0;

import "@chainlink-brownie-contracts/contracts/src/v0.8/vendor/openzeppelin-solidity/v4.8.0/contracts/token/ERC20/ERC20.sol";

contract GLDToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("Gold", "GLD") {
        _mint(msg.sender, initialSupply);
    }
}
