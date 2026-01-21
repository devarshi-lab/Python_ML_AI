def sumFactors(no):
    sumfact = 1
    for i in range(2,(no//2)+1):
       if(no%i==0):
           sumfact += i
    return sumfact 

def main():
    """Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter a number : "))
    print("Sum of factors of  ",num," is : ",sumFactors(num))

if __name__ == "__main__":
    main()