def main():
    try:
        fobj = open("hello.txt","a")
        print("File gets open successfully")

        fobj.write("Python Automation\n")
        fobj.close()
    except FileNotFoundError:
        print("File not found")
    finally:
        print("End of application")

if __name__ == "__main__":
    main()