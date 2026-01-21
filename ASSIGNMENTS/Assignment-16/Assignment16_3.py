def Add(no1,no2):
    """Write a program which contains one function named as Add() which accepts two
numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16"""
    return no1+no2

def main():
    print(Add.__doc__,"\n\n",("-"*50),"\n\n")
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    print("Addition of numbers is : ",Add(num1,num2))

if __name__ == "__main__":
    main()