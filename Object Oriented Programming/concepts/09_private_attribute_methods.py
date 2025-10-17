#private attributes and methods are meant to be used only within the class and are not accessible from outside the class
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass

acc1=Account("12345","abcde")
#here we can access both acc no and acc pass which is a bad practice but acc pass is sensitive info which should not be available to everyone
#hence we  make that attribute private by adding __ infront of it 
class Account1:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

acc11=Account1("12345","abcde")
print(acc11.__acc_pass)