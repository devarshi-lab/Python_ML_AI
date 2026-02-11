def main():
    try:
        fobj = open("hello.txt","w")
        print("File gets open successfully")

        fobj.write("Jay Ganesh Marvellous...")
        fobj.close()
    except FileNotFoundError:
        print("File not found")
    finally:
        print("End of application")

if __name__ == "__main__":
    main()