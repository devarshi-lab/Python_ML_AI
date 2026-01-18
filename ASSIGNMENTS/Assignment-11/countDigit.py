# 2.Write a program which accepts one number and prints count of digits in that number.

# Input: 7521
# Output: 4

def countDigits(no):
    count = 0
    # print(len(str(no))) inbuilt
    while(no>0):
        no = int(no / 10)
        count += 1
    return count

def main():
    no = int(input("Enter the number : "))
    count = countDigits(no)
    print("Number of digits are : ",count)

if __name__ == "__main__":
    main()
