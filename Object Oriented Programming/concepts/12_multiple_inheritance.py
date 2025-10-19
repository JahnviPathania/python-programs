class A:
    varA="welcome to class A"

class B:
    varB="WELCOME TO CLASS B"

class C(A,B):
    varC="welcome to class c"

c1=C()
print(c1.varC)
print(c1.varA)
print(c1.varB)