import time
import sys
import os
import schedule

def writeToFile(fileObject,data):
    fileObject.write(data+"\n")

def fun():
    pass

def borderFile():
    return "-"*50

def border():
    print("-"*50)

def main():
    border()
    print("--------- Marvellous Data Schield System ---------")
    border()
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This script is used to :")
            print("1. Takes auto backup at given time")
            print("2. Backup only new and updated files")
            print("3. Create and archive of the backup periodically")
            
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the automation script as")
            print(f"{sys.argv[0]} <TimeInterval> <SourceDirectory>")
            print("TimeInterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory of which we have to take backup")

        else:
            print("Invalid number of command line argumnets")
            print("Please use --h or --u to get more details")

    elif(len(sys.argv)==3):
        interval = sys.argv[1]
        SourceDirectory = sys.argv[2]
        schedule.every(int(interval)).minutes.do(fun,SourceDirectory)

        print("Data Shield System started successfully")
        print("Time Interval (minutes) : ",interval)
        print("Press Ctrl + C to stop the execution")
        border()

        # wait till abort
        # (LogDirectory)
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line argumnets")
        print("Please use --h or --u to get more details")

    border()
    print("--------- Thank You for using our script ---------")
    border()

if __name__ == "__main__":
    main()