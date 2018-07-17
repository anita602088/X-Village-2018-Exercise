
def encryption():  
    str_raw = input("請輸入明文:")  
    k = (int(input("請輸入位移值"))%26)  
    str_change = str_raw.lower()  
    str_list = list(str_change)  
    str_list_encry = str_list  
    i = 0  

    while i < len(str_list):  
        if ord(str_list[i]) < 123-k:  
            str_list_encry[i] = chr(ord(str_list[i]) + k)  
        else:  
            str_list_encry[i] = chr(ord(str_list[i]) + k - 26)  
        i = i+1  
    print ("加密結果為："+"".join(str_list_encry))  
