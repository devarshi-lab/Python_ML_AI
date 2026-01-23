import threading
import acceptNumbersList

def maxNumber(numbersList):
    print("Prime numbers from list : ",end=" ")
    max = numbersList[0]
    for j in numbersList:
        if j>max:
            max = j
    print("Max number is : ",max) 

def minNumber(numbersList):
    print("Prime numbers from list : ",end=" ")
    min = numbersList[0]
    for j in numbersList:
        if j<min:
            min = j
    print("Min number is : ",min) 
 

def main():
    """Design a Python application that creates two threads.
        • Thread 1 should calculate and display the maximum element from an list.
        • Thread 2 should calculate and display the minimum element from the same list.
        • The list should be accepted from the user."""
    
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    values = acceptNumbersList.acceptListOfNumbers()
    if len(values)==0:
        return
    
    maxThread = threading.Thread(target=maxNumber,args=(values,))
    minThread = threading.Thread(target=minNumber,args=(values,))

    maxThread.start()
    minThread.start()

    maxThread.join()
    minThread.join()

if __name__ == "__main__":
    main()

