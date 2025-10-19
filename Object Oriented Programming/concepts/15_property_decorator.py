class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        self.percentage=(self.phy+self.chem+self.maths)/3

stu1=student(98,97,96)
print(stu1.percentage)
#here we take a scenario where i have to change marks for phy
stu1.phy=86
print(stu1.phy)#here the marks will be changed but
print(stu1.percentage)#the percentage remains the same

#so to avoid this we do this instead
class student1:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
       # self.percentage=(self.phy+self.chem+self.maths)/3

    @property
    def percentage(self):
            return (self.phy+self.chem+self.maths)/3

    

stu11=student1(98,97,96)
print(stu11.percentage)
stu11.phy=86
print(stu11.phy)
print(stu11.percentage)
