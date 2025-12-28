import pandas as pd

#load dataset
data=pd.read_csv("../data/students.csv")

print("Dataset preview:")
print(data.head())

print("\nDataset information:")
print(data.info())

print("\nStatistical summary:")
print(data.describe())