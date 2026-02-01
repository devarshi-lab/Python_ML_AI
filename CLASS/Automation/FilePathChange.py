import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        ret = os.path.isabs(FileName)
        # print(os.path.abspath(FileName))
        if ret:
            print("It is absolute path")
        else:
            print("It is relative path")
            NewPath = os.path.abspath(FileName)
            print("Absolute path is : ",NewPath)
    else:
        print("File does not exists")



if __name__ == "__main__":
    main()