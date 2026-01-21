def main():
    """Write a program which accept one number and display below pattern.
Input : 5
Output : 
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter a number : "))
    for i in range(num+1):
        for j in range(1,i+1):
            print(j,end="\t")
        print()

if __name__ == "__main__":
    main()