# Write a lambda function which accepts one number and returns True if number is even otherwise False.

checkEven = lambda no : no % 2 == 0


def main():
    value1 = int(input("Enter first number : "))
    even = checkEven(value1)
    # print("Maximum number is : ",max)
    if(even):
        print("It is even")
    else:
         print("It is odd")
        

if __name__ == "__main__":
    main()