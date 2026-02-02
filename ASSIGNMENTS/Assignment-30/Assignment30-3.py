import os

def fileContentLineByLine(file):
   fd = open(file,"r")
   # fileData = fd.readlines()
   # for line in fd.readlines():
   #     print(line)
   line = fd.readline()
   while (line != ""):
       print(line)
       line = fd.readline()
     

def main():
    """Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen."""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    fileName = input("Enter a file name : ")
    if(os.path.exists(fileName)):
       fileContentLineByLine(fileName)
    else:
        print(f"{os.path.basename(fileName)} does not exists")
       

if __name__ == "__main__":
    main()
