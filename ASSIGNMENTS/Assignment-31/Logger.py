
import os 

def writeLog(file,data):
        fobj = open(file,"a" if os.path.exists(file) else "w")
        fobj.write(data+"\n")

def writeborder(file):
        fobj = open(file,"a" if os.path.exists(file) else "w")
        fobj.write("-"*50+"\n")

def headerfooter(file):
    writeborder(file)
    writeLog(file,"------------ Python Automation Script ------------")
    writeborder(file)



