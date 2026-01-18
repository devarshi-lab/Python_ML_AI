import time

def summationofCube(no):
    sum = 0
    for i in range(1,no+1):
        sum += (i**3)
    return sum

def main():
    stime = time.time()
    ret = summationofCube(10000000)
    etime = time.time()
    print(ret)
    print("Time required : ",etime-stime)
if __name__ == "__main__":
    main()