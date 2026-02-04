import os
import time
import Logger
import time

class SearchFIleWithExtension:

    filename = "Assignment31_1_%s.log" % time.ctime().replace(":","_").replace(" ","_")

    def __init__(self,directory,extension):
        self.directory  = directory
        self.extension = extension
    
    def validateDirectory(self):
        if(os.path.exists(self.directory) and os.path.isdir(self.directory)):
            return True
        return False
    
    def getFilesWithExtension(self):
        if(self.validateDirectory()):
            self.filecount = 0
            self.filesextcount = 0
            self.fileswithextension = []
            for folders,subfolder,files in os.walk(self.directory):
                for file in files:
                    self.filecount += 1
                    # print(os.path.splitext(file))
                    ext = file.split(".")
                    if len(ext) > 1 :
                        if ext[-1:][0] == self.extension.replace(".",""):
                             self.filesextcount += 1
                             self.fileswithextension.append(file)

            Logger.headerfooter(SearchFIleWithExtension.filename)
            Logger.writeborder(SearchFIleWithExtension.filename)
            logData = f'''Total files scanned : {self.filecount} \nTotal files with {self.extension} extension : {self.filesextcount}\nFile Names : \n{"\n".join(self.fileswithextension)}'''
            self.writeLog(logData)
            Logger.writeborder(SearchFIleWithExtension.filename)
            Logger.headerfooter(SearchFIleWithExtension.filename)
            return 1
        else:
            return -1
        

    def writeLog(self,data):
            Logger.writeLog(SearchFIleWithExtension.filename,data)




def main():
    """1.Design automation script which accept directory name and file extension from user. Display all files with that extension.
Usage : DirectoryFileSearch.py “Demo” “.txt”
Demo is name of directory and .txt is the extension that we want to search."""
    print(main.__doc__,"\n",("-"*50),"\n\n")
    fileName = input("Enter the name of directory : ")
    ext = input("Enter the extension :  ")
    dobj = SearchFIleWithExtension(fileName,ext.replace(".",""))
    ret = dobj.getFilesWithExtension()
    if(ret==1):
        print("Script runsuccessfully.")
    elif ret==-1:
        print("Directory does not exists.")



if __name__ == "__main__":
    main()