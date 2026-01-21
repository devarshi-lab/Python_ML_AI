def sumDigits(no):
    sum = 0
    while(no>0):
        sum = sum + (no % 10)
        no = int(no / 10)
    return sum

def main():
    """Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    try:
        no = int(input("Enter the number : "))
        sum = sumDigits(no)
        print("Sum of digits of number is : ",sum)
    except ValueError:
        print("Invalid Input. Only Numbers Allowed")


if __name__ == "__main__":
    main()
