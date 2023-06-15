import shift_operators
import keygeneration

def decrypt(encrypt_list , encryp_key):
    decrypt_list = []
    print("ENCRYPTED BLOCK :" , encrypt_list)
    for i in range(len(encrypt_list)):
        decrypt_str = encrypt_list[i]
        for j in range(len(encrypt_list)):
            call_round_key = keygeneration.key_provider(encryp_key , (len(encrypt_list)-i-1)*(len(encrypt_list)-j-1))
            decrypt_str = shift_operators.xor(decrypt_str , call_round_key)
            decrypt_str = shift_operators.circular_left_shift(decrypt_str , (len(encrypt_list)-j-1))
            left_most_bits = (decrypt_str[0:64])
            left_mid_bits = (decrypt_str[64:128])
            right_mid_bits = (decrypt_str[128:192])
            right_most_bits = (decrypt_str[192:256])
            decrypt_str = (right_mid_bits) + (left_most_bits) + (right_most_bits) + (left_mid_bits)    
            left_mid_bits = shift_operators.xor(left_mid_bits , right_most_bits)
            right_mid_bits = shift_operators.xor(right_mid_bits,left_most_bits)
            for k in range(len(encrypt_list)):
                left_most_bits = decrypt_str[0:64]
                # print("LMB = " , left_most_bits)
                left_mid_bits = decrypt_str[64:128]
                # print("LMidB = " , left_mid_bits)
                right_mid_bits = decrypt_str[128:192]
                # print("RMidB = " , right_mid_bits)
                right_most_bits = decrypt_str[192:256]
                # print("RMB = " , right_most_bits)
                decrypt_str = (left_mid_bits) + (right_most_bits) + (left_most_bits) + (right_mid_bits)      
        decrypt_list.append(decrypt_str)
    return (decrypt_list)
