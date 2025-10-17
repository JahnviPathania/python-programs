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
#create account class with 2 attributes - balance & account number
#create methods for debit,credit & printing the balance
class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def debit(self,amount):
        self.balance-=amount
        print("rs" , amount , "was debited")
        print("total balance = ", self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("added rs" , amount)
        print("total balance = ", self.get_balance())
    def get_balance(self):
        return self.balance


acc1=Account(10000,12345)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
