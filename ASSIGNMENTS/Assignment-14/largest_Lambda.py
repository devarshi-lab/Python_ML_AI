# Write a lambda function which accepts three numbers and returns largest number.


# getMaximum = lambda no1,no2  : no1>no2
# getLargest = lambda no1, no2, no3 : no1 if no1 > no2  and no1 > no3 else no2 if no2>no1 and no2>no3 else no3
getLargest = lambda no1, no2, no3 : no1 if no1 > no2  and no1 > no3 else no2 if  no2>no3 else no3


def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    value3 = int(input("Enter third number : "))
    max = getLargest(value1,value2,value3)
    print("Largest number is : ",max)
    # if(max):
    #     print("Maximum number is : ",value1)
    # else:
    #     print("Maximum number is : ",value2)
        

if __name__ == "__main__":
    main()