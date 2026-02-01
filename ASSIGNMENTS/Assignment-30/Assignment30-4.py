import os

def copyFileContent(srcFile,destFile):
   fd1 = open(srcFile,"r")
   fd2 = open(destFile,"w")
   fd2.write(fd1.read())
   print(f"File data copied successfully from {os.path.basename(srcFile)} to {os.path.basename(destFile)}")
   fd1.close()
   fd2.close()
   

def main():
    """Write a program which accepts two file names from the user. 
• First file is an existing file 
• Second file is a new file 
Copy all contents from the first file into the second file."""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    
       
    sourceFile = input("Enter the name of source file : ")
    destinationFile = input("Enter the name of destination file : ")

    if(os.path.exists(sourceFile)):
        copyFileContent(sourceFile,destinationFile)
    else:
        print(f"{os.path.basename(sourceFile)} does not exists")
       

if __name__ == "__main__":
    main()
