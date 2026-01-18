

def summationofCube(no):
    sum = 0
    for i in range(1,no+1):
        sum += (i**3)
    return sum

def main():
    ret = summationofCube(10)
    print(ret)

if __name__ == "__main__":
    main()