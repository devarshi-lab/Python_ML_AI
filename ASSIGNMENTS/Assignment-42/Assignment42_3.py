from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def main():
    dataset = [
        {"Experience": 1, "Salary": 20000},
        {"Experience": 2, "Salary": 25000},
        {"Experience": 3, "Salary": 30000},
        {"Experience": 4, "Salary": 35000},
        {"Experience": 5, "Salary": 40000},
    ]

    model = LinearRegression()
    X = [[data["Experience"]] for data in dataset]
    Y = [data["Salary"] for data in dataset]

    model.fit(X, Y)
    predSalary = model.predict([[6]])
    print("Predicted Salary for 6 years of experience: ", predSalary[0])

    plt.figure(figsize=(10, 6))
    plt.scatter(X, Y, color='blue', label='Actual Salary')
    plt.plot(X,Y, color='red', label='Regression Line')
    plt.title('Experience vs Salary')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.grid()
    plt.show()




if __name__ == "__main__":
    main()