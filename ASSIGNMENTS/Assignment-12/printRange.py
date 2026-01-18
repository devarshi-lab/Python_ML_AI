# Write a program which accepts one number and prints that many numbers starting
# from 1.

# Input: 5
# Output: 1 2 3 4 5

def printRange(no):
    elements = list()
    for i in range(1,no+1):
        elements.append(i)
    return elements

def main():
    no = int(input("Enter number : "))
    numRange = printRange(no)
    print(numRange)

if __name__ == "__main__":
    main()