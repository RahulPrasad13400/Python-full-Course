print('''
                     .---.
        .--.     ___/     \
       /    `.-""   `-,    ;
      ;     /     O O  \  /
      `.    \          /-'
     _  J-.__;      _.'
    (" /      `.   -=:
     `:         `, -=|
      |  F\    i, ; -|
      |  | |   ||  \_J
 fsc  mmm! `mmM Mmm''''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input("You are at a crossroad. where do you want to go 'left' or 'right'").lower()
print(choice1)
if choice1 == 'right':
     choice2 = input("You have come accross a lake, what you like to do 'swim' or 'wait'")
     if choice2 == 'wait':
          choice3 = input("Which door you want to choose [red, yellow, blue]")
          if choice3 == 'yellow':
               print("You Won!")
          else :
               print("Game Over!")
     else:
          print("Game Over!")
else:
     print("Game Over!")