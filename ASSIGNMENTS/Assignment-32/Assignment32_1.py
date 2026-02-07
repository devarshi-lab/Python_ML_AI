import os
import time
import Logger
import sys
import hashlib

class checkSumOfFilesInDirectory:

    filename = "Assignment32_1_%s.log" % time.ctime().replace(":","_").replace(" ","_")

    def __init__(self,directory):
        self.Directory  = directory
    
    def validateDirectory(self):
        if(os.path.exists(self.Directory) and os.path.isdir(self.Directory)):
            return True
        return False

    def getCheckSum(self):
        if(self.validateDirectory()):
            filesScanned = 0
            CheckSum = []
            for folder,__,files in os.walk(self.Directory):
                for file in files:
                    filesScanned += 1
                    filePath = os.path.join(folder,file)
                    fobj = open(filePath,"rb")
                    data = fobj.read(1024)
                    md5Hash = hashlib.md5()
                    while(len(data))>0:
                       md5Hash.update(data)
                       data = fobj.read(1024)
                    CheckSum.append(f"File Name : {filePath} | Checksum : {md5Hash.hexdigest()}")
                   
            Logger.headerfooter(checkSumOfFilesInDirectory.filename)
            self.writeLog(f"Processed at : {time.ctime()}")
            logData = f'''Total files scanned : {filesScanned}'''
            for data in CheckSum:
                logData += "\n"+data
            self.writeLog(logData)
            Logger.headerfooter(checkSumOfFilesInDirectory.filename)
            return 1
        else:
            return -1
        

    def writeLog(self,data):
            Logger.writeLog(checkSumOfFilesInDirectory.filename,data)




def main():
    """1.Design automation script which accept directory name and display checksum of all files."""
    print(main.__doc__,"\n",("-"*50),"\n\n")
    if len(sys.argv)!=2:
        print("Invalid no of arguments")
        print(f"Usage : {sys.argv[0]} <Directory_Name>")
        return
    
    directory = sys.argv[1]
    dobj = checkSumOfFilesInDirectory(directory)
    ret = dobj.getCheckSum()
    if(ret==1):
        print("Script run successfully.")
    elif ret==-1:
        print("Directory does not exists.")



if __name__ == "__main__":
    main()