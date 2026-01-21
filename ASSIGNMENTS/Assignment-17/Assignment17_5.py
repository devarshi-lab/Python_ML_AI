def isPrime(no):  
    prime = True
    for i in range(1,(no//2)+1):
        if( no%i == 0 and i!=1 and i!=no):
            prime = False
            break
    
    return prime

def main():
    """5.Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    num = int(input("Enter a number : "))
    if(isPrime(num)):
        print("It is a prime number")
    else:
        print("It is not a prime number")



if __name__ == "__main__":
    main()