# 8. Write a lambda function which accepts two numbers and returns addition.


doAddition = lambda no1 , no2 : no1 + no2


def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    result = doAddition(value1,value2)
    print("Addition  is : ",result)
    

if __name__ == "__main__":
    main()

