#if condition in another if condition is called nesting
age=23
if(age<=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("can drive")