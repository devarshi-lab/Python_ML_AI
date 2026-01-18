# Write a program which accepts one number and checks whether it is palindrome or not.

# Input: 121
# Output: Palindrome

def palindrome(no):
    original = no
    reversenumber = ""
    while(no>0):
        reversenumber = reversenumber + str((no % 10))
        no = int(no / 10)
    if(original == int(reversenumber)):
        return True
    return False


def main():
    no = int(input("Enter the number : "))
    pali = palindrome(no)
    if(pali):
        print(no ," is Palindrome number")
    else:
        print(no, " is not palindrome number")
if __name__ == "__main__":
    main()