import time

def factorial(no):
    Fact = 1
    for i in range(1,no+1):
        Fact = Fact * i
    return Fact


def main():

    value = int(input("Enter number : "))
    startTime = time.time()
    ret = factorial(value)
    endTime = time.time()
    print("Factorial is : ",ret)
    print("Total time required is : ",endTime-startTime)

if __name__ == "__main__":
    main()