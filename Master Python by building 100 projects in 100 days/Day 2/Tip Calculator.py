# print("welcome to the tip calculator.")
# bill = float(input("what was the total bill"))
# tip = int(input("what percentage tip would you like to give!"))
# people = int(input("How many people to split the bill with"))
# tip_as_percent = tip/100
# total_tip_amount = bill*tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill/people
# final_amount = round(bill_per_person, 2)
# print(f"333 test")


# name = "Rahul"
# age = 24
# print(f"My name is {name} and I am {age} years old.")


# num_to_check = int(input("Enter the number to check!"))
# if num_to_check%2==0:
#     print("even number")
# else:
#     print("odd number")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm"))

if height > 120:
    print("You can have a ride!")
    age = int(input("Enter your age"))
    if age <=12:
        bill = 5
    elif age <=18:
        bill = 7
    else:
        bill = 12


    want_photo = input("Do you want the photo!")
    if want_photo == 'y':
        bill += 3

    print(f"Your final bill {bill}")

else:
    print("Sorry you can't")