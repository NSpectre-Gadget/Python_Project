//SPDX-License-Identifier:MIT
pragma solidity >=0.6.0 ,0.8.0;
//Importing a chain link contract from npm
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";

//A contract to accept some kind of payment
contract FundMe {
    using SafeMathChainlink for uint256;
    //Keeps track of everyone that sent us value
    mapping(address => uint256) public addressToAmountFunded;
    address[] public funders;
    //function payable means this function can be used to pay for things
    address public owner;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    //Someone funds this contract and the K pushes them onto funders array above
    function fund() public payable {
        uint256 minimumUSD = 50 * 10 ** 18;
        //1gwei<$50
        require(
            getConversionRate(msg.value) >= minimumUSD,
            "There is not enough ETH to execute the function for Converstion Rate"
        );
        //Track all the addresses that sent us value or wei
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    //what the ETH -> USD conversion
    function getVersion() public view returns (uint256) {
        //AggregatorV3Interface priceFeed = AggregatorV3Interface(
        //    0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419
        //); commented out here because we used the constructor to acquire the pricefeed
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        //AggregatorV3Interface priceFeed = AggregatorV3Interface(
        //    0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419
        //);commented out here because we used the constructor to acquire the pricefeed
        (, int256 answer, , , ) = priceFeed.latestRoundData(); //Chainlink Oracle
        return uint256(answer * 10000000000);
    }

    function getConversionRate(
        uint256 ethAmount
    ) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    function getEntranceFee() public view returns (uint256) {
        // minimuUSD
        uint256 minimumUSD = 50 * 10 ** 18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10 ** 18;
        return (minimumUSD * precision) / price;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    //the following states who ever calls this function transfer to their address the balance in this K
    function withdraw() public payable onlyOwner {
        //Must include require msg.sender=owner to restrict withdrawal to only the contract admin/owner
        msg.sender.transfer(address(this).balance);
        //There is funderIndex that will start at ) and this loop is going ot finish whenever funders
        for (
            uint256 funderIndex = 0;
            funderIndex < funders.length;
            funderIndex++
        ) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}
