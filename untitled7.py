"""
Created on Thu Jul  7 10:34:09 2016

@author: student
"""

'''Prompt: Guess the password.
Write a while loop that checks if a string (called password)
is the same as the guessed password
The actual password should be 4 characters long, using 
all capital letters of the alphabet. The loop should
let the guesser know if the password is wrong or not '''

'''
password = "PARA"
guess = (input("Guess the password"))


while guess!=password:
    print("This is incorrect")
    guess = input("Enter a password")

print("Guess is right")
'''





#FOR LOOP
for i in range(0,10):
    print(i)

string = "Do you wanna be my lover"
for char in string: #goes through each character in string
    print(char)