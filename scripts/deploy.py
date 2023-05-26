from brownie import accounts, SimpleCollectable
from scripts.helpful_script import get_account
from dotenv import load_dotenv

load_dotenv()

sample_token_uri = (
    "https://ipfs.io/ipfs/QmVasQEZXXL4f7VgfPLvTERcVtT5WVU8cBQcdQmFwQyBwa?filename=mouse.json"
    # "https://ipfs.io/ipfs/QmVaP1oDR82HM2YRNc63bTeGfTdTE2DpjrPiPAq9Yf4eFv?filename=highway.jpg",
    # https://ipfs.io/ipfs/QmegWZuCiZyhdqgp7jL4tTosLfsDWFMf6ryEUXDGgJWdGK?filename=mouse.png
)
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"


def main():
    # account = get_account()
    account = accounts.load("nilesh-account")
    nft_name = "Hell"
    collectables = SimpleCollectable.deploy(nft_name, {"from": account})
    tx = collectables.createCollectibles(sample_token_uri, {"from": account})
    name = collectables.nftName()
    print("NFT_name:", name)
    tx.wait(1)
    print(OPENSEA_URL.format(collectables.address, collectables.tokenCounter() - 1))
