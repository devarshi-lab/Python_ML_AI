import sys
import os 

def removeEmptyFiles(dir = "Marvellous"):
    if((os.path.exists(dir) == False) or (os.path.isdir(dir) == False)):
        print("Directory does not exists")

    for folder,subfolders,files in os.walk(dir):
        for file in files:
            if (os.path.getsize(os.path.join(folder,file)) == 0):
                os.remove(os.path.join(folder,file))
                print(f"Deleted Filename : {os.path.join(folder,file)}")


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
    
    if(sys.argv[1]=="/"):
        print("Not allowed")
        return
    
    directory = sys.argv[1]
    removeEmptyFiles(directory)


if __name__ == "__main__":
    main()