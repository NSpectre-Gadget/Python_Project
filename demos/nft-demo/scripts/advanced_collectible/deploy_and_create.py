from Brownie import AdvancedCollectible, network, config
from scripts.helpful_scripts import (
    fund_with_link,
    get_account,
    get_contracts,
)

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contracts("vrf_coordinator"),
        get_contracts("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )

    fund_with_link(advanced_collectible.address)
    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()
