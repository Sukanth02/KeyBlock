import time as tt
import random as rr
import shift_operators

def key_initialise():
    key_str = ""
    epochtime = int(tt.time())
    # print("EPOCH TIME = ",epochtime)
    epoch_bit = (bin(epochtime).lstrip("0b"))
    # print("BINARY OFF EPCOH TIME = ",epoch_bit)
    epoch_len = len(str(epoch_bit))
    key_permut_order = []
    key_len = 0
    #PERMUTING EPOCH BITS TO GET 256 BIT KEY 
    while(key_len < 256):
        key_permut_index = rr.randint(0,(epoch_len-1))
        key_permut_order.append(key_permut_index)
        key_str = key_str + (epoch_bit[key_permut_index])
        key_len = key_len + 1

    # print("KEY STRING = ",key_str)
    # print("LENGTH OF KEY STRING = ",len(key_str))
    # print("ORDER OF KEY PERMUTATION = " , key_permut_order)
    return key_str

def key_provider(key_string,round_num):
            round_const = (round_num)
            round_key = shift_operators.left_shift(key_string , round_const)
            return round_key




          
