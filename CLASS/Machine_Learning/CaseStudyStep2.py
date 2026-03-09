
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




