import os
import sys

def compareFileContent(file1,file2):
   fd1 = open(file1,"r")
   fd2 = open(file2,"r")
   file1Data = fd1.read()
   file2Data = fd2.read()
   fd1.close()
   fd2.close()
   if(file1Data==file2Data):
       return True
   return False
       
   

def main():
    """Write a program which accepts two file names through command line arguments and compares the 
contents of both files"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    if(len(sys.argv)!=3):
       print("Invalid input parameter.")
       print(f"Expected : {sys.argv[0]} <file1.txt> <file2.txt>")
       return
       
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    
    if(os.path.exists(file1) and os.path.exists(file2)):
        if(compareFileContent(file1,file2)):
            print(f"{file1} and {file2} contains the same data.")
        else:
            print(f"{file1} and {file2} does not contains the same data.")
    else:
        print(f"one of the file does not exists")
       

if __name__ == "__main__":
    main()
