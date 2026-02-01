import os
def main():
    DirectoryName = input("Enter the name of directory : ")
    print("Content of the directory are : ")
    print("-"*50)
    print(list(os.walk(DirectoryName)))
    print("-"*50)
    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        print("Folder Name : ",FolderName)

        for subf in  SubFolderName:
            print("SubFolder Name : ",subf)
        
        for fname in FileName:
            print("Filename : ",fname)

if __name__ == "__main__":
    main()