str="wisdom in imperfection"
#string functions
print(str.endswith("on")) #checks if the string ends with the given substring
print(str.capitalize())#  temporarily capitalie first character
#to permanently capitalize
str=str.capitalize()
print(str)
#replace function
print(str.replace("i","o")) #replace character from new character also can relace a substring
print(str.replace("in","with"))#to replace substring
#find function
print(str.find("o"))# returns index of first occurence
#if you search for something that is not in the string you get -1
print(str.find("q"))
#count function
print(str.count("o"))# count number of times a charatcer or substring occured in the string
print(str.count("in"))


