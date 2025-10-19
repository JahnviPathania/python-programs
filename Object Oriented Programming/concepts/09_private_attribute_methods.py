#private attributes and methods are meant to be used only within the class and are not accessible from outside the class
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass

acc1=Account("12345","abcde")
print(acc1.acc_pass)#anyone can access the password
#here we can access both acc no and acc pass which is a bad practice but acc pass is sensitive info which should not be available to everyone
#hence we  make that attribute private by adding __ infront of it 
class Account1:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass#making it private

acc11=Account1("12345","abcde")
print(acc11.__acc_pass) #will show that it has no attribute hence now the pass is private
#private method
class Hello:
    def __init__(self, name):
        self.name = name

    def greet(self):
        # Public method that uses the private method
        self.__say_hello()

    def __say_hello(self):
        # Private method (notice the double underscore)
        print(f"Hello, {self.name}!")

# Usage
h = Hello("Jahnvi")
h.greet()           # calls the private method internally

# h.__say_hello()   #   Can't access private method directly