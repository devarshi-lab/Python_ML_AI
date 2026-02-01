import gc

class demo:
    # class variable
    no1 = 10
    no2 = 11
    def __init__(self):
        print("Inside constructor")
    
    def __del__(self):
        print("Inside destructor")
    
print(demo.no1)
print(demo.no2)



print("End of application")