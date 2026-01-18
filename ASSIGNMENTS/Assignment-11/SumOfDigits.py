#  Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6


def sumDigits(no):
    sum = 0
    while(no>0):
        sum = sum + (no % 10)
        no = int(no / 10)
    return sum

def main():
    no = int(input("Enter the number : "))
    count = sumDigits(no)
    print("Sum of digits are : ",count)

if __name__ == "__main__":
    main()