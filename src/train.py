import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score

ROLL_NO = "2022BCD0008_hemanth"
MODEL_NAME = "Decision Tree Regressor (max_depth=10)"
 
df = pd.read_csv("data/winequality-red.csv")

X = df.drop("quality", axis=1)
y = df["quality"]
 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = DecisionTreeRegressor(max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Logs (NO accuracy)
print("Roll No:", ROLL_NO)
print("Model:", MODEL_NAME)
print("MSE:", mse)
print("R²:", r2)
 
joblib.dump(model, "outputs/model.pkl")
 
results = {
    "roll_no": ROLL_NO,
    "model": MODEL_NAME,
    "mse": mse,
    "r2_score": r2
}

with open("outputs/results.json", "w") as f:
    json.dump(results, f, indent=4)
