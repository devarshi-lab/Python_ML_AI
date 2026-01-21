def summation(numList):
    sum = 0
    for i in numList:
        sum += i
    return sum

def main():
    """1.Write a program which accept N numbers from user and store it into List. Return addition of all  elements from that List.
    Input : Number of elements : 6
    Input Elements : 13 5 45 7 4 56
    Output : 130"""
    elements = []
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    limit = int(input("Enter number of elements : "))
    for i in range(limit):
        elements.append(int(input()))
    print("Sum of all numbers is : ",summation(elements))

if __name__ == "__main__":
    main()
