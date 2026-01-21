import Arithmetic

def main():
    print(Arithmetic.__doc__,"\n\n",("-"*50),"\n\n")
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    print("Addition is : ",Arithmetic.Addition(num1,num2))
    print("Subtraction is : ",Arithmetic.Subtraction(num1,num2))
    print("Multiplication is : ",Arithmetic.Multiplication(num1,num2))
    print("Division is : ",Arithmetic.Division(num1,num2))

if __name__ == "__main__":
    main()
