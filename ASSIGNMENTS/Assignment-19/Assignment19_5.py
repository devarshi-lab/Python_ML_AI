from functools import reduce
import acceptNumbersList

def checkPrime(no):
    prime = True
    for i in range(1,(no//2)+1):
        if( no == 1 or (no%i == 0 and i!=1 and i!=no)):
            prime = False
            break
    return prime    

def main():
    """5.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter should filter out all prime numbers. 
Map function will multiply each number by 2.
Reduce will return Maximum number from that numbers. (You can also use normal functions instead of lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    values = acceptNumbersList.acceptListOfNumbers()
    if len(values)==0:
        return
    filtered = list(filter(checkPrime,values))
    print("List after filter : ",filtered)
    mapped = list(map((lambda no:no*2),filtered))
    print("List after map : ",mapped)
    result = reduce((lambda no1,no2:no1 if no1>no2 else no2),mapped)
    print("Result is : ",result)

if __name__ == "__main__":
    main()


