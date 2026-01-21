#  Write a lambda function using filter () which accepts a list of numbers and returns a list of numbers divisible by both 3 and 5.

isDivisibleBy5and3 = lambda no : no % 3 == 0 and no % 5 == 0

def main():
    value = []
    limit = int(input("Enter no. of elements : "))
    print("Enter ", limit, " elements : ")
    for i in range(limit):
        value.append(int(input()))
    even = list(filter(isDivisibleBy5and3,value))
    print("Numbers which are divisible by 5 and 3  : ",even)

if __name__ == "__main__":
    main()
