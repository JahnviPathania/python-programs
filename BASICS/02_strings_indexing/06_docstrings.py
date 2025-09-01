#docstings are the string literal that appear after the defination of function,method,classor module
#example
def square(n):
    '''take in a number n and returns the square of n'''
    print(n**2)
print(5)
#difference between docstring and comments
print(square.__doc__)