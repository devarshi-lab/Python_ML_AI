import os
import time
import Logger
import sys
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
       if not os.path.exists(self.destDir):
        os.mkdir(self.destDir)
        
    
    def copyFiles(self):
        if(self.validateDirectory()):
            self.filecount = 0
            self.filesextcount = 0
            self.fileswithextension = []
            files = list(os.walk(self.srcDir))[0][2]
            self.createDirectory()
            # Logic 1
            for file in files:
                file1 = os.path.join(self.srcDir,file)
                file2 = os.path.join(self.destDir,file)
                shutil.copyfile(file1,file2)                   # copyfile() → file only
                # shutil.copy(file1,self.destDir)                # copy() → file + permission also destination can be directory
                # shutil.copy2(file1,self.destDir)               # copy2() → file + permission + time also destination can be directory

            # Logic 2
            # for file in (os.listdir(self.srcDir)):
            #     file1 = os.path.join(self.srcDir,file)
            #     file2 = os.path.join(self.destDir,file)
            #     if(os.path.isfile(file1)):
            #         shutil.copyfile(file1,file2)
            Logger.headerfooter(copyFilesFromDirectoryToAnother.filename)
            self.writeLog(f"Processed at : {time.ctime()}")
            logData = f'''Total files scanned : {len(files)} \nTotal files copied : {len(files)}\nCopied at : {os.path.abspath(self.destDir)}'''
            self.writeLog(logData)
            Logger.headerfooter(copyFilesFromDirectoryToAnother.filename)
            return 1
        else:
            return -1
        

    def writeLog(self,data):
            Logger.writeLog(copyFilesFromDirectoryToAnother.filename,data)




def main():
    """Design automation script which accept two directory names. Copy all files from first directory
into second directory. Second directory should be created at run time.."""
    print(main.__doc__,"\n",("-"*50),"\n\n")
    if len(sys.argv)!=3:
        print("Invalid no of arguments")
        print(f"Usage : {sys.argv[0]} <Source_Directory> <Destination_Directory> ")
        return
    
    srcDir = sys.argv[1]
    destDir = sys.argv[2]
    dobj = copyFilesFromDirectoryToAnother(srcDir,destDir)
    ret = dobj.copyFiles()
    if(ret==1):
        print("Script run successfully.")
    elif ret==-1:
        print("Directory does not exists.")



if __name__ == "__main__":
    main()