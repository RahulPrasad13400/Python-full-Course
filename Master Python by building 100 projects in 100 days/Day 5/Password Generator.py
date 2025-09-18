import random

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", "\"", ",", ".", "<", ">", "/", "?", "\\", "|", "`", "~"]
numbers = ["0","1","2","3","4","5","6","7","8","9"]

numLetters = int(input("Enter the number of letters"))
numSymbols = int(input("Enter the number of Symbols"))
numNumbers = int(input("Enter the number of Numbers"))

# EASY LEVEL 
# password = ''
# for char in range(1, numLetters+1):
#     password += random.choice(letters)
# for symbol in range(1, numSymbols+1):
#     password += random.choice(symbols)
# for number in range(1, numNumbers+1):
#     password += random.choice(numbers)

# print(password)

# HARD LEVEL 
password = []
for char in range(1, numLetters+1):
    password.append(random.choice(letters))
for symbol in range(1, numSymbols+1):
    password.append(random.choice(symbols))
for number in range(1, numNumbers+1):
    password.append(random.choice(numbers))

print(password)

random.shuffle(password)
print(''.join(password))