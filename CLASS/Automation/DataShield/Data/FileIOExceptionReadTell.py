def main():
    try:
        fobj = open("hello.txt","r")
        print("File gets open successfully")

        print("Current offset is : ",fobj.tell())
        fileData = fobj.read(6)
        print("Current offset is : ",fobj.tell())
        print("Data from file is : ")
        print(fileData)
        fobj.close()
    except FileNotFoundError:
        print("File not found")
    finally:
        print("End of application")

if __name__ == "__main__":
    main()