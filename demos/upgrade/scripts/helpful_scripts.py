from brownie import (
    accounts,
    network,
    config,
)
from web3 import Web3
import eth_utils

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache", "mainnet-fork"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    return None


# initializer=box.store, 1 or 2 or 3 or 4; Here we only have 1 variable to put into store
def encode_function_data(initializer=None, *args):
    """ "Encodes the function call so we can work with an initializer.

    Args:
        initializer ([borwnie.network.contract.ContracTx], optional):
        The initializer function we want to call.  Example:  'box.store'.
        Defaults to NOte.

        args(Any, optional):
        The arguments to pass to the initializer function
    Returns:
        [bytes]: Return the encoded bytes.
    """
    if len(args) == 0 or not initializer:
        return eth_utils.to_bytes(hexstr="0x")
    return initializer.encode_input(*args)


def upgrade(
    account,
    proxy,
    new_implementation_address,
    proxy_admin_contract=None,
    initializer=None,
    *args
):
    if proxy_admin_contract:
        if initializer:
            encoded_function_call = encode_function_data(initializer, *args)
            transaction = proxy_admin_contract.upgradeAndCall(
                proxy.address,
                new_implementation_address,
                encoded_function_call({"from": account}),
            )
        else:
            transaction = proxy_admin_contract.upgrade(
                proxy.address, new_implementation_address, {"from": account}
            )
    else:
        if initializer:
            encoded_function_call = encode_function_data(initializer, *args)
            transaction = proxy.upgradeToAndCall(
                new_implementation_address, encode_function_data, {"from": account}
            )
        else:
            transaction = proxy.upgradeTo(new_implementation_address, {"from": account})
    return transaction
