#multi-level inheritance-
#a class is derived from another class, which is itself derived from another class. It forms a chain of inheritance.
class college:
    @staticmethod
    def start():
        print("college starts at 9 ...")
    
    @staticmethod
    def end():
        print("college ends at 4...")

class btech(college):
    def __init__(self,branch,semester):
        self.branch=branch
        self.semester=semester

class name(btech):
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

name1=name("jahnvi",253)
name1.branch="cse"
name1.semester=3
name1.start()
print(name1.name)
print(name1.branch)
print(name1.roll_no)
print(name1.semester)
name1.end()

    
        