from web3 import Web3

# Connect to an Ethereum node using Infura's public node endpoint
infura_url = "https://mainnet.infura.io/v3/de34823b0cc8433fa2269b080678e1b1"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Set up the account that will sign the transaction
private_key = '0x234E157e169A51bC689448058F2D544605252A85'
account = web3.eth.account.from_key(private_key)

# Define the content to be added to the blockchain
content = "Hello, Ethereum world!"

# Define the transaction parameters
transaction = {
    'to': '', # A null recipient address signifies a new contract
    'value': 0, # No Ether value is being sent with this transaction
    'gas': 0, # The amount of gas to use for the transaction
    'gasPrice': web3.toWei('50', 'gwei'), # The price of gas in wei (1 gwei = 10^9 wei)
    'nonce': web3.eth.getTransactionCount(account.address), # The account's transaction nonce
    'data': web3.toHex(text=content) # The content to be added to the blockchain, converted to hexadecimal format
}

# Sign and send the transaction
signed_txn = account.signTransaction(transaction)
tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
print(f"Content added to blockchain with transaction hash: {web3.toHex(tx_hash)}")
