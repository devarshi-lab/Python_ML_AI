import pandas
border = "-"*100

def load_csv():
    try:
        data = pandas.read_csv("student_performance_ml.csv")
        print("Top 5 Records")
        print(border)
        print(data.head())
        print(border)
        print("Last 5 Records")
        print(border)
        print(data.tail())
        print(border)
        print("Total rows * col",data.shape)
        print(border)
        print("Column Names")
        print(list(data.columns))
        print(border)
        print(data.dtypes)
        print(border)
        return data
    except FileNotFoundError:
        print("No such file or directory: 'student_perfomance_ml.csv'")

def main():
    data = load_csv()

if __name__ == "__main__":
    main()