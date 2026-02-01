def addition(no1,no2):
    return no1 + no2

def subtraction(no1,no2):
    return no1 - no2

def main():
    no1 = 0
    no2 = 0
    ans = 0

    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ans = addition(no1,no2)

    print("Addition is : " , ans)

    ans = subtraction(no1,no2)
    print("Subtraction is : " , ans)


if __name__ == "__main__":
    main()