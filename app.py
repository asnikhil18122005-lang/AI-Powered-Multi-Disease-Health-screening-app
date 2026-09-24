import joblib
import os

MODEL_DIR = "models"

MODEL_FILES = {
    "Diabetes": "diabetes_model.joblib",
    "Heart Disease": "heart_disease_model.joblib",
    "Kidney Disease": "kidney_disease_model.joblib",
    "Liver Disease": "liver_disease_model.joblib",
    "Stroke": "stroke_disease_model.joblib",
    "Parkinson's": "parkinsons_model.joblib",
    "Breast Cancer": "breast_cancer_model.joblib",
    "Thyroid": "thyroid_model.joblib",
    "Lung Cancer": "lung_cancer_model.joblib",
    "Alzheimer's": "alzheimers_model.joblib"
}

models = {}

for disease, filename in MODEL_FILES.items():
    path = os.path.join(MODEL_DIR, filename)

    if os.path.exists(path):
        models[disease] = joblib.load(path)

print("Models loaded:", list(models.keys()))
