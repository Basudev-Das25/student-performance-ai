import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

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

#Predict on test data
Y_pred=model.predict(X_test)

#Evaluation
mse= mean_squared_error(Y_test, Y_pred)

print("Model trained successfully.")
print("Mean Squared Error (MSE):", mse)

# print("\nActual vs Predicted:")
# for actual, predicted in zip(Y_test, Y_pred):
#     print(f"Actual: {actual}, Predicted: {round(predicted, 2)}")

# sample_input=pd.DataFrame(
#     [[6, 85, 75]],
#     columns=["hours_studied", "attendance", "previous_score"]
# )
# sample_predicition= model.predict(sample_input)

# print("\nSample Prediction for input [6, 85, 75]:", round(sample_predicition[0], 2))

#save the trained model
with open("../app/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as model.pkl")