#  Write a program which accepts one number and prints all even numbers till that
# number.

# Input: 10
# Output: 2 4 6 8 10

def evenRange(no):
    even = list()
    for i in range(1,no+1):
        if(i % 2 == 0):
            even.append(i)
    return even

def main():
    no = int(input("Enter the number : "))
    ret = evenRange(no)
    print("Even number till  ",no," is : ",ret)

if __name__ == "__main__":
    main()