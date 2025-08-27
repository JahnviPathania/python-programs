#dictionary methods
#sample dictionary
dictionary={"name":"sam","age":24,"gender":"male","position":"senior developer"}
#keys method- return all keys
print(dictionary.keys())
#values - return all the values
print(dictionary.values())
#items- print both keys and values as pair
print(dictionary.items())
#get - return values according to key
h=dictionary.get("name")
print(h)
#update - inserts specified items to the dictionary
dictionary.update({"name":"samuel"})
print(dictionary)


