import threading
import acceptNumbersList

def checkNonPrime(numbersList):
    print("Prime numbers from list : ",end=" ")
    for j in numbersList:
        for i in range(1,(j//2)+1):
            if( j == 1 or (j%i == 0 and i!=1 and i!=j)):
                print(j,end=" ")
                break
    print() 

def checkPrime(numbersList):
    print("Non Prime numbers from list : ",end=" ")
    for j in numbersList:
        prime = True
        for i in range(1,(j//2)+1):
            if( j == 1 or (j%i == 0 and i!=1 and i!=j)):
                prime = False
        if prime:
            print(j,end=" ")

    print()  

def main():
    """Design a Python application that creates two threads named Prime and NonPrime.
• Both threads should accept a list of integers.
• The Prime thread should display all prime numbers from the list.
• The NonPrime thread should display all non-prime numbers from the list."""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    values = acceptNumbersList.acceptListOfNumbers()
    if len(values)==0:
        return
    
    primeThread = threading.Thread(target=checkPrime,args=(values,))
    nonPrimeThread = threading.Thread(target=checkNonPrime,args=(values,))

    primeThread.start()
    nonPrimeThread.start()

    primeThread.join()
    nonPrimeThread.join()

if __name__ == "__main__":
    main()

