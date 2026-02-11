import time
import psutil
import sys
import os
import schedule
import sendMail

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

    processDetails = processScan()
    header_format = "{:<5} {:<35} {:<25} {:<10} {:<25} {:<10} {:<15} {:<20} {:<15} {:<15} {:<15} \n"
    data_format = "{:<5} {:<35} {:<25} {:<10} {:<25} {:<10.2f} {:<15.2f} {:<20} {:<15} {:<15} {:<15} \n"
    writeToFile(fobj,"-"*132+"\n")
    writeToFile(fobj,header_format.format("PID", "NAME", "USERNAME","STATUS","CREATE TIME","CPU PERCENT","MEMORY PERCENT","THREADS RUNNING","OPEN FILES","RSS","VMS"))
    writeToFile(fobj,"-"*200+"\n")
    for info in processDetails:
        writeToFile(fobj,data_format.format(info.get("pid"),info.get("name") or "NA",info.get("username") or "NA",info.get("status")  or "NA",info.get("create_time")  or "NA",info.get("cpu_percent") or 0.0,info.get("memory_percent") or 0.0,info.get("num_threads"),info.get("open_files"),str(info.get("rss")) + " MB",str(info.get("vms")) + " MB"))
    writeToFile(fobj,"-"*200+"\n")

    writeToFile(fobj,"SUMMARY")

    writeToFile(fobj,"-"*200+"\n")
    writeToFile(fobj,"TOTAL PROCESSES : "+ str(len(processDetails)))
    writeToFile(fobj,"-"*200+"\n")
    writeToFile(fobj,"TOP 10 CPU CONSUMING PROCESS")
    writeToFile(fobj,"-"*200+"\n")
    processDetails.sort(key=lambda x: x.get("cpu_percent", 0.0),reverse=True)
    for info in processDetails[:10]:
        writeToFile(fobj,data_format.format(info.get("pid"),info.get("name") or "NA",info.get("username") or "NA",info.get("status")  or "NA",info.get("create_time")  or "NA",info.get("cpu_percent") or 0.0,info.get("memory_percent") or 0.0,info.get("num_threads"),info.get("open_files"),str(info.get("rss")) + " MB",str(info.get("vms")) + " MB"))
    
    writeToFile(fobj,"-"*200+"\n")
    writeToFile(fobj,"TOP 10 MEMORY CONSUMING PROCESS")
    writeToFile(fobj,"-"*200+"\n")
    processDetails.sort(key=lambda x: x.get("memory_percent", 0.0),reverse=True)
    for info in processDetails[:10]:
        writeToFile(fobj,data_format.format(info.get("pid"),info.get("name") or "NA",info.get("username") or "NA",info.get("status")  or "NA",info.get("create_time")  or "NA",info.get("cpu_percent") or 0.0,info.get("memory_percent") or 0.0,info.get("num_threads"),info.get("open_files"),str(info.get("rss")) + " MB",str(info.get("vms")) + " MB"))
    
    writeToFile(fobj,"-"*200+"\n")
    writeToFile(fobj,"TOP 10 THREAD CONSUMING PROCESS")
    writeToFile(fobj,"-"*200+"\n")
    processDetails.sort(key=lambda x: x.get("num_threads", 0.0),reverse=True)
    for info in processDetails[:10]:
        writeToFile(fobj,data_format.format(info.get("pid"),info.get("name") or "NA",info.get("username") or "NA",info.get("status")  or "NA",info.get("create_time")  or "NA",info.get("cpu_percent") or 0.0,info.get("memory_percent") or 0.0,info.get("num_threads"),info.get("open_files"),str(info.get("rss")) + " MB",str(info.get("vms")) + " MB"))
    
    writeToFile(fobj,"-"*200+"\n")
    writeToFile(fobj,"TOP 10 OPEN FILES PROCESS")
    writeToFile(fobj,"-"*200+"\n")
    processDetails.sort(key=lambda x: x.get("open_files", 0.0),reverse=True)
    for info in processDetails[:10]:
        writeToFile(fobj,data_format.format(info.get("pid"),info.get("name") or "NA",info.get("username") or "NA",info.get("status")  or "NA",info.get("create_time")  or "NA",info.get("cpu_percent") or 0.0,info.get("memory_percent") or 0.0,info.get("num_threads"),info.get("open_files"),str(info.get("rss")) + " MB",str(info.get("vms")) + " MB"))

    # writeToFile(fobj,json.dumps(processDetails,indent=4))

    writeToFile(fobj,"-"*200+"\n")
    writeToFile(fobj,"------------------ End of Log File ---------------")
    writeToFile(fobj,borderFile())

    sendLogMail(FileName)


def sendLogMail(filePath):
    sender_email = "devarshipimpale02@gmail.com"
    app_password = "yittwcbhqkuyycwc"
    receiver_mail = "devarshipimpale@gmail.com"
    subject = "System Surviellance Report - " + time.ctime()
    body = """Dear ,

    Please find attached system report file.

Regards,
Devarshi Pimpale
    """

    sendMail.send_mail(sender_email,app_password,receiver_mail,subject,body,True,filePath)

def processScan():
    listProcess = []

    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass
    
    time.sleep(0.2)

    for proc in psutil.process_iter(attrs=["pid","name","username","status","create_time","num_threads"]):
        try:
            info = proc.as_dict(attrs=["pid","name","username","status","create_time","num_threads"])
            # print(proc.memory_info().rss)
            # print(proc.memory_info().vms)
            info["open_files"] = len(proc.open_files())
            info["rss"] = f"{((proc.memory_info().rss) / (1024*1024)):.2f}"
            info["vms"] = f"{(proc.memory_info().vms / (1024*1024)):.2f}"

            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"

            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            listProcess.append(info)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listProcess

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
            print("7. Store information about Number of Threads created by  process  ")

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