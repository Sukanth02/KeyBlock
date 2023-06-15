from web3 import Web3
import numpy as np
def put_block(key_key_key):
    ganache_url = 'HTTP://127.0.0.1:7545'
    web3 = Web3 (Web3.HTTPProvider (ganache_url))
    account_1 = '0x2A89D41997350475E138184371F3D2a81e654B76'
    private_key1 = '0x63f28253050317745b51620eba990e65f4d8a3c36d4ec8d8a242806576599a9e'
    account_2 = '0x94E2991d19f4c1b27E4E6f7267d1e57607E5BADB'
    private_key2 = '0x10e3b01cfae339e6305baca357bf9c0c1126f07a292fbde8bb13e05f78d2a37c'
    print("GANACHE CONECTION STATUS : ", sep=" ")
    print(web3.is_connected ())
    #send trx from acc2 to acc1
    #get the nonce. Prevents one from sending the transaction twice
    nonce = web3.eth.get_transaction_count (account_2)
    #build a transaction in a dictionary
    # tx = {
    # 'nonce': nonce,
    # 'to': account_1,
    # 'value': web3.to_wei (3, 'ether'), # One ther = 1,000,000,000,000,000,000 wei (10e18)
    # 'gas': 200000,
    # 'gasPrice': web3.to_wei ('50', 'gwei')
    # }
    message = str(key_key_key)
    print(message)
    tx = {
        'nonce': nonce,
        'to': account_1,
        'value': web3.to_wei(3, 'ether'),
        'gas': 200000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'data': message.encode('ascii'),
    }

    #sign the transaction
    signed_tx = web3.eth.account.sign_transaction (tx, private_key2)
    #send transaction
    tx_hash = web3.eth.send_raw_transaction (signed_tx.rawTransaction)
    #get transaction hash
    print("transaction hash", web3.to_hex(tx_hash))
    # print the latest block number
    print("block numbers: ",web3.eth.block_number)
    #nonce