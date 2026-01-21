# Write a lambda function using filter () which accepts a list of numbers and returns the count of even numbers.


evenCount = lambda no : no % 2 == 0

def main():
    value = []
    limit = int(input("Enter no. of elements : "))
    print("Enter ", limit, " elements : ")
    for i in range(limit):
        value.append(int(input()))
    evenCnt = list(filter(evenCount,value))
    print("Even numbers count is   : ",len(evenCnt))

if __name__ == "__main__":
    main()