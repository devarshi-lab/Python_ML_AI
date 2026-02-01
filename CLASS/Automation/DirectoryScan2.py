import os

def DirectoryScanner(DirectoryName):
    print("Content of the directory are : ")
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        print("Folder Name : ",FolderName)

        for subf in  SubFolderName:
            print("SubFolder Name : ",subf)
        
        for fname in FileName:
            print("Filename : ",fname)

def main():
    DirectoryName = input("Enter the name of directory : ")
    if(os.path.exists(DirectoryName) and os.path.isdir(DirectoryName)):
        DirectoryScanner(DirectoryName)
    else:
        print("Directory does not exist")
    

if __name__ == "__main__":
    main()