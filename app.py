# 1) Import Libraries
from flask import Flask, render_template, request
import os

from src.predictor import predict_resume_category


import sys

print("Python executable:")
print(sys.executable)

import nltk
print("NLTK version:", nltk.__version__)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

# 2) Home Route
@app.route("/")
def home():

    return render_template(
        "index.html"
    )

# 3) Upload Route
@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    # 4) Receive Uploaded PDF
    file = request.files["resume"]

    # 5) Save Uploaded File
    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        file.filename
    )

    file.save(filepath)

    # 6) Predict
    prediction, top_matches, analysis = predict_resume_category(
        filepath
    )

    # 7) Send Results to HTML
    return render_template(
        "index.html",
        prediction=prediction,
        top_matches=top_matches,
        analysis=analysis
    )


# 8) Run Flask
if __name__ == "__main__":

    app.run(debug=True)



