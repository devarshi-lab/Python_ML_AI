def acceptListOfNumbers():
    values = []
    try:
        limit = int(input("Enter no. of elements : "))
        print("Enter ",limit," elements : ")
        for i in range(limit):
            values.append(int(input()))
    except ValueError:
        values = []
        print("Invalid Input. Only numbers are allowed")
    return values
