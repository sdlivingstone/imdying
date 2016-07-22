def cipher(message,shift):
    encryptedmessage = "" #we will add encyption char by char to this string
    for char in message:
        asc =ord(char)
        if asc >= 65 and asc<=91:
            asc+=shift 
            if asc>91: 
                asc-= 26
            encryptedmessage += chr(asc)
        elif asc <=122 and asc>=97:
            asc +=shift 
            if asc>122:
                asc-=26
            encryptedmessage += chr(asc)
        else:
            encryptedmessage += chr(asc)
    print("The message", message, "was shifted by", shift)            
    return encryptedmessage 
msg = input("Secret Message")      
shft= int(input("shift"))  
        
print(cipher(msg,shft))
        
        
        
        
        
        