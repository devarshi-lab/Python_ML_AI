# Write a program which accepts one number and prints that many numbers in reverse
# order.

# Input: 5
# Output: 5 4 3 2 1

def printReversRange(no):
    elements = list()
    for i in range(no,0,-1):
        elements.append(i)
    return elements

def main():
    no = int(input("Enter number : "))
    numRange = printReversRange(no)
    print(numRange)

if __name__ == "__main__":
    main()