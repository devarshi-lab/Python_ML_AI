from functools import reduce
import acceptNumbersList

def main():
    """4.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
    List contains the numbers which are accepted from user. Filter should filter out all such numbers which are even. 
    Map function will calculate its square. Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    values = acceptNumbersList.acceptListOfNumbers()
    if len(values)==0:
        return
    filtered = list(filter((lambda no:no%2 == 0),values))
    print("List after filter : ",filtered)
    mapped = list(map((lambda no:no*no),filtered))
    print("List after map : ",mapped)
    result = reduce((lambda no1,no2:no1+no2),mapped)
    print("Result is : ",result)

if __name__ == "__main__":
    main()


