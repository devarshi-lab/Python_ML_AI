#  Write a program which accepts marks and displays grade.

# Condition Example:

# ≥ 75 -> Distinction

# ≥ 60 -+ First Class

# ≥ 50 -+ Second Class

# <50 -+ Fail

def Grade(marks):
    if(marks>100):
        return "Invalid Percentage"
    elif(marks>=75):
        return "Distinction"
    elif(marks>=60):
        return "First Class"
    elif(marks>=50):
        return "Second Class"
    elif(marks<50):
        return "Fail"

def main():
    mark = int(input("Enter percentage : "))
    gradeDesc = Grade(mark)
    print("Grade is : ",gradeDesc)

if __name__ == "__main__":
    main()
  