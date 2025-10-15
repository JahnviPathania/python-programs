#seek function are sued to work with file objects and theri positions within a file
#these functions are part of built in io module
#seek function
#moves current position within a file to a specific point 
with open(r"E:\python programs\BASICS\08_IO_files\demo.txt","r") as f:
    #move to the tenth byte in the file
    f.seek(3)
    #read the next five bytes
    data=f.read(5)
    print(data)



