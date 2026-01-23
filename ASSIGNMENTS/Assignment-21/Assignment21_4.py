import threading
import acceptNumbersList

def sumNumbers(numbersList):
    sum = 0
    for j in numbersList:
        sum += j
    print("Sum of numbers is : ",sum) 

def productNumbers(numbersList):
    prod = 1
    for j in numbersList:
        prod *= j
    print("Product of numbers is : ",prod) 
 

def main():
    """Design a Python application that creates two threads.
    • Thread 1 should compute the sum of elements from a list.
    • Thread 2 should compute the product of elements from the same list.
    • Return the results to the main thread and display them."""
    
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    values = acceptNumbersList.acceptListOfNumbers()
    if len(values)==0:
        return
    
    sumThread = threading.Thread(target=sumNumbers,args=(values,))
    prodThread = threading.Thread(target=productNumbers,args=(values,))

    sumThread.start()
    prodThread.start()

    sumThread.join()
    prodThread.join()

if __name__ == "__main__":
    main()

