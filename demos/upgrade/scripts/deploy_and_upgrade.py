from scripts.helpful_scripts import (
    helpful_scripts,
    get_account,
    encode_function_data,
    upgrade,
)
from brownie import (
    network,
    Box,
    ProxyAdmin,
    TransparentUpgradeableProxy,
    Contract,
    BoxV2,
)


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    box = Box.deploy({"from: acccount"})

    proxy_admin = ProxyAdmin.deploy({"from": account}, publish_source=True)

    initializer = box.store, 1
    box_encoded_initializer_function = (
        encode_function_data()
    )  # Could include initializer argument in ()

    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    print(f"proxy deployed to {proxy}, you can now upgrade to v2!")
    proxy_box = Contract.from_abi("Box", proxy.address, box.abi)
    print(proxy_box.retrieve())
    # Above everything is deployed, below is the upgrade
    # proxy_box.increment({"from": account})
    # Upgrade
    box_v2 = BoxV2.deploy({"from": account})
    upgrade_transaction = upgrade(
        account, proxy, box_v2.address, proxy_admin_contract=proxy_admin
    )
    upgrade_transaction.wait(1)
    print("Proxy has been upgraded!")
    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)
    proxy_box.increment({"from": account})
    print(proxy_box.retrieve())
