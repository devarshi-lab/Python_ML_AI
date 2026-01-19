# Write a program which accepts one number and checks whether it is perfect number or
# not.

# Input: 6
# Output: Perfect Number

def perfect(no):
    sum = 0
    for i in range(1,no):
        if(no % i == 0):
            sum += i
    if no == sum:
        return True
    return False

def main():
    no = int(input("Enter number : "))
    per = perfect(no)
    if(per):
        print(no," is perfect number")
    else:
        print(no," is not perfect number")

if __name__ == "__main__":
    main()