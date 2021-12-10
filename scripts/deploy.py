# 1. In order to to deploty a contract you always need an account .....


from scripts.helpers import get_account
from brownie.network.web3 import Web3 
from brownie import TheeToken

initial_supply = Web3.toWei(1000, "ether")


def deploy_toke():
    account = get_account()
    print(account)
    the_toke = TheeToken.deploy(initial_supply, {"from": account})
    print(the_toke.name())



def main():
    deploy_toke()