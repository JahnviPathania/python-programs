#encapsulation-wrapping data and functions into a single unit(object)
class Dog:
    def __init__(self, name, age):
        self.name = name    # Public attribute
        self.age = age      # Public attribute

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

# Usage
my_dog = Dog("Buddy", 3)
my_dog.bark()
my_dog.birthday()
