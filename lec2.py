str1 = 'This is a string'
str2 = 'learning python'
print(str1+ str2)   # CONCATENATION

str3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \n sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print(str3)

# LENGTH
print(len(str3))

#SLICING
str4 = 'Rahul_Prasad'
print(str4[2:4])
print(str4[-3:-1])

#STRING FUNCTIONS 
str5 = 'rahul'
print(str5.endswith('l')) #returns true if the string ends with the given 
print(str5.capitalize()) #capializes 1st char
print(str5.replace('a','p')) #replaces all the occurence of the old with new 
print(str5.find('h')) #retunrs 1st index of 1st occurence 
print(str5.count('a')) #count the occurence of substrings in a string