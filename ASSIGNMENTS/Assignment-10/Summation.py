# Write a program which accepts one number and prints sum of first N natural numbers.

# Input: 5
# Output: 15

def summation(no):
    sum = 0
    for i in range(no+1):
        sum += i
    return sum

def main():
    no = int(input("Enter the number : "))
    ret = summation(no)
    print("Summation of number is ",ret)

if __name__ == "__main__":
    main()