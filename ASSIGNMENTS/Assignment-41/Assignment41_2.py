import math
from sklearn.neighbors import KNeighborsClassifier

def main():
    Dataset = [(1, 2), (2, 3), (3, 1), (6, 5), (4, 4)]
    Label = ["Red","Red","Blue","Blue","Blue"]

    inputX = int(input("Enter the value of X : "))
    inputY = int(input("Enter the value of Y : "))

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(Dataset, Label)
    predicted_label = model.predict([[inputX, inputY]])
    print("Predicted Class : ", predicted_label[0])

if __name__ == "__main__":
    main()