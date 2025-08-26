#WAP to print the length of a list(list is the parameter)
def print_len(list):
    print(len(list))
    return len(list)
print_len(["apple","mango","peach","kiw","dragonfruit"])
#WAP to print the elements of a list in a single line
def print_elements(list):
    for i in list:
        print(i,end="")
    return i
print_elements(["a","b","c","d","e"])
#WAP to find the factorial of n
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
        
    return result
print(factorial(5))
#WAP to convert usd into inr
def conversion(n):
    conv=n*90
    print(conv)
conversion(50)
#WAP to input a number and check if the number is odd or even andreturn odd or even
def odd_or_even(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")
x=int(input("enter a number : "))
odd_or_even(x)