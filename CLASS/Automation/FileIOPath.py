import os

def main():
    FileName = input("Enter the name of file : ")

    ret = os.path.isabs(FileName)
    # print(os.path.abspath(FileName))
    if ret:
        print("It is absolute path")
    else:
        print("It is relative path")



if __name__ == "__main__":
    main()