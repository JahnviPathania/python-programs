#absraction is hiding the implementation details of a class and only showing the essential feature to the user
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started...")
car1=Car()
car1.start()
#HERE when a user starts  the car he will only see that the car is started not how the car was started 
#hence hiding the unneccsary details from user is abstraction

