from brownie import (
    accounts,
    network,
    config,
    LinkToken,
    VRFCoordinatorMock,
    VRFCoordinator,
    Contract,
)
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache", "mainnet-fork"]
OPENSEA_URL = "https://testnets.opensea.io/{}/{}"
BREED_MAPPING = {0: "PUG", 1: "SHIBA_INU", 2: "ST_BERNARD"}


def get_breed():
    return BREED_MAPPING[0]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


contract_to_mock = {"link_token": LinkToken, "vrf_coordinator": VRFCoordinatorMock}


def get_contracts(contract_name):
    # link_token
    # LinkToken
    contract_type = contract_to_mock[contract_name]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        if len(contract_type) <= 0:
            deploy_mocks()
        contract = LinkToken[-1]
    else:
        contract_address = config["networks"][network.show_active()][contract_name]
        contract = Contract.from_abi(
            contract_type._name, contract_address, contract_type.abi
        )
    return contract


# deploy_mock()
def deploy_mocks():
    """[Use script if U want to deploy mocks to a testnet]"""
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks...")
    account = get_account()
    print("Deploying mock LinkToken...")
    link_token = LinkToken.deploy({"from": account})
    print(f"Link Token deployed to {link_token}")
    print("Deploying mock VRF Coordinator...")
    vrf_coordinator = VRFCoordinator(link_token.address, {"from": account})
    print("Deploying Mock VRF Coordinator...")
    vrf_coordinator = VRFCoordinatorMock.deploy(link_token.address, {"from": account})
    print(f"VRFCoordinator deployed to {vrf_coordinator.address}")
    print("All Done!")


def fund_with_link(
    contract_address, account=None, link_token=None, amount=Web3.toWei(1, "Ether")
):
    account if account else get_account()
    link_token = link_token if link_token else get_contracts("link_token")
    funding_tx = link_token.transfer(contract_address, amount, {"from": account})
    funding_tx = funding_tx.wait(1)
    print(f"Funded {contract_address}")
    return funding_tx
