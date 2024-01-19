//SPDX License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contrats/token/ERC20/ERC20.sol";

contract MockWETH is ERC20 {
    constructor() public ERC20("Mock WETH", "WETH") {}
}
