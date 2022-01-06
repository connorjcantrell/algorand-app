# Getting Started

This tutorial is designed to get you started with Algorand development in a step by step process. By the end of your journey, you will have:
- Set up your own development environment
- Create Accounts using the Python SDK
- Send transactions using your own CLI application

## Create a local, private network using Algorand Sandbox
A development environment requires getting access to an Algorand node. You need to access a node to submit new transactions, read data from the blockchain, and manage wallets.

The most-used option is setting up the Algorand sandbox. The sandbox allows developers to create local, private networks. To run the Algorand sandbox, open a terminal and run:
```
git clone git clone https://github.com/algorand/sandbox.git
cd sandbox
./sandbox up
```
*Note: Make sure the docker daemon is running and docker-compose is installed.*

This will run the sandbox shell script with the default configuration

For more details visit: https://github.com/algorand/sandbox)

## Connecting to your node
At the root of the directory, there is a file named `config.json`, which contains the addresses and tokens needed to connect to the Algod client, Indexer client, and KMD client. `config.json` is currently configured to connect to the sandbox API endpoints, but can be changed to connect to any Algorand node.



