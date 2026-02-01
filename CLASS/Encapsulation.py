class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        print("Object gets created successfully")

    def addition(self):
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def subtraction(self):
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans

obj1 = Arithmatic(11,10)    # Arithmatic(id(obj1),11,10)    -> __init__(id(obj1),11,10)
obj2 = Arithmatic(21,20)    # Arithmatic(id(obj2),21,20)    -> __init__(id(obj2),21,20)

Ret = obj1.addition()       # Addition(id(obj1))    -> Addition(1000)
print(Ret)  #21

Ret = obj2.subtraction()    # # Addition(id(obj2))    -> Addition(2000)
print(Ret)  #1
    