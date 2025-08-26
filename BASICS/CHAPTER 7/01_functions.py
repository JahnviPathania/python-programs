#function - block of statement that perform specific task
#syntax
#def func_name(param1,param2,..):
    #some work
    #return val
#to stop redundant coding we use functions
#example-to make function for adding two numbers
def sum(a,b):#here we are defining function
    s=a+b
    print(s)
    return s
sum(2,3)#here we are calling function
#here 2 and 3 are called arguments
#function to print hello
def print_hello():#this function does not return any value
    print("hello im learing python")

print_hello()
#function to calculate avg of 3 numbers
def avg(a,b,c):
    average=(a+b+c)/3
    print(average)
    return average
avg(2,2,2)
#function are of two types - built-in and user defined


#default parameters
#assigning values that are used when no argument is passed
def multiplication(a=1,b=1):
    mul=a*b
    print(mul)
    return mul
multiplication()#uses default value as no argument is passed here

