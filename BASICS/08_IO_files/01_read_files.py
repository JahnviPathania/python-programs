#python can be used to perform operations like read and write on files
# files are of two types - text files and binary files 
#how to open a file
f=open(r"E:\python programs\BASICS\08_IO_files\demo.txt","r")# here we directly write the file name because file is in same folder but if it is not in same folder you have to give the address of files
#in above we use r infront to show the raw string because python uses \ as escape sequence so it produces error
#how to read from a file
data=f.read()
print(data) 
#how to close file
f.close()#make sure to always close the file after use
# Common modes:
# 'r'  → read (file must exist)
# 'w'  → write (overwrites if file exists, creates if not)
# 'a'  → append (adds to end of file)
# 'x'  → create (error if file exists)
# 'b'  → binary mode (use with 'r', 'w', etc.)
# 't'  → text mode (default)
# '+'  → read and write combined (e.g., 'r+', 'w+')
#to read line by line
f1=open(r"E:\python programs\BASICS\08_IO_files\demo.txt","r")
line1=f1.readline(1)