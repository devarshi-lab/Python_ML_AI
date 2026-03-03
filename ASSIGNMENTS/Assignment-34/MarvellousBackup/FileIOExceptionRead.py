def main():
    try:
        fobj = open("hello.txt","r")
        print("File gets open successfully")

        fileData = fobj.read()
        print("Data from file is : \n",fileData)
        fobj.close()
    except FileNotFoundError:
        print("File not found")
    finally:
        print("End of application")

if __name__ == "__main__":
    main()