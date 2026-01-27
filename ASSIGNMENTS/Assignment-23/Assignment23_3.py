class Numbers:
    def __init__(self,value):
        self.Value = value
    
    def isPrime(self):
        no = self.Value
        prime = True
        for i in range(1,no+1):
            if( no%i == 0 and i!=1 and i!=no):
                prime = False
                break
        return prime
    
    def checkPerfect(self):
        no = self.Value
        sum = self.SumFactors()
        if no==sum:
            return True
        return False
    
    def Factors(self):
        no = self.Value
        factarray = list()
        factarray.append(1)
        for i in range(2,(no//2)+1):
            if(no % i == 0):
                factarray.append(i)
        return factarray
    
    def SumFactors(self):
        no =self.Value
        sum = 0
        for i in self.Factors():
            sum += i
        return sum

def main():
    numObj1 = Numbers(50)
    numObj2 = Numbers(148)
    numObj3 = Numbers(356)
    numObj4 = Numbers(11)
    numObj5 = Numbers(6)
    
    print("Number : ",50)
    print(f"Prime Number :",numObj1.isPrime())
    print(f"Perfect Number :",numObj1.checkPerfect())
    print(f"Factors of Number :",numObj1.Factors())
    print(f"Sum of factors of Number :",numObj1.SumFactors())
    print("-"*50)
    
    print("Number : ",148)
    print(f"Prime Number :",numObj2.isPrime())
    print(f"Perfect Number :",numObj2.checkPerfect())
    print(f"Factors of Number :",numObj2.Factors())
    print(f"Sum of factors of Number :",numObj2.SumFactors())
    print("-"*50)

    print("Number : ",356)
    print(f"Prime Number :",numObj3.isPrime())
    print(f"Perfect Number :",numObj3.checkPerfect())
    print(f"Factors of Number :",numObj3.Factors())
    print(f"Sum of factors of Number :",numObj3.SumFactors())
    print("-"*50)

    print("Number : ",11)
    print(f"Prime Number :",numObj4.isPrime())
    print(f"Perfect Number :",numObj4.checkPerfect())
    print(f"Factors of Number :",numObj4.Factors())
    print(f"Sum of factors of Number :",numObj4.SumFactors())
    print("-"*50)

    print("Number : ",6)
    print(f"Prime Number :",numObj5.isPrime())
    print(f"Perfect Number :",numObj5.checkPerfect())
    print(f"Factors of Number :",numObj5.Factors())
    print(f"Sum of factors of Number :",numObj5.SumFactors())
    print("-"*50)


if __name__ == "__main__":
    main()