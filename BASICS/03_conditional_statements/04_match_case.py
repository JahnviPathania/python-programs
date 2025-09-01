#match-case 
x=int(input("enter a number"))
#varibale to match
match x:
    case 0:# if x is zero 
        print("x is zero")
    case 1:#if x is 1
        print("x is 1")
    case 2:#if x is 2
          print("x is 2")
    case 3:
        print("x is 3")
    case 4:
        print("x is 4")
# we can also use if coditions in case
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)