def main():
    """Write a program which accept one number and display below pattern.
Input : 5
Output : 
* * * * *
* * * *
* * *
* *
*
"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter a number : "))
    for i in range(num):
        print("*"*(num-i))

if __name__ == "__main__":
    main()