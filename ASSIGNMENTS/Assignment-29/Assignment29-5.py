import os
import sys

def wordCount(file,wordToFind):
    fd = open(file,"r")
    fileData = fd.read()
    count = 0
    # count = fileData.count(wordToFind) inbuilt method
    fd.close()
    for word in fileData.split():
        if word == wordToFind:
            count += 1
    return count
   

def main():
    """Write a program which accepts a file name and one string from the user and returns the frequency 
(count of occurrences) of that string in the file."""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    fileName = input("Enter the name of file : ")
    word = input("Enter the word : ")
    if(os.path.exists(fileName)):
       wordCnt = wordCount(fileName,word)
       print(f"{fileName} contains the word '{word}' {wordCnt} times.")
    else:
        print(f"{fileName} does not exists")
       

if __name__ == "__main__":
    main()
