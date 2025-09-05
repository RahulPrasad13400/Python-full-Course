# #LOOPS
# i=0
# while i<5:
#     print("Hello")
#     i=i+1

# #PRINT NUMBER FROM 1 TO 100
# i=0
# while i<=100:
#     print(i)
#     i=i+1

# #PRINT THE MULTIPLICATION TABLE OF N
# i=1
# while i<=10:
#     print('3 *',i,' = ',3*i)
#     i=i+1

# nums = [1, 3, 6, 9, 13]
# i=0
# while i<len(nums):
#     print(nums[i])
#     i += 1

# #SEARCH FOR A NUMBER X IN THIS TUPLE 
# tup = (1,5,3,6,2,9)
# i=0
# x=2
# while i<len(tup):
#     if(x==tup[i]):
#         print("found")
#     i=i+1


#BREAK AND CONTINUE
# i=1
# while i<=10:    #BREAK
#     if(i==3):
#         break 
#     print(i)
#     i=i+1

# i=1
# while i<=10:
#     if(i==3):
#         i=i+1
#         continue
#     print(i)
#     i=i+1

# FOR LOOP
# list1 = [1, 2, 3]
# for el in list1:
#     print(el)

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# for el in numbers:
#     if(el == 9):
#         print("FOUND")
#     else:
#         print("Searching...")

# RANGE 
# for el in range(5):   #range(stop)
#     print(el)
# for el in range(1, 5):    #range(start, stop)
#     print(el)
# for el in range(1, 6, 2):   #range(start, stop, step)
#     print(el)

seq = range(5)
print(range(5))
print(seq[3])