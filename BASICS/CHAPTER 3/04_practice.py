#WAP to check if a number entered by user is odd or even
number=int(input("enter a number :  "))
if(number%2==0):
    print("the number is even")
else:
    print("the number is odd")
#WAP to find the greatest of 3 numbers entered by the user
num1=int(input("enter number 1 :"))
num2=int(input("enter number 2 :"))
num3=int(input("enter number 3: "))
if(num1>num2 and num1>num3):
    print("this it the greatest number",num1)
elif(num2>num1 and num2>num2):
    print("this is the greatest number",num2)
else:
    print("this is the greatest number",num3)
#WAP to check if a number is a multiple of 7 or not
numb=int(input("enter a number :  "))
if(numb%7==0):
    print("the number is a multiple of 7")
else:
    print("the number is not a multiple of 7")