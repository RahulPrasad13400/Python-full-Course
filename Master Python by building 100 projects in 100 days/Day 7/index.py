import random

word_list = ["hello", "world", "python", "is", "awesome"]

random_word = random.choice(word_list)
placeholder = ['_'] * len(random_word)
print(''.join(placeholder))

guess = input("guess a letter").lower()
print(guess)

display = ''

for letter in random_word:
    if letter == guess:
        display += letter
    else:
        display += '_'

print(display)


# for letter in random_word:
#     if(guess == letter):
#         print("Right")
#     else:
#         print("Wrong")