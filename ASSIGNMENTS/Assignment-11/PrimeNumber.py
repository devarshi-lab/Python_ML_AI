# Write a program which accepts one number and checks whether it is prime or not.

# Input: 11
# Output: Prime Number

def isPrime(no):
    prime = True
    for i in range(1,no+1):
        if( no%i == 0 and i!=1 and i!=no):
            prime = False
            break
    
    return prime
     
def main():
    no = int(input("Enter the number : "))
    ret = isPrime(no)
    if(ret):
        print(no," is prime number")
    else:
        print(no, " is not prime number")

if __name__ == "__main__":
    main()