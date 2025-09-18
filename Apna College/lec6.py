# FUNCTIONS AND RECURSION 
def add(num1, num2):
    return num1+num2
print(add(2,3))

# PRINT THE LENGTH OF A LIST 
list1 = [1, 4, 5, 6]
def lengthOfList(list1):
    return len(list1)
print(lengthOfList(list1))

# PRINT ELEMENTS IN A SINGLE LINE 
def print_list():
    for item in list1:
        print(item, end=' ')
print_list()

# Recursive function to calculate sum of n natural numbers 
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
print('\n',sum(10))

# Recursive function to print all the elements in a list 
sampleList = [2,3,4]
def printEl(list1, idx):
    if(idx == len(sampleList)):
        return
    print(list1[idx])
    printEl(list1, idx+1)
printEl(sampleList, 0)