import joblib
import numpy as np

from src.preprocessing import clean_resume
from src.pdf_parser import extract_text_from_pdf
from src.resume_analyzer import analyze_resume


# Load Pipeline
pipeline = joblib.load(
    "artifacts/resume_classifier.pkl"
)


def predict_resume_category(pdf_path: str):

    # Extract text
    text = extract_text_from_pdf(pdf_path)

    # Analyze ORIGINAL resume
    analysis = analyze_resume(text)

    # Clean text
    cleaned_text = clean_resume(text)

    # Prediction
    prediction = pipeline.predict(
        [cleaned_text]
    )[0]

    # Top matches
    scores = pipeline.decision_function(
        [cleaned_text]
    )[0]

    exp_scores = np.exp(scores - np.max(scores))

    probabilities = exp_scores / exp_scores.sum()

    classes = pipeline.classes_

    top_indices = np.argsort(
        probabilities
    )[::-1][:3]

    top_matches = []

    for idx in top_indices:

        top_matches.append(
            classes[idx]
        )

    return prediction, top_matches, analysis