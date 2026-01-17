# Write a program which accepts one number and prints factorial of that number.

# Input: 5
# Output: 120

def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact *= i
    return fact

def main():
    no = int(input("Enter the number : "))
    ret = factorial(no)
    print("Factorial of ",no," is : ",ret)

if __name__ == "__main__":
    main()