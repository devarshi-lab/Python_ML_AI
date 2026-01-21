def chkNum(no):
    """Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console.
Input : 11 Output : Odd Number
Input : 8 Output : Even Number"""
    return no % 2 ==0

def main():
    print(chkNum.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter number : "))
    if(chkNum(num)):
        print("It is even number")
    else:
        print("It is odd number")

if __name__ == "__main__":
    main()