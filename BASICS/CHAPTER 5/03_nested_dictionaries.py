#nested dictionaries
student={"name":"ashish","subject":["c programming","python programming",'java programming'],"marks":{"c programming":78,"python programming":89,"java programming":78},"age":23}
print(student)#here marks is nested dictionaries as it is under student dictionary
#accessing elements from nested dictionary
print(student["marks"]["python programming"])
