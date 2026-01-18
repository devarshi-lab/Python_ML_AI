# Write a program which accepts two numbers and prints addition, subtraction,
# multiplication and division.

def arithmatic(no1,no2):
    add = no1+no2
    sub = no1-no2
    mult = no1*no2
    div = ""
    if(no2 == 0):
        div = "error"
    else:
        div =no1/no2
    return add,sub,mult,div

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    add,sub,mult,div = arithmatic(no1,no2)
    print("Addition  of ",no1,"and ", no2," is : ",add)
    print("Subtraction  of ",no1,"and ", no2," is : ",sub)
    print("Multiplication  of ",no1,"and ", no2," is : ",mult)
    print("Division  of ",no1,"and ", no2," is : ",div)

if __name__ == "__main__":
    main()