import MarvellousNum

def sumPrime(numList):
    sum = 0
    for i in numList:
        if (MarvellousNum.checkPrime(i)):
            sum += i
    return sum

def main():
    """5.Write a program which accept N numbers from user and store it into List.  Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass each  number to ChkPrime() function which is part of our user defined module
named as MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 32 (13 + 5 + 7 +2 + 5)"""
    elements = []
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    limit = int(input("Enter number of elements : "))
    for i in range(limit):
        elements.append(int(input()))
    print("Addition of prime number is : ",sumPrime(elements))

if __name__ == "__main__":
    main()
