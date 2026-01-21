# Write a lambda function using filter () which accepts a list of strings and returns a list of strings having length greater than 5.

lengthGreaterThan5 = lambda str : len(str)>5

def main():
    value = []
    limit = int(input("Enter no. of elements : "))
    print("Enter ", limit, " elements : ")
    for i in range(limit):
        value.append((input()))
    even = list(filter(lengthGreaterThan5,value))
    print("Strings whose length is greater than 5  : ",even)

if __name__ == "__main__":
    main()