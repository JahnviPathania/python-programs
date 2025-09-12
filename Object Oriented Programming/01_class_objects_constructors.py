#object oriented programming - we introduce the concept of classes and objects
#we work around objects
#class - it is like a blueprint for creating objects. it defines the properties and methoods of an object
#objects-it is an instance of class it contains its own data and methods
#example- a class names person that contains properties such as name and age 
#oop includes topic like encapsulation,inheritance,polymorphism etc
#how to create class - example
class person:
    name="jahnvi"
    occupation="data science"
    age=19
    #we can also add methods
    def info(self):
        print(f"{self.name} is a {self.occupation}")#here self reference to the current instance of class

#print name
a=person()
print(a.name)
#change name
a.name="ashish"
print(a.name)
#print info
a.info()
#constructor - special method in class used to create and initialize an object of a class
class person1:
    def __init__(self,n,o):
        print("this is a constructor")
        self.name = n 
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=person1("jahnvi","data scientist")
b=person1("ashish","hr")
a.info()
b.info()
