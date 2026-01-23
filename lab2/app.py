from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

model = joblib.load("outputs/model.pkl")
scaler = joblib.load("outputs/scaler.pkl")

app = FastAPI()

class WineFeatures(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.post("/predict")
def predict(data: WineFeatures):
    features = np.array([[  
        data.fixed_acidity,
        data.volatile_acidity,
        data.citric_acid,
        data.residual_sugar,
        data.chlorides,
        data.free_sulfur_dioxide,
        data.total_sulfur_dioxide,
        data.density,
        data.pH,
        data.sulphates,
        data.alcohol
    ]])

    features_scaled = scaler.transform(features)
    pred = model.predict(features_scaled)[0]

    return {
        "name": "Hemanth",
        "roll_no": "2022BCD0008_hemanth",
        "wine_quality": int(round(pred))
    }
