import os

def countWordsFromFile(file):
   fd = open(file,"r")
   fileData = fd.read()
   count = len(fileData.split())
   return count

def main():
    """Write a program which accepts a file name from the user and counts the total number of words in that file"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    fileName = input("Enter a file name : ")
    if(os.path.exists(fileName)):
        wordCount = countWordsFromFile(fileName)
        print(f"Total word count from the file is : ", wordCount)
    else:
        print(f"{fileName} does not exists")
       

if __name__ == "__main__":
    main()
