
import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import (accuracy_score,confusion_matrix,classification_report,ConfusionMatrixDisplay)

border = "-"*50
###################################################################################################################
# Step 1 : Load the dataset
###################################################################################################################
print(border)
print("Step 1 : Load the Dataset")
print(border)

datasetPath = "iris.csv"
df = pd.read_csv(datasetPath)
print("Dataset gets loaded successfully")
print("Initial entries from dataset : ")
print(df.head())

###################################################################################################################
# Step 2 : Data Analysis (EDA) Exploratory Data Analysis
###################################################################################################################
print(border)
print("Step 2 : Data Analysis")
print(border)

print("Shape of dataset : ",df.shape)
print("Column Names : ",list(df.columns))
print("Missing Values (Per Column) : ")
print(df.isnull().sum())
print("Class distribution (Species Count)")
print(df["species"].value_counts())

print("Statistical Report of Dataser")
print(df.describe())

###################################################################################################################
# Step 3 : Decide Independent and dependent variables
###################################################################################################################

print(border)
print("Step 3 : Decide Independent and dependent variables")
print(border)

# X = Independent Variables or Features
# Y = Dependent variables or Labels

features_cols = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
X = df[features_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

###################################################################################################################
# Step 4 : Visualisation of dataset
###################################################################################################################

print(border)
print("Step 4 : Visualisation of dataset")
print(border)

# Scatter plot

plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"],temp["petal width (cm)"],label = sp)

plt.title("IRIS : Petal Length vs Petal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend()
plt.grid(True)
plt.show()

###################################################################################################################
# Step 5 : Split the dataset fir training and testing
###################################################################################################################

print(border)
print("Step 5 : Split the dataset fir training and testing")
print(border)

# Test size = 20%
# Train Size = 80%

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Data splitting activity done.")
print("X - Independent : ",X.shape) # (150 , 4)
print("Y - Dependent : ",Y.shape)   # (150,)

print("X_train : ",X_train.shape)   # (120 , 4)
print("X_test : ",X_test.shape)     # (30 , 4)

print("Y_train : ",Y_train.shape)   # (120,)
print("Y_test : ",Y_test.shape)     # (30,)

###################################################################################################################
# Step 6 : Build the model
###################################################################################################################

print(border)
print("Step 6 : Build the model")
print(border)

print("We are going to use DecisionTreeClassifier")

model = DecisionTreeClassifier(criterion="gini",max_depth=5,random_state=42)

print("Model successfully created")
print(model)

###################################################################################################################
# Step 7 : Train the model
###################################################################################################################

print(border)
print("Step 7 : Train the model")
print(border)

model.fit(X_train,Y_train)

print("Model Training Completed")

###################################################################################################################
# Step 8 : Evaluate the model
###################################################################################################################

print(border)
print("Step 8 : Evaluate the model")
print(border)

Y_pred = model.predict(X_test)

print("Model Evaluation (Testing) complete")

print("Shape of Y_pred : ",Y_pred.shape)

print("Expected Answers")
print(list(Y_test))

print("Predicted Answers")
print(Y_pred)

###################################################################################################################
# Step 9 : Evaluate the model performance
###################################################################################################################

print(border)
print("Step 9 : Evaluate the model performance")
print(border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is : ",accuracy*100)

cm = confusion_matrix(Y_test,Y_pred)

print("Confusion Matrix : ")
print(cm)

print("Classification Report")
print(classification_report(Y_test,Y_pred))