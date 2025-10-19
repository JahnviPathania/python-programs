class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("the car is started...")

    @staticmethod
    def stop ():
        print("car is stopped...")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

car1=ToyotaCar("innova","electric")
print(car1.type)

