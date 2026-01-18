# Write a program which accepts one character and checks whether it is vowel or
# consonant.

# Input: a
# Output: Vowel

def checkVowel(letter):
    if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or
       letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
        return True
    return False

def main():
    letter = input("Enter a character : ")
    if(len(letter)>1):
        print("Enter single character only")
        return
    isVowel = checkVowel(letter)
    if(isVowel) :
        print("It is a vowel")
    else:
        print("It is not a vowel")

if __name__ == "__main__":
    main()
