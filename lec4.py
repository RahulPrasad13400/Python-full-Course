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

# SET UNION AND INTERSECTION
set1 = {4, 5, 6}
set2 = {6, 9, 0}
print(set1.union(set2))
print(set1.intersection(set2))
