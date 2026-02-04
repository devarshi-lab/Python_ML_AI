import os
import time
import Logger
import sys

filename = "Assignment31_2_%s.log" % time.ctime().replace(":","_").replace(" ","_")

def validateDirectory(directory):
    if(os.path.exists(directory) and os.path.isdir(directory)):
        return True
    return False

def renameFileExtension(directory,sourceExtension,renameExtension):
    if(validateDirectory(directory)):
        filecount = 0
        filesextcount = 0
        fileswithextension = []
        for folder,_,files in os.walk(directory):
            for file in files:
                filecount += 1
                ext = os.path.splitext(file)
                if len(ext) > 1 :
                    if ext[1].replace(".","") == sourceExtension:
                            filesextcount += 1
                            os.rename(os.path.join(folder,file),os.path.join(folder,ext[0]+"."+renameExtension))
                            fileswithextension.append(ext[0]+"."+renameExtension)

        Logger.headerfooter(filename)
        Logger.writeborder(filename)
        writeLog(f"Processed at : {time.ctime()}")
        logData = f'''Total files scanned : {filecount} \nTotal files with {sourceExtension} extension : {filesextcount} \nRenamed File Names : \n{"\n".join(fileswithextension)}'''
        writeLog(logData)
        Logger.writeborder(filename)
        Logger.headerfooter(filename)
        return 1
    else:
        return -1

def writeLog(data):
        Logger.writeLog(filename,data)




def main():
    """Design automation script which accept directory name and two file extensions from user.
        Rename all files with first file extension with the second file extenntion.
        Usage : DirectoryRename.py “Demo” “.txt” “.doc”"""
    print(main.__doc__,"\n",("-"*50),"\n\n")
    if(len(sys.argv)!=4):
        print("Invalid no. of arguments")
        print(f"Expected : {sys.argv[0]} <DirectoryName>  <sourceExtension> <renameExtension> ")
        return
    
    directory = sys.argv[1]
    sourceExtension = sys.argv[2]
    renameExtension = sys.argv[3]
    ret = renameFileExtension(directory,sourceExtension.replace(".",""),renameExtension.replace(".",""))
    if(ret==1):
        print("Script run successfully.")
    elif ret==-1:
        print("Directory does not exists.")



if __name__ == "__main__":
    main()