import os
import time
import Logger
import time
import shutil

class copyFilesFromDirectoryToAnother:

    filename = "Assignment31_3_%s.log" % time.ctime().replace(":","_").replace(" ","_")

    def __init__(self,srcDir,destDir):
        self.srcDir  = srcDir
        self.destDir = destDir
    
    def validateDirectory(self):
        if(os.path.exists(self.srcDir) and os.path.isdir(self.srcDir)):
            return True
        return False
    
    def createDirectory(self):
       os.mkdir(self.destDir)
        
    
    def copyFiles(self):
        if(self.validateDirectory()):
            self.filecount = 0
            self.filesextcount = 0
            self.fileswithextension = []
            files = list(os.walk(self.srcDir))[0][2]
            self.createDirectory()
            for file in files:
                shutil.copyfile(self.srcDir+"\\"+file,self.destDir+"\\"+file)

            # Logger.headerfooter(copyFilesFromDirectoryToAnother.filename)
            # Logger.writeborder(copyFilesFromDirectoryToAnother.filename)
            # logData = f'''Total files scanned : {self.filecount} \nTotal files with {self.extension} extension : {self.filesextcount}\nFile Names : \n{"\n".join(self.fileswithextension)}'''
            # self.writeLog(logData)
            # Logger.writeborder(copyFilesFromDirectoryToAnother.filename)
            # Logger.headerfooter(copyFilesFromDirectoryToAnother.filename)
            return 1
        else:
            return -1
        

    def writeLog(self,data):
            Logger.writeLog(copyFilesFromDirectoryToAnother.filename,data)




def main():
    """Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.."""
    print(main.__doc__,"\n",("-"*50),"\n\n")
    srcDir = input("Enter the name of source directory : ")
    destDir = input("Enter the destination directory :  :  ")
    dobj = copyFilesFromDirectoryToAnother(srcDir,destDir)
    ret = dobj.copyFiles()
    if(ret==1):
        print("Script runsuccessfully.")
    elif ret==-1:
        print("Directory does not exists.")



if __name__ == "__main__":
    main()