def checkNumber(no):
    if(no>0):
        return "Positive Number"
    elif(no<0):
        return "Negative Number"
    else:
        return "Zero"
    
def main():
    """6.Write a program which accept number from user and check whether that number is
positive or
negative or zero.
Input : 11 Output : Positive Number
Input : -8 Output : Negative Number
Input : 0 Output : Zero"""

    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter number : "))
    print("The given number is : ",checkNumber(num))

if __name__ == "__main__":
    main()