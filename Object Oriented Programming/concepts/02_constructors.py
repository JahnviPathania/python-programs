#constructors-special method in class that gets called automatically when you create a new object
#constructors initialize the objects attributes
#in python we always use __init__(self) for constructors
#example
class Student:
    def __init__(self):#self refers to the object being created 
        print(self)#refers to the address of the object being created
        print("constructor called ")
s1=Student()
print(s1)#see in output that self and s1 has same address
s2=Student()
print(s2)
#constructors are called everytime a new object is created
#now we can pass multiple parameters in the constructors
#example
class Student1:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print("added the info in the database")
ss1=Student1("jahnvi",34)
print(ss1.name)
print(ss1.roll_no)
#if we are saying constructors are always called when object is created why is that the following code will run fine 
#even when there is no constructor
class Car:
    name="redbull racing"
    colour="orange"

c1=Car()
print(c1.colour)
print(c1.name)
