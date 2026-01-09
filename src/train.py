import json, joblib, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

ROLL_NO = "2022BCD0008_hemanth"
MODEL_NAME = "Random Forest (50 trees, max_depth=10)"

df = pd.read_csv("data/winequality-red.csv")
X = df.drop("quality", axis=1)
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Roll No:", ROLL_NO)
print("Model:", MODEL_NAME)
print("MSE:", mse)
print("R²:", r2)

joblib.dump(model, "outputs/model.pkl")
json.dump({"roll_no": ROLL_NO, "model": MODEL_NAME, "mse": mse, "r2_score": r2},
          open("outputs/results.json", "w"), indent=4)