def Multiplication(a,b):
 ans = 0
 ans = a*b
 return ans

def main():
    no1=0
    no2=0
    ans=0
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    ans = Multiplication(no1,no2)
    print("multiplication is : ",ans)

#starter
if __name__ == "__main__":
    main()
