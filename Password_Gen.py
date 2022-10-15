import random

length = int(input("How long do you want your password (max is 16 characters and min is 6): "))

password = 'Your password is: '

while length > 16:
    print("Sorry, that's too long!")
    length = int(input("How long do you want your password (max is 16 characters): "))

while length < 6:
    print("Sorry, that's too short!")
    length = int(input("How long do you want your password (max is 16 characters): "))
    
for i in range(length):
    random_character = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|":?><~`-=[]\';,/.')
    
    password += str(random_character)
    

print("------------------------------")
BUFFER = input("Hit [ENTER] to reveal password")
print("------------------------------")
print(password)