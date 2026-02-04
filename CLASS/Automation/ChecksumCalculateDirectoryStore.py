import hashlib
import os



def findDuplicate(DirectoryName = "Marvellous"):
    Ret = False
    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if(Ret == False):
        print("It is not a directory")
        return
    Duplicate = {}

    for folder,subfolder,files in os.walk(DirectoryName):
        for file in files:
            file = os.path.join(folder,file)
            checksum = calculateChecksum(file)
            if checksum in Duplicate:
                Duplicate[checksum].append(file)
            else:
                Duplicate[checksum] = [file]
    return Duplicate

def DisplayResult(MyDict):
    print(MyDict)
    Result = list(filter((lambda x : len(x)>1),MyDict.values()))
    print(Result)
    count = 0
    for value in Result:
        for subValue in value:
            count += 1
            print(subValue)
        print("Value of count is :",count)
        count = 0

def DeleteDuplicate(path = "Marvellous"):
    MyDict = findDuplicate(path)
    Result = list(filter((lambda x : len(x)>1),MyDict.values()))
    count = 0
    cnt = 0
    for value in Result:
        for subValue in value:
            count += 1
            if(count > 1):
                print("Deleted file : ",subValue)
                os.remove(subValue)
                cnt = cnt + 1
        count = 0
    print("Total deleted files  : ",cnt)


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
    Ret = DeleteDuplicate()
    # DisplayResult(Ret)
   

if __name__ == "__main__":
    main()