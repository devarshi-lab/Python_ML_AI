import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def loadDataset(filePath):
    try:
        dataset = pd.read_csv(filePath)
        return dataset
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return None
    
def main():
    dataset = loadDataset("PlayPredictor.csv")
    if dataset is not None:
        print(dataset.head())
    
    X = dataset[list(dataset.columns)[1:3]]  # Selecting the first two columns as features
    y = dataset["Play"]

    print("\nFeatures (X):")
    print(X.head()) 
    print("\nTarget (y):")
    print(y.head()) 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    le = LabelEncoder()
    for x in X_train.columns:
        X_train[x] = le.fit_transform(X_train[x])
        X_test[x] = le.fit_transform(X_test[x])

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\nPredicted values:", y_pred)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nAccuracy of KNN Classifier: {accuracy:.2f}")


    

if __name__ == "__main__":
    main()