import os
import json


def create_recursively(depth:int, path:str) -> None:
    if depth == 0:
        return
   
    for indexSubfolder in range(1, numberOfFolders+1):
        currentPath:str = GetPath(path, depth, indexSubfolder)
        os.mkdir(currentPath)
        create_recursively(depth-1, currentPath)
    return


def GetPath(path:str, folderDepth:int, index:int) -> str:
    return path+"/"+directory_name+" " + str(folderDepth) + " " + str(index)


def create_folders() -> None:
    with open('config.json', 'r') as configFile:
        jsonConfig:dict = json.load(configFile)


    path:str = jsonConfig['path']
    numberOfFolders:int = jsonConfig['nrOfFolders']
    folderDepth: int = jsonConfig['depthOfFolders']

    directory_name:str = "test"
    path += "/"+directory_name
    os.mkdir(path)

    for index in range(1,numberOfFolders+1):
        folderPath:str = GetPath(path, folderDepth, index)
        os.mkdir(folderPath)
        create_recursively(folderDepth-1, folderPath)
    return




print("Start...")
print("Select:")
print("1. Create folders")
print("2. Delete Folders")


command:str = input("Command: ")


if command == "1" :
    create_folders()
#else if command == "2" :
#    delete_folders()
#else:
 


print("Done. Execution Succesful!")
