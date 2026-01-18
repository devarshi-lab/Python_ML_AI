import threading

def sumEven(No):
    sum = 0
    for i in range(2,No+1,2):
        sum += i
    print("Even sum is : ",sum)


def main():
    sumEven(10)

if __name__ == "__main__":
    main()