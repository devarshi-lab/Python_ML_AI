import time
import os
import multiprocessing

def summationofCube(no):
    print("Process is running with PID : ",os.getpid())
    sum = 0
    for i in range(1,no+1):
        sum += (i**3)
    return sum

def main():
    data = [1000000,2000000,3000000,4000000,5000000,6000000,7000000,8000000,9000000,10000000]
    result = []

    stime = time.time()
    pobj = multiprocessing.Pool()
    result = pobj.map(summationofCube,data)

    pobj.close()
    pobj.join()

    etime = time.time()
    # ret = summationofCube(10000000)
    print(result)
    print("Time required : ",etime-stime)

if __name__ == "__main__":
    main()