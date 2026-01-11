from functools import reduce

checkEven = lambda No : (No % 2 == 0)
increment = lambda No : (No+1)
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