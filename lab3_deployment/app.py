from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Load trained model
model = joblib.load("model.pkl")

app = FastAPI(
    title="Wine Quality Prediction API",
    description="ML Model Deployment using FastAPI and Docker",
    version="1.0"
)

# Input schema
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
    
@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/predict")
def predict_wine_quality(data: WineFeatures):
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

    prediction = model.predict(features)[0]

    return {
        "name": "Hemanth",
        "roll_no": "2022BCD0008",
        "wine_quality": int(round(prediction))
    }
