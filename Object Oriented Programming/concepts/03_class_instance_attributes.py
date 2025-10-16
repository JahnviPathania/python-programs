#class and instance attributes 
#example to understand the concept
class Student:
    college="PPSU"
    def __init__(self,name):
        self.name=name
        print("college is PPSU")
s1=Student("jahnvi")
print(s1.name)
s2=Student("karan")
print(s2.name)

