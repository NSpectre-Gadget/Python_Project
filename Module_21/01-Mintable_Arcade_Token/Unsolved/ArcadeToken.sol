/*
Arcade Mintable Token

Instructions:

Navigate to Remix, and create a new smart contract file called `ArcadeToken.sol`. Then complete the following steps:

1. Add the following pragma line and import statements:

```solidity
pragma solidity ^0.5.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";
```

2. Define a contract called `ArcadeToken` that inherits the `ERC20`, `ERC20Detailed`, and `ERC20Mintable` contracts.

> **Hint** You can use the `is` keyword in Solidity to inherit code from other contracts.

3. Inside of the `ArcadeToken` contract, create a constructor by using the following code:

```solidity
    constructor(
        string memory name,
        string memory symbol,
        uint initial_supply
    )
        ERC20Detailed(name, symbol, 18)
        public
    {
        mint(msg.sender, initial_supply);
    }
```

4. Navigate to the "Solidity compiler" menu in the Remix sidebar.

5. From the COMPILER drop-down menu, select any version from 0.5.0 to 0.5.17, and click the Compile button.

6. Check for any errors and debug as needed.

*/

// Write the code for the import statements and ArcadeToken contract below:
