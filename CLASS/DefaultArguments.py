
def EmployeeInfo(Name,Age,Salary,City = "Pune"):
    print("Name : ", Name)
    print("Age : ", Age)
    print("Salary : ", Salary)
    print("City : ", City)

def main():
    EmployeeInfo("Devarshi",26,200.50) # Correct
    EmployeeInfo("Devarshi",26,200.50,"Mumbai") # Correct
    

if __name__ == "__main__":
    main()