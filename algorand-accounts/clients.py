import json
from algosdk.v2client import algod, indexer

with open("../clients.json", 'r') as rf:
    data = rf.read()

obj = json.loads(data)


def algod_client():
    """Instantiate and return Algod client object"""
    address = obj["clients"]["algod"]["address"]
    token = obj["clients"]["algod"]["token"]
    return algod.AlgodClient(token, address)


def indexer_client():
    """Instantiate and return Indexer client object"""
    address = obj["clients"]["indexer"]["address"]
    token = obj["clients"]["indexer"]["token"]
    return indexer.IndexerClient(token, address)
