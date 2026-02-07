import os
import time
import Logger
import sys
import hashlib

class DuplicateFilesInDirectory:

    filename = "Assignment32_4_%s.log" % time.ctime().replace(":","_").replace(" ","_")

    def __init__(self,directory):
        self.Directory  = directory
    
    def validateDirectory(self):
        if(os.path.exists(self.Directory) and os.path.isdir(self.Directory)):
            return True
        return False
    
    def findAndDeleteDuplicateFiles(self):
        startTime = time.time()
        if(self.validateDirectory()):
            filesScanned = 0
            dupliacateFiles = []
            checkSumList = []
            for folder,__,files in os.walk(self.Directory):
                for file in files:
                    filesScanned += 1
                    filePath = os.path.join(folder,file)
                    hashValue = self.getCheckSum(filePath)
                    if hashValue in checkSumList:
                        dupliacateFiles.append(filePath)
                        self.deleteFile(filePath)
                    else:
                        checkSumList.append(hashValue)
                   
            Logger.headerfooter(DuplicateFilesInDirectory.filename)
            self.writeLog(f"Processed at : {time.ctime()}")
            logData = f'''Total files scanned : {filesScanned} \nTotal duplicate files : {len(dupliacateFiles)} \nDeleted duplicate files are :'''
            for data in dupliacateFiles:
                logData += "\n"+data
            self.writeLog(logData)
            logData = f"Total Time Required to process : {time.time() - startTime} seconds"
            self.writeLog(logData)
            Logger.headerfooter(DuplicateFilesInDirectory.filename)
            return 1
        else:
            return -1
     
    def getCheckSum(self,filePath):
        fobj = open(filePath,"rb")
        data = fobj.read(1024)
        md5Hash = hashlib.md5()
        while(len(data))>0:
            md5Hash.update(data)
            data = fobj.read(1024)
        fobj.close()
        return md5Hash.hexdigest()
                   
    def deleteFile(self,filePath):
        os.remove(filePath)
        

    def writeLog(self,data):
            Logger.writeLog(DuplicateFilesInDirectory.filename,data)




def main():
    """Design automation script which accept directory name and delete all duplicate files from thatdirectory."""
    print(main.__doc__,"\n",("-"*50),"\n\n")
    if len(sys.argv)!=2:
        print("Invalid no of arguments")
        print(f"Usage : {sys.argv[0]} <Directory_Name>")
        return
    
    directory = sys.argv[1]
    dobj = DuplicateFilesInDirectory(directory)
    ret = dobj.findAndDeleteDuplicateFiles()
    if(ret==1):
        print("Script run successfully.")
    elif ret==-1:
        print("Directory does not exists.")



if __name__ == "__main__":
    main()