# 7. Write a lambda function which accepts one number and returns True if divisible by 5.


checkOdd = lambda no : no % 5 == 0


def main():
    value1 = int(input("Enter  number : "))
    divisible = checkOdd(value1)
    # print(divisible)
    # print("Maximum number is : ",max)
    if(divisible):
        print("It is divisible by 5")
    else:
         print("It is not divisible by 5")
        

if __name__ == "__main__":
    main()
