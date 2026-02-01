import os

def main():
    FileName = input("Enter the name of file : ")

    if(os.path.exists(FileName)):
        os.remove(FileName)
        print("File deleted")
    else:
        print("File does not exists")



if __name__ == "__main__":
    main()