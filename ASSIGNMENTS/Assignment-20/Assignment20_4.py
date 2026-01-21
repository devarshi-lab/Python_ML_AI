import threading

def capitalCount(value):
    print("Capital Thread Id : ",threading.get_ident())
    print("Capital Thread Name : ",threading.current_thread().name)
    count = 0
    for i in (value):
        if(i>='A' and i<="Z"):
            count += 1
    print(" Capital letter characters count is : ",count)
def smallCount(value):
    print("Small Thread Id : ",threading.get_ident())
    print("Small Thread Name : ",threading.current_thread().name)
    count = 0
    for i in (value):
        if(i>='a' and i<="z"):
            count += 1
    print(" Small letter characters count is : ",count)
def digitCount(value):
    print("Digit Thread Id : ",threading.get_ident())
    print("Digit Thread Name : ",threading.current_thread().name)
    count = 0
    for i in (value):
        try:
            if(int(i) and int(i)>=0 and int(i)<=9):
                count += 1
        except ValueError:
            continue
    print(" Digit count is : ",count)

    

def main():
    """Design a Python application that creates three threads named Small, Capital, and Digits.
    • All threads should accept a string as input.
    • The Small thread should count and display the number of lowercase characters.
    • The Capital thread should count and display the number of uppercase characters.
    • The Digits thread should count and display the number of numeric digits.
    • Each thread must also display:
    ◦ Thread ID
    ◦ Thread Name"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    str = (input("Enter a string : "))
    
    capitalThread = threading.Thread(target=capitalCount,args=(str,))
    smallThread = threading.Thread(target=smallCount,args=(str,))
    digitThread = threading.Thread(target=digitCount,args=(str,))

    capitalThread.start()
    smallThread.start()
    digitThread.start()

    capitalThread.join()
    smallThread.join()
    digitThread.join()
    print("Exit from main")

if __name__ == "__main__":
    main()
    