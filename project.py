from mimetypes import init
from pathlib import Path
import os

import git
#CRUD

def createfolder():
    name = input("Enter your folder name: ")
    p = Path(name)
            #  "D:\P21 File Handling\Superman"
    p.mkdir()

def readfolder():
    p = Path("") #d"/P21 file handlingw
    items = list(p.rglob("*"))
    for i in range(len(items)):
        print(i+1, items[i])

def deletefolder():
    readfolder()
    name = input("Enter folder name to be deleted: ")
    p = Path(name)
    if p.exists():
        p.rmdir()
        print("Folder deleted successfully")
    else:
        print("No folder exists")

def updatefolder():
    oldname = input("Enter folder name: ")
    p = Path(oldname)
    if p.exists():
        new_name = input("Enter new name for folder: ")
        new_p = Path(new_name)
        p.rename(new_p)
        print("Folder renamed")

def createfile():
    readfolder()
    name = input("Enter your file name (with extension): ")
    p = Path(name)
    if not p.exists():
        with open(name,'w') as fs:
            data = input("Enter your data")
            fs.write(data)
            print("File created successfully")

def readfile():
    readfolder()
    name = input("Enter your file name (with extension): ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(name,'r') as fs:
            print(fs.read())
    
def deletefile():
    readfolder()
    name = input("Enter your file name (with extension): ")
    p = Path(name)
    if p.exists() and p.is_file():    
        os.remove(p)
        print("File deleted successfully")

def updatefile():
    name = input("Enter the file name with extension")
    p = Path(name)
    if p.exists() and p.is_file():
        print("Press 1 for renaming  the file:")
        print("Press 2 for appending the data in file")
        print("Press 3 for overwriting data")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_name = input("Enter new name for file")
            new_p = Path(new_name)
            p.rename(new_p)
            print("File name changed successfully")
        
        if choice == 2:
            readfile()
            with open(name,'a') as fs:
                data = input("Enter your data: ")
                fs.write(data)
        
        if choice == 3:
            with open(name,'w') as fs:
                data = input("Enter your data: ")
                fs.write(data)

while True:
    print("Press 1 for creating folder")
    print("Press 2 for reading folder")
    print("Press 3 for deleting folder")
    print("Press 4 for Updating folder")
    print("Press 5 for creating file")
    print("Press 6 for reading file")
    print("Press 7 for deleting file")
    print("Press 8 for updating file")
    print("Press 0 for exiting..")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        createfolder()
    if choice == 2:
        readfolder()
    if choice == 3:
        deletefolder()
    if choice == 4:
        updatefolder()
    if choice == 5:
        createfile()
    if choice == 6:
        readfile()
    if choice == 7:
        deletefile()
    if choice == 8:
        updatefile()
    if choice == 0:
        break



