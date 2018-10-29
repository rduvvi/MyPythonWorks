# Python COPY File using shutil.copy(), shutil.copystat()

import os
import shutil
import time
import datetime
from os import path
from shutil import make_archive
def main():
    if path.exists("test.txt"):
        src=path.realpath("test.txt") # get path to the file in the current directory
        print(src)
        head,tail=path.split(src) # separate the path from filter
        print("Path :"+head)
        print("File :"+tail)
        # Lets make a backup copy by appending "bak" to the name
        dst=src+".bak"
        shutil.copy(src,dst) # create a copy file with new name
        # copy over the permission,modification
        shutil.copystat(src,dst)
        shutil.make_archive("test archive", "zip", head) # Python ZIP file with Example
        t=time.ctime(path.getmtime("test.txt.bak"))
        print(t)
        print(datetime.datetime.fromtimestamp(path.getmtime("test.txt")))
        os.rename("test.txt.bak1","test.txt.bak2")


if __name__=="__main__":
    main()