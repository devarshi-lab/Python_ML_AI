import os

def readFileContent(file):
   fd = open(file,"r")
   fileData = fd.read()
   fd.close()
   return fileData

def main():
    """Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the """
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    fileName = input("Enter a file name : ")
    if(os.path.exists(fileName)):
        print(f"Content from the file {fileName} is : ")
        print(readFileContent(fileName))
    else:
        print(f"{fileName} does not exists")
       

if __name__ == "__main__":
    main()
