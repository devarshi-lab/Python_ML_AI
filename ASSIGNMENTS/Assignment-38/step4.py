import pandas
import matplotlib.pyplot as mt
import seaborn as sns
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
    return None

def data_analysis(data):
    print(border)
    print("Total number of students in the dataset : ",len(data))
    print(border)
    print("Total number of Passed students in the dataset : ",(data["FinalResult"] == 1).sum())
    print("Total number of Failed students in the dataset : ",(data["FinalResult"] == 0).sum())
    print(border)

def calculation_of_data(data):
    print(border)
    print("Average StudyHours : ",data["StudyHours"].mean())
    print("Average Attendance : ",data["Attendance"].mean())
    print("Maximum PreviousScore : ",data["PreviousScore"].max())
    print("Minimum SleepHours : ",data["SleepHours"].min())

def checkData(data):
    print(border)
    print("Final Result Distibution",data["FinalResult"].value_counts())
    print("Passed students percentage : ", ((((data["FinalResult"]==1).sum())/len(data))*100),"%")
    print("Failed students percentage : ", ((((data["FinalResult"]==0).sum())/len(data))*100),"%")
    print("Data is not balanced as passed percentage is grater than failed percentage")

    mt.figure()
    sns.countplot(x = data["FinalResult"])
    mt.title("Distribution of Final Result to find dataset is balanced.")
    mt.show()
    

def main():
    data = load_csv()
    if(data is not None):
        data_analysis(data)
        calculation_of_data(data)
        checkData(data)

if __name__ == "__main__":
    main()