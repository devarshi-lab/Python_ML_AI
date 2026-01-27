class Demo:
    value = 100
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
    
    def Fun(self):
        print("Instance Variables are : ",self.No1,self.No2)
    def Gun(self):
         print("Instance Variables are : ",self.No1,self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
