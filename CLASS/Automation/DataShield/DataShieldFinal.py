import time
import sys
import os
import schedule
import shutil 
import hashlib
import zipfile

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

def backupFiles(source,destination):
    copied_Files = []
    print("Creating the backup folder for backup process")
    os.makedirs(destination, exist_ok=True)

    for root,dir,files in os.walk(source):
        for file in files:
            src_path = os.path.join(root,file)
            relative = os.path.relpath(src_path,source)
            dest_path = os.path.join(destination,relative)
            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #copy the file if its new or updated
            if((not os.path.exists(dest_path)) or (calculate_hash(dest_path)!=calculate_hash(src_path))):
                shutil.copy2(src_path,dest_path)
                copied_Files.append(relative)
                            
    return copied_Files

def MarvellousDataShieldStart(Source = "Data"):
    BackupFolderName = "MarvellousBackup"

    border()
    print("Backup Process Started Successfully : ",time.ctime())
    border()

    files = backupFiles(Source,BackupFolderName)
    zip_file = makezip(BackupFolderName)

    border()
    print("Backup Completed successfully.")
    print("Files Copied : ",len(files))
    print("Zip file gets created : ",zip_file)
    border()
    

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
        schedule.every(int(interval)).minutes.do(MarvellousDataShieldStart,SourceDirectory)

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