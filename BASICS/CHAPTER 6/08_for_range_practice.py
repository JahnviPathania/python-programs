#WAP to print numbers from 1 to 100
for i in range(1,101):
    print(i)
    #WAP to print numbers from 100 to 1
    for i in range(100,0,-1):
        print(i)
#WAP print the multiplication table of a number n
i=int(input("enter a number : "))
for i in range(1,11):
    print(i*i)
#WAP to find the factorial of first n natural numbers 
i2=int(input("enter a number "))
fact=1
for i in range(1,i2+1):
    fact=fact*i
   
print(fact)