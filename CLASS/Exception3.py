def main():
    try:
        print("Inside Try")
        Ans = 0
        no1 = int(input("Enter first number : "))
        no2 = int(input("Enter second number : "))
        Ans = no1 / no2
    except ZeroDivisionError as zobj:
        print("Inside Except : " ,zobj)
    except ValueError as vobj:
        print("Inside Except : " ,vobj) 
    except Exception as eobj:
        print("Inside except : ",eobj)   
    finally:
        print("Inside finally")

    
    print("Division is : ",Ans)

if __name__ == "__main__":
    main()