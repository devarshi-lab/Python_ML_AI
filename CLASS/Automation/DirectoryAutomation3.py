import sys
import os 

def getSizeOfFilesInDirectory(dir = "Marvellous"):
    if((os.path.exists(dir) == False) or (os.path.isdir(dir) == False)):
        print("Directory does not exists")

    for folder,subfolders,files in os.walk(dir):
        for file in files:
            print(f"Filename : {os.path.join(folder,file)} \t size : {os.path.getsize(os.path.join(folder,file))}  bytes")

def border():
    print("-"*50)

def main():
    border()
    print("--------- Marvellous Directory Automation---------")
    border()

    if(len(sys.argv)!=2):
        print("Invalid Input Parameter")
        print(f"Expected : {sys.argv[0]} <Directoryname>")
        return
    
    directory = sys.argv[1]
    getSizeOfFilesInDirectory(directory)


if __name__ == "__main__":
    main()