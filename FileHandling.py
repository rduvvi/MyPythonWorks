# Python File Handling: Create, Open, Append, Read, Write
import os.path
import pathlib
from os import path
def main():
    print("File exist :"+str(path.exists('carreer.txt')))
    print("Is it File? "+str(path.isfile("test.tx")))
    print("Is it File? "+str(path.isfile('myDirectory')))
    print("Is it Directory? " + str(path.isdir('myDirectory')))
    file=pathlib.Path("test.txt")
    print("Path of the file :"+str(file))
    if file.exists():
        print("File exists")
    else:
       f=open("test.txt","w+") # open file for write and create if does not exist
       for i in range(10): # write some date to a file and line numbers
        f.write("This is line %d \r\n" %(i+1))
    # close file when done
    f=open("test.txt","a+")
    for i in range(2):
        f.write("Appended lines %d \r\n"%(i+1))
    f.close()
def readFile():
    f=open("test.txt","r")
    if f.mode=="r":
        content=f.read()
        print(content)

def readFilelinebyline():
    f=open("test.txt","r")
    f1=f.readlines()
    for x in f1:
        print(x)


if __name__=="__main__":
    main()
   # readFile()
    #readFilelinebyline()