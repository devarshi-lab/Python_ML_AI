class demo:
    def __init__(self):
        print("Inside constructor")
    
    def __del__(self):
        print("Inside destructor")
    

obj = demo()

print("End of application")