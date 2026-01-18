import threading

iCnt = 0

def update():
    global iCnt

    for _ in range(20000000):
        iCnt = iCnt + 1

def main():
    global iCnt
    update()
    update()
    print("Value of icnt is : ",iCnt)

if __name__ == "__main__":
    main()