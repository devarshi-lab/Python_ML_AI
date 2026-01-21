def getFrequency(numList,num):
    count = 0
    for i in numList:
        if i == num:
            count += 1
    return count

def main():
    """4.Write a program which accept N numbers from user and store it into List.Accept one another number from user and return frequency of that number from List.
        Input : Number of elements : 11
        Input Elements : 13 5 45 7 4 56 5 34 2 5 65
        Element to search : 5
        Output : 3"""
    elements = []
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    limit = int(input("Enter number of elements : "))
    for i in range(limit):
        elements.append(int(input()))
    no = int(input("Elements to search  : "))
    print("Frequency of number is : ",getFrequency(elements,no))

if __name__ == "__main__":
    main()
