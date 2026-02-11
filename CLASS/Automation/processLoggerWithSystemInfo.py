import time
import psutil
import sys
import os
import schedule

def writeToFile(fileObject,data):
    fileObject.write(data+"\n")

def createLog(foldername):
    if not os.path.exists(foldername) or not os.path.isdir(foldername):
        os.mkdir(foldername)
    
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(foldername,"Marvellous_%s.log" %timestamp)
    fobj = open(FileName,"w")
    print("Log file gets created with name : ",FileName)
    writeToFile(fobj,borderFile())
    writeToFile(fobj,"----- Marvellous Platform Surviellance System ----")
    writeToFile(fobj,"Log created at : "+(time.ctime()))
    writeToFile(fobj,borderFile()+"\n")
    writeToFile(fobj,"------------------ System Report -----------------")

    writeToFile(fobj,"CPU Usage : %s %%" %psutil.cpu_percent())
    writeToFile(fobj,borderFile())
    mem = psutil.virtual_memory()
    writeToFile(fobj,"RAM Usage : %s %%" %mem.percent)
    writeToFile(fobj,borderFile())
    writeToFile(fobj,"Disk Usage Report")

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            writeToFile(fobj,"%s -> %s %%" %(part.mountpoint,usage.percent))
        except:
            pass

    writeToFile(fobj,borderFile())
    net = psutil.net_io_counters()
    writeToFile(fobj,"Network Usage Report")
    writeToFile(fobj,"Sent : %.2f MB" %(net.bytes_sent/(1024*1024)))
    writeToFile(fobj,"Received : %.2f MB" %(net.bytes_recv/(1024*1024)))

    writeToFile(fobj,borderFile())
    writeToFile(fobj,"------------------ End of Log File ---------------")
    writeToFile(fobj,borderFile())

def borderFile():
    return "-"*50

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
        schedule.every(int(interval)).minutes.do(createLog,LogDirectory)

        print("Platform Surveillance System started successfully")
        print("Directory created with name : ",LogDirectory)
        print("Time Interval (minutes) : ",interval)
        print("Press Ctrl + C to stop the execution")
        border()

        # wait till abort
        createLog(LogDirectory)
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