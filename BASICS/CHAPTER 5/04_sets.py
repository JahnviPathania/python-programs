#set - collection of  unordered items
#set is mutable
#element must be unique and immutable
#list and dictionary cannot be in sets
#sets
collection={1,2,3,4}
set1={5,6,7,8}
print(collection)
print(type(collection))
sets={"apple","apple"}
print(sets)#if value is repeated it only shows it once
# set ignores duplicate value
# empty set
emp_set=set()
# sets methods
# add - adds an element
sets.add("mango")
print(sets)
# remove - remove element from set
sets.remove("apple")
print(sets)
#  #clear - empties the set
sets.clear()
print(sets)
#pop- remove any random value
collection.pop()
print(collection)
#union - combines both set values & return new
print(collection.union(set1))
#intersection- combines common elements & return new
print(collection.intersection(set1))#here output will be null 

