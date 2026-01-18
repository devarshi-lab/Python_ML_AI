# Write a program which accepts one number and prints reverse of that number.

# Input: 123
# Output: 321


def reverse(no):
    reversenumber = ""
    # print(str(no)[::-1]) InBuilt
    while(no>0):
        reversenumber = reversenumber + str((no % 10))
        no = int(no / 10)
    return int(reversenumber)

def main():
    no = int(input("Enter the number : "))
    count = reverse(no)
    print("Revers Number is : ",count)

if __name__ == "__main__":
    main()