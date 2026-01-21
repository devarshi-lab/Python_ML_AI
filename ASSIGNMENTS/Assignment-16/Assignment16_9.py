def main():
    """Write a program which display first 10 even numbers on screen.
Output : 2 4 6 8 10 12 14 16 18 20"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter number : "))
    i = 1
    while(num!=0):
        if(i % 2 == 0):
            print(i)
            num -= 1
        i += 1

if __name__ == "__main__":
    main()