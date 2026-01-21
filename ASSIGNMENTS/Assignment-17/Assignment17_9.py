def countDigits(no):
    count = 0
    # print(len(str(no))) inbuilt
    while(no>0):
        no = int(no / 10)
        count += 1
    return count

def main():
    """Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    try:
        no = int(input("Enter the number : "))
        count = countDigits(no)
        print("Number of digits are : ",count)
    except ValueError:
        print("Invalid Input. Only Numbers Allowed")


if __name__ == "__main__":
    main()
