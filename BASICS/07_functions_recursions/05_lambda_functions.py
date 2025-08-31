#lambda functions is a small anonymous functions without a name
#syntax
#lambda arguments:expressions
#example-for finding cube
cube=lambda x:x*x*x
print(cube(5))
#you can give multiple arguments but its not preferable 
#we use it for one line functions  
#we use lambda functions when we have to use a function inside a function
#example
def apply(fx,value):
    return 6+fx(value)
print(apply(cube,2))
#we can also directly use lambda function in print
print(apply(lambda x:x*x,2))
