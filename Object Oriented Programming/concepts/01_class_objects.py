#to map real world scenarios we use object 
#class- blueprint for creating objects
#how to create class 
class Student:
    name="karan"#constant name
#we cant use class direclty so we make an object of the class
#object - instance of class
s1=Student()
print(s1)#will point at the address of the object 
print(s1.name)#will return the name
#example 1
class Car:
    color="blue"
    model="safari"
c1=Car()
print(c1.color)
print(c1.model)
#constructors- all classes have _init_() is always executed  when the object is being initiated
class Student1:
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in database")
s1=Student1("karan")#here the constructor will be executed
print(s1.name)