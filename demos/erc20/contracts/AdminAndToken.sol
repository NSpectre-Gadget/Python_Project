// SPDX-License-Identifier: MIT
pragma solidity >=0.4.0 <0.9.0;

// K to transfer administrative rights from the admin address to another address
contract Admined {
    address public admin;

    // Establishes the admin as the msg.sender
    function admined() public {
        admin = msg.sender;
    }

    // restricts admin rights to the user of contract
    modifier onlyAdmin() {
        require(msg.sender == admin);
        _;
    }

    // transfers the Admin rights to newAdmin address when called
    function transferAdminship(address newAdmin) public onlyAdmin {
        admin = newAdmin;
    }
}

// Contract for transfer of tokens between accounts; maps token and balance to address
contract TCoin {
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    // balance of address of the sender = 5; e.g. balance Of[address] = 5
    string public standard = "TCoin v1.0";
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;
    event Transfer(address indexed from, address indexed to, uint256 value);

    function tokenCoin(
        uint256 initialSupply,
        string memory tokenName,
        string memory tokenSymbol,
        uint8 decimalUnits
    ) public {
        balanceOf[msg.sender] = initialSupply;
        totalSupply = initialSupply;
        decimals = decimalUnits;
        symbol = tokenSymbol;
        name = tokenName;
    }

    // transfers token when given the address of where the tokens will be sent and how much;
    // also updates each account's balances
    function transfer(address _to, uint256 _value) public {
        require(balanceOf[msg.sender] > _value);
        require(balanceOf[_to] + _value > balanceOf[_to]);

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
    }

    // allows the adminstrator to approve any another account for sending certain value
    // from the admin account to another account.
    function approve(
        address _spender,
        uint256 _value
    ) public returns (bool success) {
        allowance[msg.sender][_spender] = _value;
        return true;
    }

    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) public payable returns (bool success) {
        require(balanceOf[_from] > _value);
        require(balanceOf[_to] + _value > balanceOf[_to]);
        require(_value < allowance[_from][msg.sender]);
        balanceOf[_from] -= _value;
        balanceOf[_to] += _value;
        allowance[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }
}
