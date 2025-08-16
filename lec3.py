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