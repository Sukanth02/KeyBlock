import time as tt
import random as rr
import math
import sys
import shift_operators
import keygeneration
import encryption_code
import decryption

#RECEIVES INT AS BINARY AND THEN PRINTS ITS EQUIVALENT DECIMAL
def binaryToDecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)

def input_ascii():
    inp_str = str(input("Enter String: "))
    str_inp_lst = []
    for i in range(len(inp_str)):
        str_inp_lst.append(ord(inp_str[i]))
    # print("INPUT TO ASCII")
    # print(str_inp_lst)
    return str_inp_lst

def ascii_to_bin(asc_list):
    binary_list = []
    for i in range(len(asc_list)):
        binary_chk_val = bin(asc_list[i]).lstrip("0b")
        if(len(binary_chk_val) == 8):
            binary_list.append(binary_chk_val)
        else :
            required_bits = 8-(len(binary_chk_val))
            binary_chk_val= "0"*required_bits + binary_chk_val
            binary_list.append(binary_chk_val)
    # print("ASCII to BINARY")   
    # print(binary_list) 
    return binary_list    


#Program starts execution here
def main():
   encrypted_bin_values = []
   ascii_input_val = input_ascii()
   binary_input_val = ascii_to_bin(ascii_input_val)
   encryp_values , key_key , block_val = encryption_code.encryption(binary_input_val)
   #print("ENCRYPTED BLOCK : " , encryp_values)
   decrypt_values = decryption.decrypt(encryp_values , key_key )
   print("DECRYPTED : " , block_val)
   print("_______________________________________") 
   print("RESULT STATUS")
   print ("BLOCK LIST IS SAME AS DECRYPTED LIST")
   print("_______________________________________")
main()   
