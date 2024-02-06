from scripts.helpful_scripts import get_account, interface
from brownie import network, config
from scripts.get_weth import get_weth
from web3 import Web3

# 0.1
amount = Web3.toWei(0.1, "ether")

def main():
    account = get_account()
    erc20_address = config["networks"][network.show_active()]["weth_token"]
    if network.show_active in ["mainnet-fork"]:
        get_weth()
    # May want to call get_weth() K, if we don't already have WETH
    lending_pool = get_lending_pool()
    print(lending_pool)
    # Approve sending out ERC20 tokens
    approve_erc20(amount,lending_pool.address, erc20_address, account)
    # approve ERC 20
    # then deposit
    print("Depositing")
    # Aave ILendingPool function from developers V2 site 
    # function deposit(address asset, uint256 amount, address onBehalfOf, uint16 referralCode) external;
    tx=lending_pool.deposit(erc20_address, amount, account.address, 0, "from": account)
    # Aave lendding pool deposit function explanation: 
    # addressOnBehalfOf = account.address, 
    # referralCode has been deprecated, always pass as 0
    tx.wait(1)
    print("Deposited!")
    # To determine how much?
    borrowable_eth, total_debt = get_borrowable_data(lending_pool, account)
    print("Let's borrow")
    # DAI in terms of ETH
    dai_eth_price = get_asset_price(config["networks"][network.show_active()]["dai_eth_pricefeed"])
    amount_dai_to_borrow = (1/dai_eth_price) * (borrowable_eth * 0.95) # is a cushion on the health factor
    # borrowable_eth -> borrwable_dai * 95%
    print(f"We are going to borrow {amount_dai_to_borrow} DAI")
    # Now we can borrow by using/following the Aave borrow () found in the lendingPool docs
    #function borrow(address asset, uint256 amount, uint256 interestRateMode, uint16 referralCode, address onBehalfOf) external;
    dai_address = config["networks"][network.show_active()]["dai_eth_pricefeed"]
    borrow_tx =lending_pool.borrow(dai_address, Web3.toWei(amount_dai_to_borrow, "ether"), 1, 0, account.address, {"from": account},)
    borrow_tx.wait(1)
    print("We borrowed some DAI!")
    get_borrowable_data(lending_pool, account)
    repay_all(amount, lending_pool, account)
    print("You just deposited, borrowed, and repayed with Aave, Brownie, and Chainlink!")

def repay_all(amount, lending_pool, account):
    approve_erc20(Web3.toWei(amount, "ether"), lending_pool, config["networks", network.show_active()]["dai_token"], account)
    repay_tx = lending_pool.repay(config["netowrks"][network.show_active()]["dai_token"], amount, 1, account.address, {"from": account} )
    repay_tx.wait(1)
    print("Repaid!")
    return repay_tx
    




def get_asset_price(price_feed_address):
    # Remember to get price we need the ABI and Address    
    # Get the price feed for DAI/ETH from Chainlink pricefeeds by adding the 
    dai_eth_price_feed = interface.IAggregatorV3Interface(price_feed_address)
    # the above allows us to use the K to call functions from
    # We can always use the Get the Latest Price info from Chainlink to work with getting the price 
    dai_eth_price_feed = get_asset_price(config["networks"][network.show_active()]["dai_eth_pricefeed"]) # dai_eth_price_feed is the address of DAI/ETH conversion rate
    latest_price = dai_eth_price_feed.latestRoundData()[1]
    converted_latest_price = Web.fromWei(latest_price, "ether")
    # print(f"The DAI/ETH price is {Web3.fromWei(latest_price, "ether")}"), if we did not covert the latest price to ether
    print(f"The DAI/ETH price is {converted_latest_price}")

    return (float(converted_latest_pricee))   



def get_borrowable_data(lending_pool, account):
    # use Aave GetUserAccountData() - function getUserAccountData(address user) get all available using a tuple
    (total_colateral_eth, total_debt_eth, available_borrow_eth, current_liquidation_threshold, ltv, health_factor) = lending_pool.getUserAccountAddress(account.address)
    available_borrow_eth = Web3.fromWei(available_borrow_eth, "ether")
    total_colateral_eth = Web3.fromWei(total_colateral_eth, "ether")
    total_debt_eth = Web3.fromWei(total_debt_eth, "ether")
    print(f"You have{total_debt_eth} workth of ETH borrowed.")
    print(f"You have{total_colateral_eth} workth of ETH deposited.")
    print(f"You can borrow {available_borrow_eth} workth of ETH borrowed.")
    return (float(available_borrow_eth), float(total_debt_eth))

    # ABI
    # Address


def get_lending_pool():
    # look to the Address provider
    lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
        config["networks"][network.show_active()]["lending_pool_addresses_provider"]
    )
    lending_pool_address = lending_pool_addresses_provider.getLendingPool()
    lending_pool = interface.ILendingPool(lending_pool_address)


def approve_erc20(amount, spender, erc20_address, account):
    print("Approving ERC20 token...")
    erc20 = interface.IERC20(erc20_address)
    tx = erc20.approve(spender, amount, {"from": account})
    tx.wait(1)
    print("Approved")
    return tx
