# Write a lambda function which accepts one number and returns True if number is odd  otherwise False.


checkOdd = lambda no : no % 2 != 0


def main():
    value1 = int(input("Enter first number : "))
    odd = checkOdd(value1)
    # print("Maximum number is : ",max)
    if(odd):
        print("It is odd")
    else:
         print("It is even")
        

if __name__ == "__main__":
    main()