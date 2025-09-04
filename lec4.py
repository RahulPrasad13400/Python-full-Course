#DICTIONARY
info = {
    "name" : "Rahul",
    "age" : 23,
    "isAdult" : True,
    "subjectes" : ["python","javascript"] 
}

# print(info.keys())
# print(list(info.keys()))
# print(info.items())  
# print(list(info.items()))  

pairs = list(info.items())
# print(pairs[0])

info.update({"city" : "kochi"})
print(info)

#SET
collection = {1, 2, 4, 5, 5}    
print(collection)   #print only unique values

collection.add(6)
collection.remove(1)
print(collection)
