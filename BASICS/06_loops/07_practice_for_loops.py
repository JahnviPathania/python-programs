#WAP to print the elements of the following list using a loop
#ls=[1,2,9,16,25,36,49,64,81,100]
ls=[1,2,9,16,25,36,49,64,81,100]
for i in ls:
    print(i)
#WAP to search for number in the above list
print(ls)
searching=int(input("enter the element you wann search :  "))
index=0
for i in ls:
    if(i==searching):
        print("FOUND at index",index)
        break
    index=index+1

    
