from algosdk import mnemonic
from clients import algod_client

def passphrase_from_private_key(private_key):
    """Return passphrase from provided private key."""
    return mnemonic.from_private_key(private_key)

def account_balance(address):
    """Return funds balance of the account having provided address."""
    account_info = algod_client().account_info(address)
    return account_info.get("amount")

