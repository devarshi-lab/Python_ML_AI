# 3. Write a lambda function which accepts two numbers and returns maximum number.


getMaximum = lambda no1,no2  : no1>no2
# getMaximum = lambda no1, no2: no1 if no1 > no2 else no2


def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    max = getMaximum(value1,value2)
    # print("Maximum number is : ",max)
    if(max):
        print("Maximum number is : ",value1)
    else:
        print("Maximum number is : ",value2)
        

if __name__ == "__main__":
    main()