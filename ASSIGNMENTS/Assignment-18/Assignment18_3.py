def maxNumber(numList):
    min = numList[0]
    for i in numList:
        if i<min:
            min = i
    return min

def main():
    """3.Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
        Input : Number of elements : 4
        Input Elements : 13 5 45 7
        Output : 5"""
    elements = []
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    limit = int(input("Enter number of elements : "))
    for i in range(limit):
        elements.append(int(input()))
    print("Minimum number is : ",maxNumber(elements))

if __name__ == "__main__":
    main()
