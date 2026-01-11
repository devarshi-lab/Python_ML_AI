checkEven = lambda No : (No % 2 == 0)
increment = lambda No : (No+1)
add = lambda a,b : a+b

def filterX(function,data):
    result = list()
    for i in data:
        if function(i):
            result.append(i)
    return result

def mapX(function,data):
    result = list()
    for i in data:
        no = increment(i)
        result.append(no)
    return result

def reduceX(function,data):
    result = 0
    for i in data:
        result = function(result,i)
    return result

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)
    
    Fdata = (filterX(checkEven,Data))
    print("Data after filter : ",Fdata)

    Mdata = list(mapX(increment,Fdata))
    print("Data after map : ",Mdata)

    Rdata = int(reduceX(add,Mdata))
    print("Data after reduce : ",Rdata)

if __name__ == "__main__" :
    main()