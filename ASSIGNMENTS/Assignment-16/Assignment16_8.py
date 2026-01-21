def main():
    """Write a program which accept number from user and print that number of “*” on screen.
Input : 5 Output : * * * * *"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter number : "))
    print("*"*num)

if __name__ == "__main__":
    main()