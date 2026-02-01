import os

def isFileExist(file):
    return os.path.exists(file)

def main():
    """Problem Statement: 
Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not. """
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    fileName = input("Enter a file name : ")
    if(isFileExist(fileName)):
        print(f"{fileName} exists")
    else:
        print(f"{fileName} does not exists")

if __name__ == "__main__":
    main()
