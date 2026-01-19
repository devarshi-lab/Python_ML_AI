# 9. Write a lambda function which accepts two numbers and returns multiplication.

doMultiplication= lambda no1 , no2 : no1 * no2


def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    result = doMultiplication(value1,value2)
    print("Multiplication  is : ",result)
    

if __name__ == "__main__":
    main()

