# seek(offset,whence)
# seek(कुठे ,कुठून )
# whence / कुठून : 0 / 1 / 2 
# 0 : Starting 
# 1 : Current  
# 2 : End  
def main():
    try:
        fobj = open("hello.txt","r")
        print("File gets open successfully")

        print("Current offset is : ",fobj.tell()) # 0
        fobj.seek(7,0)
        print("Current offset is : ",fobj.tell()) # 7
        fileData = fobj.read(10)
        print("Current offset is : ",fobj.tell()) # 17
        print("Data from file is : ")
        print(fileData)
        fobj.close()
    except FileNotFoundError:
        print("File not found")
    finally:
        print("End of application")

if __name__ == "__main__":
    main()