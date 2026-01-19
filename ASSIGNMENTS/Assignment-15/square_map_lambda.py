# 1. Write a lambda function using map () which accepts a list of numbers and returns a list of squares of each number.

getSquare = lambda no : no*no

def main():
    value = []
    limit = int(input("Enter no. of elements : "))
    print("Enter ", limit, " elements : ")
    for i in range(limit):
        value.append(int(input()))
    square = list(map((lambda no : no*no),value))
    print("Square of ",value," is : ",square)

if __name__ == "__main__":
    main()