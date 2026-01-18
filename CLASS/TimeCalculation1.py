import time

def factorial(no):
    Fact = 1
    for i in range(1,no+1):
        Fact = Fact * i
    return Fact


def main():

    value = int(input("Enter number : "))
    ret = factorial(value)
    print("Factorial is : ",ret)

if __name__ == "__main__":
    main()