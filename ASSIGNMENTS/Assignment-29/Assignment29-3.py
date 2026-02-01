import os
import sys

def copyFileContent(file):
   fdread = open(file,"r")
   fileData = fdread.read()
   fdwrite = open("Hello.txt","w")
   fdwrite.write(fileData)
   print("File data copied successfully")
   fdread.close()
   fdwrite.close()
   

def main():
    """Write a program which accepts an existing file name through command line arguments, creates a new 
file named Hello.txt, and copies all contents from the given file into Hello.txt."""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    if(len(sys.argv)!=2):
       print("Invalid input parameter.")
       print(f"Expected : {sys.argv[0]} <filename.txt>")
       return
       
    sourceFile = sys.argv[1]
    if (sourceFile.__contains__(".txt") == False):
        print("Invalid filwe format")
        return

    if(os.path.exists(sourceFile)):
        copyFileContent(sourceFile)
    else:
        print(f"{sourceFile} does not exists")
       

if __name__ == "__main__":
    main()
