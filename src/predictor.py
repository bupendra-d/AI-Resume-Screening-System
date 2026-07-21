# Imports
import joblib
import numpy as np

from .preprocessing import clean_resume
from .pdf_parser import extract_text_from_pdf
from .resume_analyzer import analyze_resume


# Load the Pipeline
pipeline = joblib.load(
    "artifacts/resume_classifier.pkl"
)


# Build Prediction Function
def predict_resume_category(pdf_path: str):

    # Extract text from PDF
    text = extract_text_from_pdf(pdf_path)

    # Clean resume text
    cleaned_text = clean_resume(text)

    # Analyze original resume
    analysis = analyze_resume(text)

    # Predict category
    prediction = pipeline.predict([cleaned_text])[0]

    # Get decision scores
    scores = pipeline.decision_function([cleaned_text])[0]

    # Class labels
    classes = pipeline.classes_

    # Top 3 matching categories
    top_indices = np.argsort(scores)[::-1][:3]

    top_matches = [
        classes[idx]
        for idx in top_indices
    ]

    return prediction, top_matches, analysis