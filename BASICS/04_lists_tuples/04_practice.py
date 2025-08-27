#WAP to ask user to enter names of their 3 favorite movie & store them in a list
movie1=input("enter your favorie movie")
movie2=input("enter your favorie movie")
movie3=input("enter your favorie movie")
movies=[movie1,movie2,movie3]
print("list of your favorite movies")
print(movies)
#WAP to check if the list contains palindrome
list=[1,2,2,1]
copy=list.copy()
copy.reverse()
if(list==copy):
    print("list is an palindrome")
else:
    print("not a palindrome")
#WAP to count the number of student with grade A from a tuple
tuples=["A","C","D","A","C","D","B","C"]
tuples.sort()
print(tuples)




