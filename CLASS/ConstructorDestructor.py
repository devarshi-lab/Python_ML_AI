import gc

class demo:
    def __init__(self):
        print("Inside constructor")
    
    def __del__(self):
        print("Inside destructor")
    

obj = demo()

del obj
gc.collect()

print("End of application")