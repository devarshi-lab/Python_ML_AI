import threading
import time

def sumEven(No):
    sum = 0
    for i in range(2,No+1,2):
        sum += i
    print("Even sum is : ",sum)

def sumOdd(No):
    sum = 0
    for i in range(1,No+1,2):
        sum += i
    print("Odd sum is : ",sum)


def main():
    start = time.time()
    t1 = threading.Thread(target=sumEven,args=(100000000,))
    t2 = threading.Thread(target=sumOdd,args=(100000000,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time.time()
    print("Required time is : ",end-start)

if __name__ == "__main__":
    main()