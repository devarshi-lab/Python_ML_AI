import threading
import acceptNumbersList

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(500000):
        with lock:
            counter += 1    

 

def main():
    """Design a Python application where multiple threads update a shared variable.
    • Use a Lock to avoid race conditions.
    • Each thread should increment the shared counter multiple times.
    • Display the final value of the counter after all threads complete execution."""
    
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    # values = acceptNumbersList.acceptListOfNumbers()
    # if len(values)==0:
        # return
    
    t1 = threading.Thread(target=increment)
    t2 = threading.Thread(target=increment)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Counter value : ",counter)

if __name__ == "__main__":
    main()

