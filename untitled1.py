
'''
WHILE loop - loop that keeps on running code until a certain condition is met
WHILE loop will stop running after the condition is met
'''
'''
myint=465 #type of counter 

while myint > 400:
    #Edit my "counter"
    myint = myint-5
    print(myint)
    

'''
#this imports a random library inside my code
'''

guess = int(input("Guess my number"))
number = random.randint(0,100)

#number guessing game loop


while guess!=number:
    if number < guess:
        print("This Number is too big")
    else:
        print("This number is too small")
    guess = int(input("Guess again"))
    

print("Congrats, the number is correct")
print("Your number was", number)
'''

'''Prompt: Guess the password.
Write a while loop that checks if a string (called password)
is the same as the guessed password
The actual password should be 4 characters long, using 
all capital letters of the alphabet. The loop should
let the guesser know if the password is wrong or not '''

'''guess = (input("Guess the password"))
password = PARA

while guess!password:
    print("This is incorrect")  '''
    
lowercase = False
uppercase = False
length = False
password = input("What's your password?")
if len(password) <6:
    print("password is too short")
else:
    length = True
for i in password:
    if ord(i) >= 65 and ord(i) <=90:
        uppercase = True
    if ord(i) >=97 and ord(i) <=122:
        lowercase = True
if lowercase==True and length==True and uppercase ==True:
    print("Password is good")
        
    









