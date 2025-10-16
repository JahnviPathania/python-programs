#formatted twinkle poem
# print("twinkle twinkle little star ,")
# print("        how i wonder what you are !")
# print("                up above the world so high,")
# print("                like a diamond in the sky .")
# print("twinke twinkle, little star,")
# print("        how i wonder what you are")
#python version checker
# import sys
# print(sys.version)
# print(sys.version_info)
# print("aboce is the current version of python")
#current date and time 
# import datetime
# print("the current date and time are")
# now=datetime.datetime.now()
# print(now.strftime("%Y-%m-%d %H:%M:%S"))
# calculate area of circle
# radius=int(input("enter the radius of circle : "))
# area=3.14*radius*radius
# print("area of circle is ", area)
# reverse full name
# fname=input("enter your first name : ")
# lname=input("enter your surname :  ")
# print("hello"+"  "+lname+" "+fname)
#list and tuple generator
# numbers=input("enter numbers : ")
# list=numbers.split(",")
# tuple=tuple(list)
# print("list and tuple generated are :  ")
# print(list)
# print(tuple)
#file extension extractor
# filename=input("enter your file name : ")
# spplit=filename.split(".")
# print("the extension of the given file is : ",spplit[-1])
#Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"]
# print("the first element is : ",color_list[0])
# print("the last element is : ",color_list[-1])
# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
# exam_date=(11,12,2014)
#we can use %i placeholder here
# print("the examination will start from %i/%i/%i"% exam_date) 
# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615
# x=input("enter a number : ")
# n1=int("%s" % x)
# n2=int("%s%s" % (x,x))
# n3=int("%s%s%s"% (x,x,x))
# print(n1+n2+n3)
# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.
# print(abs.__doc__)
# Write a Python program that prints the calendar for a given month and year.
# Note : Use 'calendar' module.
# import calendar
# y=int(input("input the year : "))
# m=int(input("input the month : "))
# print(calendar.month(y,m))
#create  a multi line string
# ''' here is an example of a
# multi line  string or docs '''
#  Write a Python program to calculate the number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days
# from datetime import date
# fdate=date(2014,7,2)
# ldate=date(2014,7,11)
# difference=ldate-fdate
# print(difference)
# Write a Python program to get the volume of a sphere with radius six.
# radius=6
# volume=4/3*3.14*radius*radius*radius
# print("the volume of the cylinder is ", volume)

