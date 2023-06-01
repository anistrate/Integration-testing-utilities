import os
import json
import shutil

def create_recursively(depth:int, path:str) -> None:
    if depth == 0:
        return
   
    for indexSubfolder in range(1, numberOfFolders):
        currentPath:str = GetPath(path, depth, indexSubfolder)
        os.mkdir(currentPath)
        create_recursively(depth-1, currentPath)
    return


def GetPath(path:str, folderDepth:int, index:int) -> str:
    return path+"/"+directory_name+" " + str(folderDepth) + " " + str(index)


def create_folders() -> None:
    os.mkdir(path)

    for index in range(1,numberOfFolders):
        folderPath:str = GetPath(path, folderDepth, index)
        os.mkdir(folderPath)
        create_recursively(folderDepth-1, folderPath)
    return

def delete_folders() -> None:
    deleteConfirmInvalid:bool = True
    while deleteConfirmInvalid:
        print("Are you sure you want to delete the folders at " + path +"?")
        deleteConfirm:str = input("Confirm: Y/N")
        if deleteConfirm == "Y":
            try:
                shutil.rmtree(path)
                print("Folders deleted!")
            except OSError as e:
                print("Error : %s : %s " % (path, e.strerror))
            deleteConfirmInvalid = False
        elif deleteConfirm == "N":
            deleteConfirmInvalid = False
        else:
            print("Invalid command!")
    return

print("Start...")

directory_name:str = "test"
with open('config.json', 'r') as configFile:
    jsonConfig:dict = json.load(configFile)

path:str = jsonConfig['path']
numberOfFolders:int = int(jsonConfig['nrOfFolders'])
numberOfFolders += 1
folderDepth:int = int(jsonConfig['depthOfFolders'])
path += "/"+directory_name

commandIsInvalid:bool = True
while commandIsInvalid:
    print("Select:")
    print("1. Create folders at " + path)
    print("2. Delete Folders at " + path)
    command:str = input("Command: ")
    if command == "1" :
        create_folders()
        commandIsInvalid = False
    elif command == "2" :
        delete_folders()
        commandIsInvalid = False
    else:
        print("Invalid command.")

print("Done. Execution Succesful!")
