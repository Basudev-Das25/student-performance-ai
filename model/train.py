import pandas as pd
from sklearn.model_selection import train_test_split

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

print("Training feature shape:", X_train.shape)
print("Testing feature shape:", X_test.shape)
print("Training feature shape:", Y_train.shape)
print("Testing feature shape:", Y_test.shape)