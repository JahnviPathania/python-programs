#inheritance- when one class derives the properties & methods of another class
#parent class - class whose properties are being derived
#child class- class who derives the properties of parent classg
#inheritance can be of 3 types 
#1. single level 
#2. multi level
#3. multiple inheritance 
# example - single level inheritance
class Car:
    colour="black"
    @staticmethod
    def start():
        print("the car is started...")

    @staticmethod
    def stop ():
        print("car is stopped...")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
        
car1=ToyotaCar("fortuner")
car2=ToyotaCar("pirus")


print(car1.name)
print(car1.start())
