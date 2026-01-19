# 3. Write a lambda function which accepts two numbers and returns minimum number.


getminimum = lambda no1,no2  : no1<no2
# getminimum = lambda no1, no2: no1 if no1 < no2 else no2


def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    max = getminimum(value1,value2)
    # print("minimum number is : ",max)
    if(max):
        print("minimum number is : ",value1)
    else:
        print("minimum number is : ",value2)
        

if __name__ == "__main__":
    main()