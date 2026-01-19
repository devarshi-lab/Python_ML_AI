# 5. Write a lambda function using reduce () which accepts a list of numbers and returns the maximum element.

from functools import reduce

maximum = lambda no1,no2 : no1 if no1>no2 else no2

def main():
     value = []
     limit = int(input("Enter no. of elements : "))
     print("Enter ", limit, " elements : ")
     for i in range(limit):
        value.append(int(input()))
     max = (reduce(maximum,value))
     print("Maximum number is  : ",max)

if __name__ == "__main__":
    main()