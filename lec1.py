print("Hello world")
print(100)
print(100+20)

name = 'Rahul'
age = 24
hello = True
print(type(name))
print(type(age))

#   hii i'm a comment

#   relational operators
a=50
b=50
print(a==b)
print(a!=b)

#   ASSIGNMENT OPERATIORS
ao1 = 5
sum = 0
sum += ao1
print(sum)

#   LOGICAL OPERATOR 
print(not False)
print(not True)
print(not (age < a))

val1 = True
val2 = True
val3 = False
print("and :", val1 and val2)
print(val1 and val3)

print("or :", val1 or val2)
print("or :", val1 or val3)

#   TYPE CONVERSION
type1 = 4
type2 = 6.5
type3 = type1 + type2
print("type3 :", type3)

#   TYPE CASTING
typeCasting1 = "2"
typeCasting2 = 4
typeCasting3 = int(typeCasting1) + typeCasting2
print("typeCasting3 :",typeCasting3)

#   INPUT IN PYTHON
name = input("Enter Your Name")
print("Your Name is :", name)

name = input("Enter your name")
age = int(input("Enter the age"))
marks = float(input("Enter the marks"))

print("Welcome", name)
print("Age", age)
print("Marks ", marks)