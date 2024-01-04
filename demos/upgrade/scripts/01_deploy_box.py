from scripts.helpful_scripts import helpful_scripts, get_account
from brownie import network, Box


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    box = Box.deploy({"from: acccount"})
    print(box.increment())
