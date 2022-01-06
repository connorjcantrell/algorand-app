from algosdk import account, encoding
from helper import *


class Account():
    def __init__(self, address, private_key):
        self.address = address
        self.private_key = private_key

    def is_valid(self):
        """Check if this instance has a valid Algorand address"""
        return encoding.is_valid_address(self.address)

    def passphrase(self):
        """Return this instance's passphrase"""
        return passphrase_from_private_key(self.private_key)

    def balance(self):
        """Return this instance's balance in microAlgos"""
        return account_balance(self.address)

    def send_transaction(self):
        pass


def generate_account():
    private_key, address = account.generate_account()
    return Account(address, private_key)
