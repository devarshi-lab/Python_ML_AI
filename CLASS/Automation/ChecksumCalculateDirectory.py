import hashlib
import os

def DirectoryWatcher(DirectoryName = "Marvellous"):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    for folder,subfolder,files in os.walk(DirectoryName):
        for file in files:
            checksum = calculateChecksum(os.path.join(folder,file))
            print(f"Filename : {file} \t checksum : {checksum}")

def calculateChecksum(fileName):
    fobj = open(fileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    fobj.close()

    return hobj.hexdigest()


def main():
    DirectoryWatcher()
   

if __name__ == "__main__":
    main()