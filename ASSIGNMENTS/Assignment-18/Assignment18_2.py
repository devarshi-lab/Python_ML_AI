def maxNumber(numList):
    max = numList[0]
    for i in numList:
        if i>max:
            max = i
    return max

def main():
    """2.Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56"""
    elements = []
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    limit = int(input("Enter number of elements : "))
    for i in range(limit):
        elements.append(int(input()))
    print("Maximum number is : ",maxNumber(elements))

if __name__ == "__main__":
    main()
