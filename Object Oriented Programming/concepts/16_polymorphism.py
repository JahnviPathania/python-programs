#polymorphism : operator overloading
print(1+2)#add
print("jahnvi"+"pathania")#concatenate
#for integers and strings + operator has different meaning
#it it operator overloading
#single operator has different meanings
#we can make our own class and do operator ooverloading
#example 
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newReal,newimg)



num1=complex(1,3)
num1.shownumber()
num2=complex(2,3)
num2.shownumber()
#how to add these two complex numbers
#we can use this method
# num3=num1.add(num2)
# num3.shownumber()
#but we want people to be able to use + directly
#so we use dunder function
#we just add __add__ in the function
num3=num1+num2
num3.shownumber()
