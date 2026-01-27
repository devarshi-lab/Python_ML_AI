class Arithmatic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self,no1,no2):
        self.Value1 = no1
        self.Value2 = no2
    
    def Addition(self):
        return self.Value1 + self.Value2
    def Subtraction(self):
        return self.Value1 - self.Value2
    def Multiplication(self):
        return self.Value1 * self.Value2
    def Division(self):
        return self.Value1 / self.Value2 if self.Value2 != 0 else "error"
    
def main():

    Aobj1 = Arithmatic()
    Aobj1.Accept(5,2)
    print("Addition of 5 and 2 is : ",Aobj1.Addition())
    print("Subtraction of 5 and 2 is : ",Aobj1.Subtraction())
    print("Multiplication of 5 and 2 is : ",Aobj1.Multiplication())
    print("Division of 5 and 2 is : ",Aobj1.Division())
    print("*"*50)
    Aobj2 = Arithmatic()
    Aobj2.Accept(15,0)
    print("Addition of 15 and 0 is : ",Aobj2.Addition())
    print("Subtraction of 15 and 0 is : ",Aobj2.Subtraction())
    print("Multiplication of 15 and 0 is : ",Aobj2.Multiplication())
    print("Division of 15 and 0 is : ",Aobj2.Division())
    print("*"*50)
    Aobj3 = Arithmatic()
    Aobj3.Accept(78,54)
    print("Addition of 75 and 54 is : ",Aobj3.Addition())
    print("Subtraction of 75 and 54 is : ",Aobj3.Subtraction())
    print("Multiplication of 75 and 54 is : ",Aobj3.Multiplication())
    print("Division of 75 and 54 is : ",Aobj3.Division())
    print("*"*50)
    Aobj4 = Arithmatic()
    Aobj4.Accept(45,95)
    print("Addition of 45 and 95 is : ",Aobj4.Addition())
    print("Subtraction of 45 and 95 is : ",Aobj4.Subtraction())
    print("Multiplication of 45 and 95 is : ",Aobj4.Multiplication())
    print("Division of 45 and 95 is : ",Aobj4.Division())
    print("*"*50)
        

if __name__ == "__main__":
    main()

