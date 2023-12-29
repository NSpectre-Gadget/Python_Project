from brownie import get_account
from scripts.helpful_scripts import get_account, AdvancedCollectible, OPENSEA_URL

sample_token_uri = (
    "ipfs://Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
)


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy("from", account)


def main():
    deploy_and_create()
