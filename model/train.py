import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#load dataset
data=pd.read_csv("../data/students.csv")

#separate features
X=data[["hours_studied", "attendance", "previous_score"]]
Y=data["final_score"]

#Spli data into testing and training sets
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

#Create and Train the model
model = LinearRegression()
model.fit(X_train, Y_train)

print("Model training completed.")

print("\nLearned Weights:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")

print("\nBias (Intercept):", model.intercept_)