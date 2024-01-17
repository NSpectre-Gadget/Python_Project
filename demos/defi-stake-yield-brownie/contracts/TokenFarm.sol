//SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract TokenFarm is Ownable {
    // mapping token address --> staker address --> amount; So we know how much of each token each staker has staked.
    mapping(address => mapping(address => uint256)) public stakingBalance;
    mapping(address => uint256) public uniqueTokensStaked;
    mapping(address => address) public tokenPriceFeedMapping;
    address[] public stakers;
    // stakeTokens
    // unStakeTokens
    // issueTokens
    // addAllowedTokens
    // getEthValue
    //SPDX-License-Identifier: MIT
    address[] public allowedTokens;
    IERC20 public dappToken;

    constructor(address _dappTokenAddress) public {
        dappToken = IERC20(_dappTokenAddress);
    }

    // Set the priceFeed associated with the token
    function setPriceFeedContract(
        address _token,
        address _priceFeed
    ) public onlyOwner {
        tokenPriceFeedMapping[_token] = _priceFeed; // Chainlink Smart K Docs or docs.chain.link and price feeds to select
        // appropriate price feed.
    }

    // 100 ETH 1:1 for every 1 ETH, we give 1 DappToken
    //50 ETH and 50 DAI staked, and we want to give a reward of 1 DAPP / 1 DAI
    function issueTokens() public onlyOwner {
        // Issue tokens to all stakers or how do we issue tokens
        // We need a list of stakers to go along with the list of acceptable/allowed tokens
        // So we make a global variable address list of stakers
        for (
            uint256 stakersIndex = 0;
            stakersIndex < stakers.length;
            stakersIndex++
        ) {
            address recipient = stakers[stakersIndex];
            uint256 userTotalValue = getUserTotalValue(recipient);
            dappToken.transfer(recipient, userTotalValue);
            // send them a token reward
            // based on their total value locked
            // dappToken.transfer(receipient, ???);
        }
    }

    function getUserTotalValue(address _user) public view returns (uint256) {
        uint256 totalValue = 0;
        require(uniqueTokensStaked[_user] > 0, "No tokens staked.");
        for (
            uint256 allowedTokensIndex = 0;
            allowedTokensIndex < allowedTokens.length;
            allowedTokensIndex++
        ) {
            totalValue =
                totalValue +
                getUserSingleTokenValue(
                    _user,
                    allowedTokens[allowedTokensIndex]
                );
        }
        return totalValue;
    }

    function getUserSingleTokenValue(
        address _user,
        address _token
    ) public view returns (uint256) {
        // We're getting that conversion rate of the value that someone has staked.
        // e.g. - 1 ETH -> $2,000; 2000 or 200 DAI -> 200
        if (uniqueTokensStaked[_user] <= 0) {
            return 0;
        }
        // Get price and stakingBalance.  Price of the token * stakingBalance[_token][user]
        (uint256 price, uint256 decimals) = getTokenValue(_token);
        return ((stakingBalance[_token][_user] * price) / (10 ** decimals));
    }

    function getTokenValue(
        address _token
    ) public view returns (uint256, uint256) {
        // We need to get some pricing information from Chainlink.
        // We will need to map the token address to its priceFeed address
        address priceFeedAddress = tokenPriceFeedMapping[_token];
        // Use the above line on a AggregatorV3Interface such as below:
        // import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol"; found at docs.chain.link/docs/get-the-latest-price/
        // Chainlink Get the Latest Price
        AggregatorV3Interface priceFeed = AggregatorV3Interface(
            priceFeedAddress
        );
        (, int256 price, , , ) = priceFeed.latestRoundData();
        uint256 decimals = priceFeed.decimals();
        return (uint256(price), decimals);
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
            _amount;
        if (uniqueTokensStaked[msg.sender] == 1) {
            stakers.push(msg.sender);
        }
        // Since we have this list for the msg.sender that will be updated whenever they stake or unstake,
        // we can loop through issued tokens to all stakers as in the issueTokens function
    }

    function unstakeTokens(address _token) public {
        uint256 balance = stakingBalance[_token][msg.sender];
        require(balance > 0, "Staking balance cannot be 0");
        IERC20(_token).transfer(msg.sender, balance);
        stakingBalance[_token][msg.sender] = 0;
        uniqueTokensStaked[msg.sender] = uniqueTokensStaked[msg.sender] - 1;
    }

    function updateUniqueTokensStaked(address _user, address _token) internal {
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
