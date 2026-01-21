#  Write a lambda function using reduce () which accepts a list of numbers and returns the product of all elements.

from functools import reduce

product = lambda no1,no2 : no1 * no2

def main():
    value = []
    limit = int(input("Enter no. of elements : "))
    print("Enter ", limit, " elements : ")
    for i in range(limit):
        value.append(int(input()))
    prod = (reduce(product,value))
    print("Even numbers are  : ",prod)

if __name__ == "__main__":
    main()