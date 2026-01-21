#  Write a lambda function using reduce () which accepts a list of numbers and returns the minimum element.

from functools import reduce

minimum = lambda no1,no2 : no1 if no1<no2 else no2

def main():
     value = []
     limit = int(input("Enter no. of elements : "))
     print("Enter ", limit, " elements : ")
     for i in range(limit):
        value.append(int(input()))
     max = (reduce(minimum,value))
     print("Minimum number is  : ",max)

if __name__ == "__main__":
    main()