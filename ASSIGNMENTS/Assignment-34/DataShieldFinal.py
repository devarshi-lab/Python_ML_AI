import time
import sys
import os
import schedule
import shutil 
import hashlib
import zipfile
import sendMail


def writeToFile(fileObject,data):
    fileObject.write(data+"\n")

def makezip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder+"_"+timestamp+".zip"

    # open the zip file
    zobj = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
    
    for root,dirs,files in os.walk(folder):
        for file in files:
            fullPath = os.path.join(root,file)
            relative = os.path.relpath(fullPath,folder)
            zobj.write(fullPath,relative)
    
    zobj.close()

    return zip_name

def calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path,"rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)
    
    return hobj.hexdigest()

def getIgnore():
    try:
        fd = open(".ignore","r")
        extension = [line.strip() for line in fd]
        return extension
    except FileNotFoundError:
        pass

    return []

def backupFiles(source,destination):
    copied_Files = []
    print("Creating the backup folder for backup process")
    os.makedirs(destination, exist_ok=True)

    ignoreExtensions = getIgnore()
    for root,dir,files in os.walk(source):
        for file in files:
            src_path = os.path.join(root,file)
            relative = os.path.relpath(src_path,source)
            dest_path = os.path.join(destination,relative)
            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #copy the file if its new or updated
            if(((not os.path.splitext(file)[1] in (ignoreExtensions))) and ( (not os.path.exists(dest_path)) or (calculate_hash(dest_path)!=calculate_hash(src_path)))):
                shutil.copy2(src_path,dest_path)
                copied_Files.append(relative)
                            
    return copied_Files

def MarvellousDataShieldStart(Source = "Data"):
    BackupFolderName = "MarvellousBackup"

    if not os.path.exists("Logs"):
        os.mkdir("Logs")

    logfile = "Logs/DataShieldLog_%s.log" %(time.strftime("%Y-%m-%d_%H-%M-%S"))
    fd = open(logfile,"w")
    try:
        writeToFile(fd,borderFile())
        writeToFile(fd,"Backup Process Started Successfully : "+time.ctime())
        writeToFile(fd,borderFile())

        files = backupFiles(Source,BackupFolderName)
        zip_file = makezip(BackupFolderName)

        writeToFile(fd,borderFile())
        writeToFile(fd,"Backup Completed successfully.")
        writeToFile(fd,"Files Copied : " + str(len(files)))
        writeToFile(fd,"Zip file gets created : "+zip_file)
        writeToFile(fd,borderFile())

        fd.close()

        fd = open("DataShieldHistory.log","a")
        DataFormat = "{:<25} {:<15} {:<50} {:<15}"
        writeToFile(fd,DataFormat.format(time.strftime("%Y-%m-%d_%H-%M-%S"),str(len(files)),zip_file,str(os.path.getsize(zip_file)) + " bytes"))
        fd.close()
    
        ""
        sendLogMail(zip_file,logfile)
    except Exception as e:
        import traceback
        writeToFile(fd,borderFile())
        writeToFile(fd, "Exception occurred:")
        writeToFile(fd, traceback.format_exc())
        writeToFile(fd,borderFile())


def sendLogMail(zipname,filePath):
    sender_email = "devarshipimpale02@gmail.com"
    app_password = "yittwcbhqkuyycwc"
    receiver_mail = "devarshipimpale@gmail.com"
    subject = "Data Shield Report - " + time.ctime()
    body = """Dear ,

    Data backup has completed successfully.
    Please find attached log file for more details.
    
    ZipFileName - %s

Regards,
Devarshi Pimpale
    """ %zipname

    sendMail.send_mail(sender_email,app_password,receiver_mail,subject,body,True,filePath)



def restoreZip(zipFileName,Destination = None):
    try:
        if Destination is None:
            Destination = zipFileName[:-4]
        zp = zipfile.ZipFile(zipFileName,"r")
        zp.extractall(os.path.abspath(Destination))
        print(f"Successfully extracted '{zipFileName}' to '{Destination}'")
    except zipfile.BadZipFile as e:
        print(f"Error: The file '{zipFileName}' is not a valid zip file or is corrupted. {e}")
    except FileNotFoundError as e:
        print(f"Error: The file '{zipFileName}' was not found. {e}")


def getHistory():
    try:
        fd = open("DataShieldHistory.log","r")
        DataFormat = "{:<25} {:<15} {:<50} {:<15}"
        print(DataFormat.format("Date","No. of Files","Zip Name","Zip Size"))
        print(fd.read())
        fd.close()
    except FileNotFoundError:
        print("History File Not Found")    

def borderFile():
    return "-"*80

def border():
    print("-"*80)

def main():
    border()
    print("--------- Marvellous Data Schield System ---------")
    border()
    if(len(sys.argv)==2):
        if(sys.argv[1].lower()=="--h"):
            print("This script is used to :")
            print("1. Takes auto backup at given time")
            print("2. Backup only new and updated files")
            print("3. Create and archive of the backup periodically")
            
        elif(sys.argv[1].lower()=="--u"):
            print("Use the automation script as")
            print(f"{sys.argv[0]} <command>")
            print("Command : ")
            print("--backup | --b : To backup the specified directory")
            print(f"\t usage : {sys.argv[0]} --backup <TimeInterval> <SourceDirectory>")
            print("\t\tTimeInterval : The time in minutes for periodic scheduling")
            print("\t\tSourceDirectory : Name of directory of which we have to take backup")
            print("--restore | --r : To restore the zip")
            print(f"\t usage : {sys.argv[0]} --restore <ZipFileName> <Destination>")
            print("\t\tZipFileName : Name of zip with path to be extracted")
            print("\t\tDestination : Path where zip should extract (optional)")
            print("--history | --hi : To get history")
            print(f"\t usage : {sys.argv[0]} --history")
        
        elif(sys.argv[1].lower()=="--history" or sys.argv[1].lower()=="--hi") :
            getHistory()
            
        else:
            print("Invalid number of command line argumnets")
            print("Please use --h or --u to get more details")
    
    elif(len(sys.argv)==3):
        if sys.argv[1].lower() == "--restore" or sys.argv[1].lower() == "--r" :
            restoreZip(sys.argv[2])

    elif(len(sys.argv)==4):
        if sys.argv[1].lower() == "--restore" or sys.argv[1].lower() == "--r" :
            restoreZip(sys.argv[2],sys.argv[3])
        
        elif sys.argv[1].lower() == "--backup" or sys.argv[1].lower() == "--b" :

            interval = sys.argv[2]
            SourceDirectory = sys.argv[3]
            # schedule.every(int(interval)).minutes.do(MarvellousDataShieldStart,SourceDirectory)

            print("Data Shield System started successfully")
            print("Time Interval (minutes) : ",interval)
            print("Press Ctrl + C to stop the execution")
            border()

            # wait till abort
            MarvellousDataShieldStart(SourceDirectory)
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