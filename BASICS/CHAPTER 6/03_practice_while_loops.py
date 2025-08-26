#WAP to print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i=i+1
print("loop ended")
#WAP to print numbers from 100 to 1
i2=100
while i2>=1:
    print(i2)
    i2=i2-1
print("loop ended")
#WAP to print the multiplication table of n number (user input)
x=int(input("enter number :  "))
count=1
while count<=10:
    print(x," x" ,count,"=",x*count)
    count=count+1
print("loop ended")
#WAP to print elemenst of list [1,4,9,45,67,89,98,90]
ls=[1,4,9,45,67,89,98,90]
index=0
while index<=(len(ls)-1):
    print(ls[index])
    index=index+1
#WAP to search a value in the tuple (1,2,9,16,25,36,49,64,81,100)
tuples=(1,2,9,16,25,36,49,64,81,100)
print(tuples)
searching=int(input("enter element you wanna search in the tuple :  "))
index=0
while index<=(len(tuples)-1):

    if tuples[index]==searching:
        print("element found at location ",index)
        break
    else:
        index=index+1
#WAP to find the sum of first n natural numbers 
n=int(input("enter number"))
i3=1
sum=0
while i3<=n:
    sum=sum+i3
    i3=i3+1
print(sum)
    
    