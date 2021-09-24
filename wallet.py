# Import dependencies
import subprocess
import os
import json
from dotenv import load_dotenv
from constants import *
from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)


# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")

# Import constants.py and necessary functions from bit and web3
# YOUR CODE HERE
 
 
# Create a function called `derive_wallets`
def derive_wallets(coin, mnemonic):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive=3 --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    p_status = p.wait()
    print(output)
    return json.loads(output)
    

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {ETH:derive_wallets(ETH,mnemonic), BTCTEST:derive_wallets(BTCTEST, mnemonic)}

#derive_wallets()


# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
#def priv_key_to_account(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
#def create_tx(account, recipient, amount):
    # YOUR CODE HERE

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
#def send_tx(# YOUR CODE HERE):
    # YOUR CODE HERE

