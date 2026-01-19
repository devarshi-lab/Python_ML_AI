# 1. Write a lambda function which accepts one number and returns square of that number.
#
getSquare = lambda no : no*no

def main():
    value = int(input("Enter a number : "))
    square = getSquare(value)
    print("Square of ",value," is : ",square)

if __name__ == "__main__":
    main()