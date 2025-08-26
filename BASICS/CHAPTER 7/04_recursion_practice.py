#return factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        fact=n*factorial(n-1)
        return fact
print(factorial(5))
#write a recursive function to calculate the sum of first natural numbers
def sum(n):
    if(n==1):
        return 1
    else:
        s=n+sum(n-1)
        return s
print(sum(5))
#write a recursive function to print all elemenst in a list
def print_elements(list,index):
    if(index==len(list)):
        return
    print(list[index])
    print_elements(list,index+1)

list=[1,2,3,4,5]
print_elements(list,0)
