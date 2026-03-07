import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

def loadDataset(filePath):
    try:
        dataset = pd.read_csv(filePath)
        return dataset
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return None
    
def main():
    dataset = loadDataset("Advertising.csv")
    if dataset is not None:
        print(dataset.head())
    
    X = dataset[list(dataset.columns)[1:4]]  # Selecting the first three columns as features
    y = dataset["sales"]

    print("\nFeatures (X):")
    print(X.head()) 
    print("\nTarget (y):")
    print(y.head()) 

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print("\nPredicted values:", y_pred)
    accuracy = model.score(X_test, y_test)
    print(f"\nAccuracy of Linear Regression: {accuracy:.2f}")


    

if __name__ == "__main__":
    main()