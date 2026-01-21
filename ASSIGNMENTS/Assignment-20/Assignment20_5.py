import threading

def printRange(value):
    for i in range(1,value+1):
        print(i,end=" ")
    print()

def printRangeReverse(value):
    for i in range(value,0,-1):
        print(i,end=" ")


def main():
    """Design a Python application that creates two threads named Thread1 and Thread2.
        • Thread1 should display numbers from 1 to 50.
        • Thread2 should display numbers from 50 to 1 in reverse order.
        • Ensure that:
        ◦ Thread2 starts execution only after Thread1 has completed.
        • Use appropriate thread synchronization"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    
    printRangeThread = threading.Thread(target=printRange,args=(50,))
    printRangeReverseThread = threading.Thread(target=printRangeReverse,args=(50,))

    printRangeThread.start()
    printRangeThread.join()

    printRangeReverseThread.start()
    printRangeReverseThread.join()

if __name__ == "__main__":
    main()
    