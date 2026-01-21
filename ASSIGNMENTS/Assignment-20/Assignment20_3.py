import threading
import acceptNumbersList

def evenListSum(numbers):
    sum = 0
    for i in numbers:
        if(i % 2 == 0):
            sum += i
    print(" Sum of all Even numbers is : ",sum)


def oddListSum(numbers):
    sum = 0
    for i in numbers:
        if(i % 2 == 1):
            sum += i
    print("Sum of Odd numbers is : ",sum)
    

def main():
    """Design a Python application that creates two threads named EvenList and OddList.
    • Both threads should accept a list of integers as input.
    • The EvenList thread should:
    ◦ Extract all even elements from the list.
    ◦ Calculate and display their sum.
    • The OddList thread should:
    ◦ Extract all odd elements from the list.
    ◦ Calculate and display their sum.
    • Threads should run concurrently."""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    values = acceptNumbersList.acceptListOfNumbers()
    if(len(values)==0):
        return
    
    evenListSumThread = threading.Thread(target=evenListSum,args=(values,))
    oddListSumThread = threading.Thread(target=oddListSum,args=(values,))

    evenListSumThread.start()
    oddListSumThread.start()

    evenListSumThread.join()
    oddListSumThread.join()
    print("Exit from main")

if __name__ == "__main__":
    main()
    