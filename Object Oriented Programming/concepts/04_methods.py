#methods are basically the functions inside the class
#example- strng methods are the methods of thr string class
#example
class Student:
    college="PPSU"

    def __init__(self,name,marks):#constructor
        self.name=name
        self.marks=marks
    
    def hello(self):#METHOD
        print("Hello",self.name)

    def get_marks(self):
        print(self.marks)



s1=Student("karan",97)
s1.hello()
s1.get_marks()
