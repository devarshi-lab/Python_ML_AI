def divisibleBy5(no):
    return no % 5 ==0

def main():
    """Write a program which contains one function that accept one number from user and
returns
true if number is divisible by 5 otherwise return false.
Input : 8 Output : False
Input : 25 Output : True"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter number : "))
    if(divisibleBy5(num)):
        print("It is divisible by 5")
    else:
        print("It is not divisible by 5")

if __name__ == "__main__":
    main()