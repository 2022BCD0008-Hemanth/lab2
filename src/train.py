import json, joblib, pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score

ROLL_NO = "2022BCD0008_hemanth"
MODEL_NAME = "Ridge Regression (alpha=1.0) + Standardization + Corr-FS"

df = pd.read_csv("data/winequality-red.csv")
df.columns = df.columns.str.strip()

corr = df.corr()["quality"].abs()
selected = corr[corr > 0.2].index.drop("quality")

X = df[selected]
y = df["quality"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = Ridge(alpha=1.0)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Roll No:", ROLL_NO)
print("Model:", MODEL_NAME)
print("MSE:", mse)
print("R²:", r2)

joblib.dump(model, "outputs/model.pkl")

json.dump({
    "roll_no": ROLL_NO,
    "model": MODEL_NAME,
    "selected_features": list(selected),
    "mse": mse,
    "r2_score": r2
}, open("outputs/results.json", "w"), indent=4)
