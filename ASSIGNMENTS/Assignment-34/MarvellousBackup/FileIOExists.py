import os

def main():
    FileName = input("Enter the name of file : ")

    ret = os.path.exists(FileName)
    if ret:
        fobj = open(FileName,"r")
        print("File gets opened successfully")
    else:
        print("File not exists.")



if __name__ == "__main__":
    main()