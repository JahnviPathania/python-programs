#store following word meaning in python dictionary
#table:"a piece of furniture","list of facts and figures
#cat:"a small animal"
meanings={"table":["a piece of furniture","list of facts and figures"],"cat":"a small animal"}
print(meanings)
#you are given a list of subjects for students assume one classroom is required for 1 subject how mamny classroom are needed by all students
#python,java,cpp,python,javascript,java,python,java,cpp,c
subjects={"python","java","cpp","python","javascript","java","cpp","c"}
print(subjects)
print("number of classroom needed is   ",end="")
print(len(subjects))
#WAP to enter marks of 3 subjects from user and store them in dictionary start with an empty dict & add one by one use subject as key and marks as value
empt_dict={}
subject1=input("enter subject :  ")
marks1=int(input("enter marks :  "))
subject2=input("enter subject :  ")
marks2=int(input("enter marks :  "))
subject3=input("enter subject :  ")
marks3=int(input("enter marks :  "))
empt_dict[subject1]=marks1
empt_dict[subject2]=marks2
empt_dict[subject3]=marks3
print(empt_dict)
#figure out a way to store 9 and 9.0 as seperate values in set
sets={int(9),str(9.0)}
print(sets)
