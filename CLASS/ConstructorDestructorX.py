import gc

class demo:
    def __init__(self):
        print("Inside constructor")
    
    def __del__(self):
        print("Inside destructor")
    

obj1 = demo()
obj2 = demo()

del obj1
del obj2

gc.collect()

print("End of application")