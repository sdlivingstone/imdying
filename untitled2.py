# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 09:25:50 2016

@author: student
"""


def decryptCC(encrypted): #one parameter called encrypted. string var
    for i in range(26):  # for loop that goes through numbers 0-26
        decrypted = "" #empty string every iteration of the for loop
        for char in encrypted: 
        #for loop inside for loop that loops through ea. char in string
            asc = ord(char) #convert char to ascii value
            if asc >= 65 and asc <= 91: #check if upper
                asc -= i #decrypt shift
                if asc< 65: #checks if ascii value is below 65 range
                    asc+= 26 #if true, add 26 to make it a letter
                decrypted += chr(asc) #add the decrypted char to decrypted string
            elif asc <= 122 and asc>=97: #check if lower
                asc -= i
                if asc<97:
                    asc+=26 
                decrypted +=chr(asc)
            else:
                decrypted += char #adds random char (not letter) to string
        print(i, decrypted) 
        #print each different variation of CC in the first for loop
    return (True) 

decryptCC("Zkij te yj")