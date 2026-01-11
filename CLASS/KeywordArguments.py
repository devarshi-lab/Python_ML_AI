
def EmployeeInfo(Name,Age,Salary,City):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", Salary)
    print("City : ", City)

def main():
    #Positional
    # EmployeeInfo("Devarshi",26,2000.50,"Pune") # Correct
    # EmployeeInfo(26,"Devarshi","Pune",2000.50) #Wrong

    #Keyword
    EmployeeInfo(Age=26,Name="Devarshi",City="Pune",Salary=2000.50) # Correct
    

if __name__ == "__main__":
    main()