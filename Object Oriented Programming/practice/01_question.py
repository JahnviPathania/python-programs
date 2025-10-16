# create student class that takes name and marks of 3 subjects as agruments in constructors 
#then create a method to print the average
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        sum=0
        for i in self.marks:
            sum=sum+i
        print("your average score is : ", sum/3)

s1=Student("jahnvi",[97,97,98])
s1.average()