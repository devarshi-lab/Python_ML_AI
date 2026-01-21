def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact *= i
    return fact 

def main():
    """Write a program which accept one number from user and return its factorial.
Input : 5 Output : 120"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter a number : "))
    print("Factorial of ",num," is : ",factorial(num));

if __name__ == "__main__":
    main()