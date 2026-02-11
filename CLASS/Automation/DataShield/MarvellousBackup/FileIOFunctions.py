import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        fobj = open(FileName,"r")
        print(fobj.name)
        print(fobj.mode)
        print(fobj.closed)
        fobj.close()
        print(fobj.closed)
    else:
        print("File does not exists")



if __name__ == "__main__":
    main()