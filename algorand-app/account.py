from algosdk import account, encoding
from algosdk.future.transaction import PaymentTxn
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

    def send_transaction(self, receiver, amount, note):
        client = algod_client()
        params = client.suggested_params()
        unsigned_txn = PaymentTxn(
            self.address, params, receiver, amount, None, note.encode())
        signed_txn = unsigned_txn.sign(self.private_key)
        txid = client.send_transaction(signed_txn)

        try:
            confirmed_txn = wait_for_confirmation(client, txid, 4)
        except Exception as err:
            print(err)
        print(confirmed_txn)


def generate_account():
    private_key, address = account.generate_account()
    return Account(address, private_key)


def generate_account_with_passphrase(passphrase):
    private_key = mnemonic.to_private_key(passphrase)
    address = account.address_from_private_key(private_key)
    return Account(address, private_key)
