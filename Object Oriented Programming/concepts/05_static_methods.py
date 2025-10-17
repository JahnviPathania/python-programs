#static methods - they dont use self parameter
#they work on the class level
#example
class Student:

    def __init__(self,name,marks):#constructor
        self.name=name
        self.marks=marks
    
    @staticmethod #decorator- allows us to wrap another function to extend its behaviour of the wrapped function without permanently modifying it
# we need to write @staticmethod in order to make a function static
    def hello():
        print("hello")

    def get_marks(self):
        print(self.marks)


s1= Student("jahnvi",97)
print(s1.hello())

