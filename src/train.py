import json
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------------
# Metadata
# -------------------------------
ROLL_NO = "2022BCD0008_hemanth"
MODEL_NAME = "Linear Regression"

# -------------------------------
# Load Dataset (Comma-separated)
# -------------------------------
df = pd.read_csv("data/winequality-red.csv")

# Features & Target
X = df.drop("quality", axis=1)
y = df["quality"]

# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Model Training
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------------
# Prediction & Evaluation
# -------------------------------
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# -------------------------------
# Print Metrics (Logs)
# -------------------------------
print("Roll No:", ROLL_NO)
print("Model:", MODEL_NAME)
print("Mean Squared Error (MSE):", mse)
print("R2 Score:", r2)
print("Accuracy: N/A (Regression task)")

# -------------------------------
# Save Trained Model
# -------------------------------
joblib.dump(model, "outputs/model.pkl")

# -------------------------------
# Save Metrics to JSON
# -------------------------------
results = {
    "roll_no": ROLL_NO,
    "model": MODEL_NAME,
    "mse": mse,
    "r2_score": r2,
    "accuracy": "N/A (Regression task)"
}

with open("outputs/results.json", "w") as f:
    json.dump(results, f, indent=4)
