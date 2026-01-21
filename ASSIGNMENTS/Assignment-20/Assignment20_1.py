import threading

def even(no):
    for i in range(2,(no*2)+1,2):
        print("Even : ",i)

def odd(no):
    for i in range(1,no*2,2):
        print("Odd : ",i)

def main():
    """Design a Python application that creates two separate threads named Even and Odd.
• The Even thread should display the first 10 even numbers.
• The Odd thread should display the first 10 odd numbers.
• Both threads should execute independently using the threading module.
• Ensure proper thread creation and execution."""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    evenThread = threading.Thread(target=even,args=(10,))
    oddThread = threading.Thread(target=odd,args=(10,))

    evenThread.start()
    oddThread.start()

    evenThread.join()
    oddThread.join()

if __name__ == "__main__":
    main()
    