def main():
    """Write a program which accept name from user and display length of its name.
Input : Marvellous Output : 10"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    name = (input("Enter string : "))
    print(len(name))

if __name__ == "__main__":
    main()