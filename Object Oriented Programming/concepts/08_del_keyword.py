#del keyword is used to delete an attribute of object or the object as whole
#example
class Student:
    def __init__(self,name):
        self.name=name

s1= Student("jahnvi")
print(s1.name)
del s1
print(s1.name)#will throw error because s1 is deleted 