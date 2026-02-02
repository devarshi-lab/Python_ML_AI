import sys
import os 

def removeEmptyFiles(dir = "Marvellous"):
    if((os.path.exists(dir) == False) or (os.path.isdir(dir) == False)):
        print("Directory does not exists")
    scannedFileCounter = 0
    emptyFileCounter = 0
    for folder,subfolders,files in os.walk(dir):
        for file in files:
            print(f"Filename : {os.path.join(folder,file)} \t size : {os.path.getsize(os.path.join(folder,file))}  bytes")
            scannedFileCounter += 1
            if (os.path.getsize(os.path.join(folder,file)) == 0):
                emptyFileCounter += 1
                os.remove(os.path.join(folder,file))
                # print(f"Deleted Filename : {os.path.join(folder,file)}")
    
    border()
    print("-------------- Automation Report -----------------")
    print("Total files scanned : ",scannedFileCounter)
    print("Total empty files found : ",emptyFileCounter)
    border()


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

    border()
    print("--------- Marvellous Directory Automation---------")
    border()

if __name__ == "__main__":
    main()