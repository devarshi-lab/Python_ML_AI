from functools import reduce

# def checkEven(No):
    # return No % 2 == 0
checkEven = lambda No : (No % 2 == 0)

# def increment(No):
#     return No+1

increment = lambda No : (No+1)


# def add(a,b):
#     return a+b
add = lambda a,b : a+b
def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)
    
    Fdata = list(filter(checkEven,Data))
    print("Data after filter : ",Fdata)

    Mdata = list(map(increment,Fdata))
    print("Data after map : ",Mdata)

    Rdata = int(reduce(add,Mdata))
    print("Data after reduce : ",Rdata)

    


if __name__ == "__main__" :
    main()