from functools import reduce
import acceptNumbersList

def main():
    """3.Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. List contains the numbers which are accepted
from user. Filter should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    values = acceptNumbersList.acceptListOfNumbers()
    if len(values)==0:
        return
    filtered = list(filter((lambda no:no>=70 and no<=90),values))
    print("List after filter : ",filtered)
    mapped = list(map((lambda no:no+10),filtered))
    print("List after map : ",mapped)
    result = reduce((lambda no1,no2:no1*no2),mapped)
    print("Result is : ",result)

if __name__ == "__main__":
    main()


