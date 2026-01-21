import threading

def evenFactors(no):
    sum = 0
    for i in range(2,(no//2)+1,2):
        if(no % i == 0):
            sum += i
    print(" Sum of Even Factors of ",no," is : ",sum)


def oddFactors(no):
    sum = 0
    for i in range(1,(no//2)+1,2):
        if(no % i == 0):
            sum += i
    print("Sum of Odd Factors of ",no," is : ",sum)
    

def main():
    """Design a Python application that creates two threads named EvenFactor and OddFactor.
• Both threads should accept one integer number as a parameter.
• The EvenFactor thread should:
◦ Identify all even factors of the given number.
◦ Calculate and display the sum of even factors.
• The OddFactor thread should:
◦ Identify all odd factors of the given number.
◦ Calculate and display the sum of odd factors.
• After both threads complete execution, the main thread should display the message:“Exit from main”"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = 0
    try:
        num = int(input("Enter a number : "))
    except ValueError:
        print("Invalid Input. Only numbers are allowed")
        return
    
    evenFactorThread = threading.Thread(target=evenFactors,args=(num,))
    oddFactorThread = threading.Thread(target=oddFactors,args=(num,))

    evenFactorThread.start()
    oddFactorThread.start()

    evenFactorThread.join()
    oddFactorThread.join()
    print("Exit from main")

if __name__ == "__main__":
    main()
    