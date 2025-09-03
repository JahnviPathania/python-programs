#finally keyword - the block of code inside the finally keyword is executed no matter what is in the try except method
try:
    l=[1,2,3,4,5]
    i=int(input("enter a index: "))
    print(l[i])
except:
    print("some error occured")
finally:
    print("i am always executed")
    