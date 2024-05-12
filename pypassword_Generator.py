import random
import string
letters = string.ascii_lowercase
letter=list(letters)
number=['0', '1', '2', '3' ,'4','5','6','7','8','9']
symbol=['!','@','#','$','%','&']
word=int(input("how many letter do you want in your password"))
# print(random.letter)
symbols=int(input("how many symbol do you want to use"))
numbers=int(input("how many number do you wan to use"))
password=[]
for char in range(1,word+1):
    password.append(random.choice(letter))
for char in range(1,numbers+1):
    password.append(random.choice(number))
for char in range(1,symbols+1):
    password.append(random.choice(symbol))
print(password)
random.shuffle(password)
print(password)
passwordstr=""
for char in password:
    passwordstr +=char
print(f"your password could be {passwordstr}")


