import sys
import os 
import time

def removeEmptyFiles(dir = "Marvellous"):
    logfilename = "Marvellous_%s.log" %(time.ctime().replace(":","_").replace(" ","_"))
    # logfilename = "Marvellous_" + time.ctime().replace(":","_").replace(" ","_") + ".log"
    fobj = open(logfilename,"w")
    fobj.write(border()+"\n")
    fobj.write("This is a log file created by marvellous automation\n")
    fobj.write("This is a Directory Cleaner Script\n")
    fobj.write(border()+"\n")

    if((os.path.exists(dir) == False) or (os.path.isdir(dir) == False)):
        print("Directory does not exists")
        return
    
    scannedFileCounter = 0
    emptyFileCounter = 0
    for folder,subfolders,files in os.walk(dir):
        for file in files:
            # print(f"Filename : {os.path.join(folder,file)} \t size : {os.path.getsize(os.path.join(folder,file))}  bytes")
            scannedFileCounter += 1
            if (os.path.getsize(os.path.join(folder,file)) == 0):
                emptyFileCounter += 1
                os.remove(os.path.join(folder,file))
                # print(f"Deleted Filename : {os.path.join(folder,file)}")
    
    # fobj.write(border()+"\n")
    fobj.write("-------------- Automation Report -----------------\n")
    fobj.write("Total files scanned : "+str(scannedFileCounter)+"\n")
    fobj.write("Total empty files found : "+str(emptyFileCounter)+"\n")
    fobj.write("This log file is created at - "+time.ctime()+"\n")
    fobj.write(border()+"\n")



def border():
    return "-"*50


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