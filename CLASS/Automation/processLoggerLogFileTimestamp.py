import time
import psutil
import sys
import os

def createLog(foldername):
    if not os.path.exists(foldername) or not os.path.isdir(foldername):
        os.mkdir(foldername)
        print("Directory for log file gets created")
    
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(foldername,"Marvellous_%s.log" %timestamp)
    fobj = open(FileName,"w")
        


def border():
    print("-"*50)

def main():
    
    border()
    print("----- Marvellous Platform Surviellance System ----")
    border()
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to :")
            print("1. Create automatic logs")
            print("2. Executes periodically")
            print("3. Sends mail with the log")
            print("4. Store information about processes")
            print("5. store information about CPU")
            print("6. Store information about RAM usage")
            print("7. Store information about secondary storage")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print(f"{sys.argv[0]} <TimeInterval> <LogDirectoryName>")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("LogDirectoryName : Name of directory to create auto logs")

        else:
            print("Invalid number of command line argumnets")
            print("Please use --h or --u to get more details")

    elif(len(sys.argv)==3):
        interval = sys.argv[1]
        LogDirectory = sys.argv[2]
        createLog(LogDirectory)

    else:
        print("Invalid number of command line argumnets")
        print("Please use --h or --u to get more details")

    border()
    print("--------- Tahnk You for using our script ---------")
    border()

if __name__ == "__main__":
    main()