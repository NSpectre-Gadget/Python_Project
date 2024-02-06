from scripts.helpful_scripts import get_account
from brownie import interface, config, network

def main():
    get_weth()

def get_weth():
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show.active()]["weth_token"])
    tx = weth.deposit("from": account, "value": 0.1 * 10 **18)
    tx.wait(60)
    print ("Received 0.1Weth")
    return tx
#  Gives an ERC20 token to use in AAVE
#  Swapping WETH for ETH