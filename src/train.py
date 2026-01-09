import json
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("data/winequality-red.csv", sep=";")
print("Columns in dataset:", df.columns.tolist())
X = df.drop("quality", axis=1)
y = df["quality"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model_name = "Linear Regression"
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print metrics (logs)
print("Roll No: 2022BCD0008_hemanth")
print("Model:", model_name)
print("MSE:", mse)
print("R2 Score:", r2)

# Save model
joblib.dump(model, "outputs/model.pkl")

# Save metrics
results = {
    "roll_no": "2022BCD0008_hemanth",
    "model": model_name,
    "mse": mse,
    "r2_score": r2,
    "accuracy": "N/A (Regression task)"
}

with open("outputs/results.json", "w") as f:
    json.dump(results, f, indent=4)
