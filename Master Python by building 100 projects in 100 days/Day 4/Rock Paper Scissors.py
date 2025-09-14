import random
import my_module

print(random.randint(1, 10))
print(my_module.my_favourite_number) # imported value from the my_module 

print(random.random())


list1 = ['apple', 'banana', 'cherry']
list1.append('coconut')
list1.extend(['A', 'B'])
print(list1)