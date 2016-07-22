def decryptCC(encrypted):
    for i in range(26):
        decrypted = ""
        for char in encrypted:
            asc=ord(char)
            if asc >= 65 and asc <= 91:
                asc -= i
                if asc<65:
                    asc+= 26
                decrypted += chr(asc)
            elif asc <= 122 and asc >= 97:
                asc -= i
                if asc<97:
                    asc+=26
                decrypted += chr(asc)
            else:
                decrypted += char
            print(i,decrypted)
            return(i)
        
decryptCC("Zkij te yj.")