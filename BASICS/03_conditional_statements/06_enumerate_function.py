#enumerate function-it allows you to loop over a sequence and print the index and value 
#example - if you wanna print index using for loop
ls=[1,2,3,4,5,6,7,8]
index=0
for i in ls:
    print(i)
    if(index==3):
        print("hello")
    index+=1
#here instead of using variable index we can use enumerate
for index1, i in enumerate(ls):
    print(index1,i)
    if(index1==3):
        print(index1,"hello")
