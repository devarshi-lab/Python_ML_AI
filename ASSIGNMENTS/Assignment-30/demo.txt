import os

def countLinesFromFile(file):
   fd = open(file,"r")
   fileData = fd.read()
   count = len(fileData.split("\n"))
   return count

def main():
    """Write a program which accepts a file name from the user and counts how many lines are present in the file"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    fileName = input("Enter a file name : ")
    if(os.path.exists(fileName)):
        lineCount = countLinesFromFile(fileName)
        print(f"Total line count from the {os.path.basename(fileName)} is : ", lineCount)
    else:
        print(f"{os.path.basename(fileName)} does not exists")
       

if __name__ == "__main__":
    main()
