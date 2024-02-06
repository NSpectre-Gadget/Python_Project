from brownie import (
    FundMe,
    MockV3Aggregator,
    accounts,
    config,
    network,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache", "hardhat", "local-ganache", "mainnet-fork"]
)


from scripts.helpful_scripts import get_account


def get_account(index=None, id=None):
    # accounts[0'
    # # accounts.add("env")
    # accounts.load("id")
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    return None
