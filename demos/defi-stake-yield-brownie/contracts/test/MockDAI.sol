//SPDX-License-Identifier: MIT
pragma solidity >=0.4.0 <0.9.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MockDAI is ERC20 {
    constructor() public ERC20("Mock DAI", "DAI") {}
}
