#how to create string
str1="this is a string"
str2='this is also a string'
str3='''this is also a string'''
#next line in python
print(str1,str2,str3,sep="\n")
#operations on string
#concate
print(str1+str2)
#length of string use of len function(counts everything from spaces to special character)
print(len(str1))
print(len(str2))
#title method
print(str1.title())
#upper case
print(str1.upper())
#lowercase
print(str1.lower())
#f-string method
print(f"{str1} {str2}")
#remove extra white space from right side (for left side just use lstrip())
x="hey   "
x=x.rstrip()
print(x)
      