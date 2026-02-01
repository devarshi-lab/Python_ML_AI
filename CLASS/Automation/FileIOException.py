def main():
    try:
        open("demo.txt")
        print("File gets open successfully")
    except FileNotFoundError:
        print("File not found")
    finally:
        print("End of application")
    

if __name__ == "__main__":
    main()