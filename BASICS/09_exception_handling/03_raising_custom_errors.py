#sometimes in python we need to raise some  custom errors to stop a program 
#for this we use raise function
a=int(input("enter any value between 5 and 9: "))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")
#we raise custom error because it helps us know exaclty where a problem arises
