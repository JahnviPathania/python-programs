#used to store value in form of key:values
#here key acts as index
#you can store list and tuples in dictionary
#example
dictionary={"name":"jahnvi","age":19,"subjects":["c programming","data science","java programming"],"is_adult":True,}
print(dictionary)
#acess value
print(dictionary["name"])#use key name instead of index
#change value
dictionary["name"]="ashish"
print(dictionary)
#add a new key:value pair
dictionary["surname"]="pathania"
print(dictionary)
#empty dictionaries
null_dict={}
print(null_dict)
#add value in empty dictionaries
null_dict["name"]="jahnvi"
print(null_dict)