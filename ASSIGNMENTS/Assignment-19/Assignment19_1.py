square = lambda no : no**2

def main():
    """1.Write a program which contains one lambda function which accepts one parameter and return power of two.
Input : 4 Output : 16
Input : 6 Output : 36"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    try:
        num = int(input("Enter a number : "))
        print("Square of ",num," is : ",square(num)) #print("Square of", num, "is:", (lambda no: no**2)(num))
    except ValueError:
        print("Invalid Input. Only numbers are allowed.")

if __name__ == "__main__":
    main()