from zipfile import ZipFile
from os import path
def main():
    if path.exists("test.txt"):
        src=path.realpath("test.txt")

with ZipFile("testguru.zip","w") as newzip:
    newzip.write("test.txt")
    newzip.write("test.txt.bak2")

if __name__ == '__main__':
 main()