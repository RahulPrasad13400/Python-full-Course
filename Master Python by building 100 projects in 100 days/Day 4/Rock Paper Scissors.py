import random
# import my_module

# print(random.randint(1, 10))
# print(my_module.my_favourite_number) # imported value from the my_module 

# print(random.random())


# list1 = ['apple', 'banana', 'cherry']
# list1.append('coconut')
# list1.extend(['A', 'B'])
# print(list1)

# list2 = ['Aa', 'Bb', 'Cc']
# print(random.choice(list2))

user_choice = int(input("What do you choose Type 0 for Rock 1 for paper and 2 for scissors."))
computer_choice = random.randint(0,2)

if user_choice == 0 and computer_choice == 2:
    print("User wins")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("User lose")
elif computer_choice < user_choice:
    print("User Wins")
elif computer_choice == user_choice:
    print("Its a draw")
elif user_choice >=3 or user_choice < 0:
    print("Invalid")