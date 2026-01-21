multiplication = lambda no1,no2 : no1*no2

def main():
    """2.Write a program which contains one lambda function which accepts two parameters and return its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    try:
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        print("Multiplication of ",num1,"x",num2," is : ",multiplication(num1,num2))
    except ValueError:
        print("Invalid Input. Only numbers are allowed.")

if __name__ == "__main__":
    main()