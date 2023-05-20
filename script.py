import os, shutil

def Menue():
    print("AI Homework")
    print('1 - Check if file exists')
    print('2 - Check file type | file or directory')
    print('3 - Create a file')
    print('4 - Print file data')
    print('5 - Move a file')
    print('6 - Delete a file')
    print('7 - Exit')
    taskNO = InputTaskNo()
    if taskNO == 1:
        if  FileExists():
            print  ("File exists")
        else: print("File not exists")
        print("Press enter to continue...")
    
    elif taskNO == 2:
        print(CheckLocationType())
        Menue()
    elif taskNO ==3:
        CreateFile()
        Menue()
    elif taskNO == 4:
        PrintFileData()
        Menue()
    elif taskNO == 5:
        MoveFile()
        Menue()
    elif taskNO == 6:
        DeleteFile()
        Menue()
    elif taskNO ==7:
        exit()


def InputTaskNo():
    while True:
        try:
            day_number = int(input("Enter the number of task: "))
            if 1 <= day_number <= 7:
                return day_number
            else:
                print("Invalid input. Please enter a number from 1 to 7.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def FileExists():
    filePath = input("Enter the file name: ")
    return os.path.exists(filePath)

def CreateFile():
    filePath = input("Enter the file name: ")
    if not FileExists(filePath):
        with open(filePath, 'w') as file:
            pass
        print("File created successfully.")
    else:
        print("File already exists.")

def CheckLocationType():
    path = input("Enter the file name: ")
    if os.path.isfile(path):
        return "File"
    elif os.path.isdir(path):
        return "Directory"
    else:
        return "Invalid path"

def PrintFileData():
    filePath = input("Enter the file name: ")
    try:
        with open(filePath, 'r') as file:
            for line in file:
                print(line.rstrip())
    except FileNotFoundError:
        print("File not found.")
    except IOError:
        print("An error occurred while reading the file.")

def MoveFile():
    sourcePath = input("Enter the file name: ")
    destinationPath = input("Enter the file name: ")
    try:
        shutil.move(sourcePath, destinationPath)
        print("File moved successfully.")
    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission denied. Unable to move the file.")
    except shutil.Error as e:
        print(f"An error occurred while moving the file: {e}")

def DeleteFile():
    filePath = input("Enter the file name: ")
    try:
        os.remove(filePath)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied. Unable to delete the file.")
    except OSError as e:
        print(f"An error occurred while deleting the file: {e}")


Menue()