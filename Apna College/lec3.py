#conditions 
age = 21
if(age >= 21):
    print('eligible to drive')
elif(age == 20):
    print('oii')

#EXAMPLE 2
num = 14
rem = num % 2
if(rem == 0):
    print("EVEN")
else:
    print("ODD")


#GREATEST AMONG THREE NUMBER
a = 10
b = 20
c = 30
if(a > b and a > c):
    print('First Number Is Greatest')
elif(b > a and b > c):
    print('Second Number Is Greatest')
else:
    print('Third Number Is Greatest')


#LIST SLICING 
data = [87,64,33,95,76]
print(data[1:4])
print(data[:4])
print(data[1:])
print(data[-3:-1])

#LIST METHOD
list1 = [2,1,3]
list1.sort()
list1.append(4)
list1.sort(reverse=True)
list1.reverse()
list1.insert(2, 9)
print(list1)

list2 = [2,5,1,7,1]
list2.remove(2)
print(list2)
list2.pop(3)
print(list2)


#TUPLES
#A BUIT IN DATA TYPES THAT LETS US CREATE IMMUTABLE SEQUENCES OF VALUES 
tup = (2,4,6)
print(tup)
print(tup[1])
print(tup[1:3])

#QN1, ENTER THE NAME OF 3 MOVIES AND STORE IT ON A LIST 
# mov1 = input("Enter the name of 1st movie")
# mov2 = input("Enter the name of 2nd movie")
# mov3 = input("Enter the name of 3rd movie")
# movies = []
# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)
# print(movies)

#QN2, CHECK IF A LIST CONTAINS PALINDROME OF ELEMENTS
list5= [1,2,1]
list5_cop1 = list5.copy()
list5_cop1.reverse()
if(list5_cop1 == list5):
    print("Is palindrome")
else:
    print("Not palindrome")