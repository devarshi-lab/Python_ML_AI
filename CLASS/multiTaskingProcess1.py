import multiprocessing
import time
import os

def sumEven(No):
    print("process id of sumeven : ",os.getpid())           #51
    print("parent process id of sumeven : ",os.getppid())   #21
    sum = 0
    for i in range(2,No+1,2):
        sum += i
    print("Even sum is : ",sum)

def sumOdd(No):
    print("process id of sumodd : ",os.getpid())            #101
    print("parent process id of sumodd : ",os.getppid())    #21
    sum = 0
    for i in range(1,No+1,2):
        sum += i
    print("Odd sum is : ",sum)


def main():
    print("process id of main : ",os.getpid())              # 21
    print("parent process id of main : ",os.getppid())      # 11 CMD
    start = time.time()
    p1 = multiprocessing.Process(target=sumEven,args=(100000000,))
    p2 = multiprocessing.Process(target=sumOdd,args=(100000000,))
    
    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print("Required time is : ",end-start)

if __name__ == "__main__":
    main()