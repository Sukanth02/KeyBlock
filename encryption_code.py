import time as tt
import random as rr
import math
import sys
import shift_operators
import keygeneration
import put_ganache

def encryption(binary_input_list):
    #BLOCK DERIVATION FROM PLAIN TEXTS
    block_encryp_list = []
    added_inp_bin = ""
    for i in binary_input_list:
        added_inp_bin = added_inp_bin + str(i)
    if(len(added_inp_bin) < 256):    
        required_padding_len = 256 - len(added_inp_bin)
        added_inp_bin = added_inp_bin =  "0" * required_padding_len   
    else:
        for i in range(math.ceil(len(added_inp_bin)/256)):
            block_encryp_list.append(added_inp_bin[(i*256):256+(i*256)])
            if(len(block_encryp_list[-1]) != 256):
                padding_length = 256 - len(block_encryp_list[-1])
                block_encryp_list[-1] = block_encryp_list[-1] +  "0"*padding_length

    print("BLOCK LIST = " , block_encryp_list)        
    #ACTUAL ENCRYPTION USING BLOCKS
    encryp_key = keygeneration.key_initialise()
    put_ganache.put_block(encryp_key)
    print("------------------------------")
    print("ENCRYPTION KEY = ",encryp_key)
    print("------------------------------")
    encrypt_list = []
    for i in range(len(block_encryp_list)):
        encrypt_str = block_encryp_list[i]
        for j in range(len(block_encryp_list)):
            for k in range(len(block_encryp_list)):
                left_most_bits = encrypt_str[0:64]
                # print("LMB = " , left_most_bits)
                left_mid_bits = encrypt_str[64:128]
                # print("LMidB = " , left_mid_bits)
                right_mid_bits = encrypt_str[128:192]
                # print("RMidB = " , right_mid_bits)
                right_most_bits = encrypt_str[192:256]
                # print("RMB = " , right_most_bits)
                encrypt_str = str(left_mid_bits) + str(right_most_bits) + str(left_most_bits) + str(right_mid_bits)
            left_most_bits = str(encrypt_str[0:64])
            left_mid_bits = str(encrypt_str[64:128])
            right_mid_bits = str(encrypt_str[128:192])
            right_most_bits = str(encrypt_str[192:256])
            left_mid_bits = shift_operators.xor(left_mid_bits,right_most_bits)
            right_mid_bits = shift_operators.xor(right_mid_bits,left_most_bits)
            encrypt_str = str(left_mid_bits) + str(right_most_bits) + str(left_most_bits) + str(right_mid_bits)
            #CIRCULAR RIGHT SHIFTING OF THE BITS IN ENCRYP_STR
            encrypt_str = shift_operators.circular_right_shift(encrypt_str,j) 
            #GETTING THE ROUND KEY FROM KEYGENERATION.KEY_PROVIDER 
            call_round_key = keygeneration.key_provider(encryp_key,j*i)
            encrypt_str = shift_operators.xor(encrypt_str,call_round_key)
        encrypt_list.append(encrypt_str)    
    return encrypt_list , encryp_key, block_encryp_list  





            




