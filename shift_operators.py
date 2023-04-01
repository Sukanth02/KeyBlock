def left_shift(str_val,shift_number):
    lst_val = list(str_val)
    for l in range(shift_number):
            for i in range(len(lst_val)-1):
                lst_val[i] = lst_val[i+1]
            lst_val[len(lst_val)-1] = '0'  
    return lst_val


def right_shift(str_val,shift_number):
    lst_val = list(str_val)
    for l in range(shift_number):
            for i in range((len(lst_val)-1),0,-1):
                print(i)
                lst_val[i] = lst_val[i-1]
            lst_val[0] = '0'  
    return lst_val   


def circular_left_shift(str_val , shift_number):
    lst3 = list(str_val)
    for l in range(shift_number):
        temp=lst3[0]
        for i in range(1,len(lst3)):
            lst3[i-1]=lst3[i]
        lst3[len(lst3)-1]=temp
    return lst3 

def circular_right_shift(str_val , shift_number):
    lst3 = list(str_val)
    for l in range(shift_number):
        temp=lst3[len(lst3)-1]
        for i in range((len(lst3)-1),0,-1):
            lst3[i]=lst3[i-1]
        lst3[0] = temp
    return lst3

def xor(operand1 , operand2):
    #  print("LENGTHS")
    #  print(operand1)
    #  print(operand2)
    #  print(len(operand1))
    #  print(len(operand2))
     result_str = ""
     for i in range(len(operand1)):
          if operand1[i] == operand2[i]:
               result_str += "0"
          else:
               result_str += "1"
     return result_str
             
                 

