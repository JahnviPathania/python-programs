#recursion- when function calls itself repeatedly
#everything that you can do with loops you can do the same thing with recursion
#recursive function
def show(n):
    if(n==0):#base case - condition for stopping recursion
        return
    print(n)
    show(n-1)#function calling itself
show(5)



