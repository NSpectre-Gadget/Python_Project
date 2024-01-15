//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenFarm is Ownable {
    // mapping token address --> staker address --> amount; So we know how much of each token each staker has staked.
    mapping(address => mapping(address => uint256)) public stakingBalance;
    mapping(addres => uint256) public uniqueTokensStaked;
    address[] public stakers;
    // stakeTokens
    // unStakeTokens
    // issueTokens
    // addAllowedTokens
    // getEthValue
    //SPDX-License-Identifier: MIT
    address[] public allowedTokens;
    IERC20 public dappToken;
    
    constructor(address _dapptokenAddress) public {
        dappToken = IERC20(_dappTokenAddress);
    }

    // 100 ETH 1:1 for every 1 ETH, we give 1 DappToken
    //50 ETH and 50 DAI staked, and we want to give a reward of 1 DAPP / 1 DAI
    function issueTokens() public onlyOwner {
        // Issue tokens to all stakers or how do we issue tokens
        // We need a list of stakers to go along with the list of acceptable/allowed tokens
        // So we make a global variable address list of stakers
        for (uint256 stakersIndex = 0;
        stakersIndex < stakers.length;
        stakersIndex++)
    }{
        address recipient = stakers[stakersIndex];
        uint256 userTotalValue = getUserTotalValue(recipient);
        // send them a token reward
        // based on their total value locked
        // dappToken.transfer(receipient, ???);

        function getUserTotalValue(address _user) pbulic view returns (uint256){
            uint256 totlaVlaue = 0;
            require(uniqueTokensStaked[_user]>0, "No tokens staked.");
            for (uint256 allowedTokensIndex = 0; allowedTokensIndex < allowedTokens.length; allowedTokensIndex++){
                totalValue = totalValue + getUserSingleTokenValue(_user, allowedTokens[allowedTokensIndex]);
            }
        }
    }

    function getUserSingleTokenValue (){
        
    }

    function stakeTokens(uint256 _amount, address _token) public {
        // what tokens can they stake?
        // how much can they stake?
        require(_amount > 0, "Amount must be more than 0");
        //require(_token is allowed???)
        require(tokenIsAllowed(_token), "Token is currently not allowed.");
        //Tranfer function from the ERC20; ERC has 2 transfer type functions;
        //TTRANSFER function only works if it is being called from the wallet that owns the tokens.
        //We are using the TRANSFERFROM function bc our TokenFarm does not own the ERC20. They call for approval 1st.
        //We need the address from, to, value for the the TRANSFERFROM function parameters
        //We need the ABI of the K to call this TRANSFERFROM function. So either include in interface, import, or add the K to the list of contracts
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        // After wrapping the token into ERC20 token, we have the ABI via this interface and token address,
        // we'll call from whoever calls stakeTokens and send to this TokenFarm K address, and send the _amount indicated
        // To keep track of the amount of the tokens they actually sent us, we will use a mapping as above.
        //
        // We also needed to know how many unique tokens the person actually has so we created a function to do so
        updateUniqueTokensStaked(msg.sender, _token);

        stakingBalance[_token][msg.sender] =
            stakingBalance[_token][msg.sender] +
            amount;
        if (uniqueTokensStaked[msg.sender] == 1) {
            stakers.push(msg.sender);
        }
        // Since we have this list for the msg.sender that will be updated whenever they stake or unstake,
        // we can loop through issued tokens to all stakers as in the issueTokens function
    }

    function updateUniqueTokensStaked(adddres _user, addrss _token) internal {
        if (stakingBalance[_token][_user] <= 0) {
            uniqueTokensStaked[_user] = uniqueTokensStaked[_user] + 1;
        }
    }

    function addAllowedTokens(address _token) public onlyOwner {
        allowedTokens.push(_token);
    }

    function tokenIsAllowed(address _token) public returns (bool) {
        for (
            uint256 allowedTokensIndex = 0;
            allowedTokensIndex < allowedTokens.length;
            allowedTokensIndex++
        ) {
            if (allowedTokens[allowedTokensIndex] == _token) {
                return true;
            }
        }
        return false;
    }
}
