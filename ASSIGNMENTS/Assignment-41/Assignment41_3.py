import math
from sklearn.neighbors import KNeighborsClassifier

def main():
    Dataset = [(2,60),(5,80),(6,85),(1,50)]
    Label = ["Fail","Pass","Pass","Fail"]

    studyHours = float(input("Enter the Study Hours : "))
    attendance = float(input("Enter the Attendance : "))

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(Dataset, Label)
    predicted_label = model.predict([[studyHours, attendance]])
    print("Predicted Result : ", predicted_label[0])

if __name__ == "__main__":
    main()