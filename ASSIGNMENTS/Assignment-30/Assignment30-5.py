import os

def wordCount(file,wordToFind):
    fd = open(file,"r")
    fileData = fd.read()
    wordPresent = False
    # count = fileData.count(wordToFind) inbuilt method
    # if count > 0 then return True
    # for line in fileData:
    #             if word in line:
    #                 return True
    fd.close()
    for word in fileData.split():
        if word == wordToFind:
            wordPresent = True
            break
    return wordPresent
   

def main():
    """Write a program which accepts a file name and a word from the user and checks whether that word is 
present in the file or not"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    fileName = input("Enter the name of file : ")
    word = input("Enter the word : ")
    if(os.path.exists(fileName)):
       wordPresent = wordCount(fileName,word)
       if wordPresent:
        print(f"{os.path.basename(fileName)} contains the word '{word}' ")
       else:
        print(f"{os.path.basename(fileName)} does not contains the word '{word}' ")
           
    else:
        print(f"{os.path.basename(fileName)} does not exists")
       

if __name__ == "__main__":
    main()
