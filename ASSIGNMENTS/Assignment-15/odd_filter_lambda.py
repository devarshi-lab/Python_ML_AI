# 3. Write a lambda function using filter () which accepts a list of numbers and returns a list of odd numbers.


getOdd = lambda no : no % 2 != 0

def main():
    value = []
    limit = int(input("Enter no. of elements : "))
    print("Enter ", limit, " elements : ")
    for i in range(limit):
        value.append(int(input()))
    even = list(filter(getOdd,value))
    print("Odd numbers are  : ",even)

if __name__ == "__main__":
    main()