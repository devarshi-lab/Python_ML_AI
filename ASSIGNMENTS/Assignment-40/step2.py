import pandas
import matplotlib.pyplot as mt
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)
from sklearn.model_selection import train_test_split

border = "-"*100

def load_csv():
    try:
        # Loading CSV Dataset using pandas stored at secondary storage
        data = pandas.read_csv("student_performance_ml_2.csv")
        print("Top 5 Records")
        print(border)
        print(data.head()) # Reads top 5 records
        print(border)
        print("Last 5 Records")
        print(border)
        print(data.tail()) # Reads last 5 Records
        print(border)
        print("Total rows * col",data.shape) # shows rows and columns
        print(border)
        print("Column Names")
        print(list(data.columns)) # return columns names
        print(border)
        print(data.dtypes)
        print(border)
        return data
    except FileNotFoundError:
        print("No such file or directory: 'student_perfomance_ml.csv'")
    return None

def data_analysis(data):
    print(border)
    print("Total number of students in the dataset : ",len(data)) # return total number of rows
    print(border)
    print("Total number of Passed students in the dataset : ",(data["FinalResult"] == 1).sum()) # return the values where finalresult is 1 and sum function count the total passed
    print("Total number of Failed students in the dataset : ",(data["FinalResult"] == 0).sum())
    print(border)

def calculation_of_data(data):
    print(border)
    print("Average StudyHours : ",data["StudyHours"].mean()) # mean return average of studyhours
    print("Average Attendance : ",data["Attendance"].mean()) 
    print("Maximum PreviousScore : ",data["PreviousScore"].max()) # max return maximum number from previousscore column
    print("Minimum SleepHours : ",data["SleepHours"].min()) # min return minimum number from sleephours

def checkData(data):
    print(border)
    print("Final Result Distibution",data["FinalResult"].value_counts())
    print("Passed students percentage : ", ((((data["FinalResult"]==1).sum())/len(data))*100),"%")
    print("Failed students percentage : ", ((((data["FinalResult"]==0).sum())/len(data))*100),"%")
    print("Data is not balanced as passed percentage is grater than failed percentage")

def corelation(data):
    print(border)
    study = data["StudyHours"].corr(data["FinalResult"]) # correlation between studyhours and finalresult
    attendance = data["Attendance"].corr(data["FinalResult"]) # correlation between attendance and finalresult
    print("Higher study hours passing percentage : ", study)
    print("Higher attedance passing percentage : ",attendance)
    print("""When we correlate between studyhours and finalresult
we get result near +1 which shows that higher study hours increases
the passing probability.""")
    print(border)
    print("""When we correlate between attendance and finalresult
we get result near +1 which shows that higher study hours increases
the passing probability.""")

def histogram(data):
    mt.figure()
    mt.hist(x=data["StudyHours"],bins=8, linewidth=0.5, edgecolor="white") # to plot histogram
    mt.title("Study Hours")
    mt.xlabel("Study Hours")
    mt.ylabel("Frequency")
    mt.show()

def scatterplot(data):
    mt.figure()
    for result in data["FinalResult"].unique():
        temp = data[data["FinalResult"] == result]
        mt.scatter(temp["StudyHours"],temp["PreviousScore"],label="Pass" if result==1 else "Fail")

    mt.title("Students Perfomance : Study Hours vs Previous Score")
    mt.xlabel("Study Hours")
    mt.ylabel("Previous Score")
    mt.legend()
    mt.grid(True)
    mt.show()

def boxplot(data):
    mt.figure()
    mt.boxplot(data["Attendance"])
    mt.title("Boxplot of attendance")
    mt.xlabel("Attendance")
    mt.show()

def correlationplot1(data):
    mt.figure()
    mt.scatter(data[data["FinalResult"] == 0]["FinalResult"], data[data["FinalResult"] == 0]["AssignmentsCompleted"])
    mt.scatter(data[data["FinalResult"] == 1]["FinalResult"], data[data["FinalResult"] == 1]["AssignmentsCompleted"])
    mt.xticks([0, 1], ["Fail", "Pass"])
    mt.xlabel("Final Result")
    mt.ylabel("Assignments Completed")
    mt.title("Assignments Completed vs Final Result")
    mt.show()
    print(border)
    print("""The result of correlation between FinalResult
and AssignmentCompleted shows that - 
1. Students who has solved max assignment has more probability
of getting pass
2. Students who has completed less number of assignment has low probability
of getting pass""")
    
def correlationplot2(data):
    mt.figure()
    mt.scatter(data[data["FinalResult"] == 0]["FinalResult"], data[data["FinalResult"] == 0]["SleepHours"])
    mt.scatter(data[data["FinalResult"] == 1]["FinalResult"], data[data["FinalResult"] == 1]["SleepHours"])
    mt.xticks([0, 1], ["Fail", "Pass"])
    mt.xlabel("Final Result")
    mt.ylabel("Sleep Hours")
    mt.title("Sleep Hours vs Final Result")
    mt.show()
    print(border)
    print("""The result of correlation between FinalResult
and Sleep Hours shows that - 
1. Students who has slept more number of hours upto 8 has more probability
of getting pass
2. Students who has slept less number of hours has low probability
of getting pass""")
    
def train_test_model(data):
    model = DecisionTreeClassifier(max_depth=None)
    X = data[list(data.columns)[:4]]
    Y = data['FinalResult']
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)
    model.fit(X_train,Y_train)

    X_train_pred = model.predict(X_train)
    Y_pred = model.predict(X_test)
    print(border)
    print("Actual Values are : ")
    print(border)
    print(list(Y_test))
    print(border)
    print("Predicted result is : ")
    print(border)
    print(Y_pred)
    print(border)
    print("Testing Accuracy : ")
    calculate_accuracy(X_train_pred,Y_train)
    print(border)
    print("Training Accuracy : ")
    calculate_accuracy(Y_pred,Y_test)
    print(border)
    print("Training accuracy is greater than testing accuracy but not a major difeerence which overrules the overfitting and underfitting")
    print(border)
    calc_confusionmatrix(Y_pred,Y_test)
    return model

def calculate_accuracy(Y_pred,Y_test):
    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy of model is : ",accuracy*100," %")

def calc_confusionmatrix(Y_pred,Y_test):
    print(border)
    conf_matrix = confusion_matrix(Y_test,Y_pred)
    print("confusion matrix is : ")
    print(conf_matrix)
    print("where : ")
    print("Assume - \n1 : Pass : Positive\n2 : Fail : Negative")
    print(conf_matrix[0][0]," : True Negative means student is failed and predicted as failed")
    print(conf_matrix[0][1]," : False Positive means student is failed and predicted as passed")
    print(conf_matrix[1][0]," : False Negative means student is passed and predicted as failed")
    print(conf_matrix[1][1]," : True Positive means students is passed and predicted as passed")

def test_model(model:DecisionTreeClassifier,test_data):
    print(border)
    print("Testing Input : ")
    print(test_data)
    test_pred = model.predict(test_data)
    print(border)
    print("Prediction : ","Pass" if test_pred==1 else 'Fail')

def feature_importance(model:DecisionTreeClassifier):
    print(border)
    print("Feature Importance - ")
    importance_df = pandas.DataFrame({
    "Feature": model.feature_names_in_,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

    print(importance_df)
    print("Prevoius score contributes most for predicting the result")
    print("All others features contributes least for predicting the result")
    print(border)
    print("Even after removing sleep hours column from dataset, accuracy has remain unchanged as it was least contributing feature")

def main():
    data = load_csv()
    if(data is not None):
        # data_analysis(data)
        # calculation_of_data(data)
        # checkData(data)
        # corelation(data)
        # histogram(data)
        # scatterplot(data)
        # boxplot(data)
        # correlationplot1(data)
        # correlationplot2(data)
        model = train_test_model(data)
        test_data = pandas.DataFrame([[6,85,66,7]],columns=[
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
    ])
        test_model(model,test_data)
        feature_importance(model)

if __name__ == "__main__":
    main()