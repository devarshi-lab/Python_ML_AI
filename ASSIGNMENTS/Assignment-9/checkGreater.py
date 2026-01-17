#Write a program which contains one function ChkGreater () that accepts two numbers and prints the greater number.

def checkGreater(no1,no2):
    if no1>no2:
        return no1
    elif no1<no2:
        return no2
    else:
        return "Both are same"
    
def main():
    value1 = int(input("Enter first number : "))
    value2 = int(input("Enter second number : "))
    greater = checkGreater(value1,value2)
    print("The grater number is : ",greater)

if __name__ == "__main__":
    main()


