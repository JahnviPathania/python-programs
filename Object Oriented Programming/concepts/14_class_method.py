class person:
    name="anonymous"

    def changename(self,name):
        self.name=name

p1=person()
p1.changename("rahul kumar")#this changes the name for object but in class name still remains anonymous
print(p1.name)
print(person.name)
#hence instead we use
class person1:
    name="anonymous"
    @classmethod
    def changename(cls,name):#here cls is not self but refers to class
        cls.name=name

p1=person1()
p1.changename("rahul kumar")#this changes the name for object but in class name still remains anonymous
print(p1.name)
print(person1.name) 