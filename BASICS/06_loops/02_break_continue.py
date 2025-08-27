#break- used to terminate loop when encountered
#example
i=1
while i<=5:
    print(i)
    if(i==3):
        break# the condition in if is true when i=3 hence the loop got terminated
    i=i+1
print("end of loop due to break ")
#continue - terminates execution in the current iteration & continues execution of the loop with the next iteration
i2=1
while i2<=5:
    if(i2==3):
        i2=i2+1
        continue#skips the current iteration
    print(i2)
    i2=i2+1
    
