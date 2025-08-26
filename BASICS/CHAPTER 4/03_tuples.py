#tuples- allows to create immutable sequence of values
tuples=(3,2,5,6)
#access element in tuples
print(tuples[0])
#you cannot modify the value because it is immutable
#slicing
print(tuples[1:3])
#tuples method
#index- returns index of first occurence
print(tuples.index(2))
#count- count total occurences
print(tuples.count(3))