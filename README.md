# AI Resume Screening System using NLP

An end-to-end **Natural Language Processing (NLP)** project that automatically classifies resumes into one of **24 professional job categories** using Machine Learning.

The system extracts text from PDF resumes, performs advanced NLP preprocessing, predicts the most suitable job category using a trained **Linear Support Vector Machine (Linear SVM)** model, and provides resume insights such as detected skills, education, experience, email, phone number, GitHub, and LinkedIn profile.

The application is built using **Flask** and deployed on **Render**, with a **Hugging Face Spaces** version planned for interactive demonstrations.



# Live Demo

Experience the deployed application here:

** Live Application:** : https://ai-resume-screening-system-wfen.onrender.com

Note: This application is deployed on Render's free tier. If the app has been inactive for some time, the initial request may take 30–60 seconds to load while the server wakes up.



#  Features

- Upload resumes in PDF format
- Automatic PDF text extraction using PyMuPDF
- Complete NLP preprocessing pipeline
- Resume classification into **24 job categories**
- Displays Top-3 predicted categories
- Resume analyzer including:
  - Skills Detection
  - Education Detection
  - Experience Detection
  - Email Detection
  - Phone Number Detection
  - GitHub Detection
  - LinkedIn Detection
- Clean and responsive Flask web interface
- Deployed using Render



# Project Workflow

1. Resume PDF
2. Extract Text (PyMuPDF) 
3. Text Cleaning & NLP Preprocessing 
4. TF-IDF Vectorization 
5. Linear SVM Classifier 
6. Predicted Resume Category 
7. Resume Analysis 
8. Display Results in Flask App




#  Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Linear Support Vector Machine (Linear SVM)
- TF-IDF Vectorizer

### NLP
- NLTK
- Regular Expressions (Regex)

### PDF Processing
- PyMuPDF

### Deployment
- Flask
- Render

### Future Deployment
- Hugging Face Spaces



#  Dataset

This project uses the **Resume Classification Dataset**, containing **2484 resumes** across **24 different professional categories**.

The dataset includes raw resume text and corresponding job categories.

Due to GitHub file size limitations, the dataset is **not included** in this repository.

### Dataset Link

> **https://www.kaggle.com/datasets/snehaanbhawal/resume-dataset**

After downloading, place the dataset inside: datasets/ before running the notebooks.



# Project Pipeline

This project was developed following a complete end-to-end NLP and Machine Learning workflow, starting from raw resume data to a deployed AI Resume Screening application.

## 1. Dataset Understanding & NLP-EDA

Performed an in-depth exploratory analysis of the resume dataset to understand its structure and quality.
- Inspected dataset dimensions and data types
- Analyzed class distribution across 24 resume categories
- Examined missing values and duplicate records
- Measured character length and word count distributions
- Identified common words and vocabulary size
- Explored token frequency distributions
- Visualized category imbalance and text statistics



## 2. Text Preprocessing

Designed a reusable preprocessing pipeline to clean noisy resume text before feature extraction.

Preprocessing steps included:
- HTML tag removal
- URL removal
- Email removal
- Phone number removal
- Extra whitespace removal
- Lowercase conversion
- Tokenization
- Stopword removal
- Punctuation removal
- Lemmatization

The preprocessing pipeline significantly reduced vocabulary size while preserving meaningful information.



## 3. Feature Engineering

Converted cleaned resume text into numerical features using **TF-IDF Vectorization**.

Experimented with multiple configurations including:
- Different maximum feature sizes
- Unigrams and Bigrams
- Minimum document frequency (`min_df`)
- Maximum document frequency (`max_df`)

The optimal feature representation was selected based on validation performance.



## 4. Machine Learning Model Building

Several machine learning algorithms were trained and compared.

Models evaluated:
- Logistic Regression
- Multinomial Naive Bayes
- Random Forest
- Linear Support Vector Machine (Linear SVM)

Performance was compared using:
- Accuracy
- Precision
- Recall
- F1-Score
- Training Time



## 5. Hyperparameter Tuning

Performed **GridSearchCV** to optimize the Linear SVM pipeline.

Parameters tuned included:
- TF-IDF max_features
- TF-IDF ngram_range
- TF-IDF min_df
- Regularization parameter (C)

The optimized Linear SVM model achieved the best overall performance.



## 6. Model Evaluation

The final model was evaluated using multiple performance metrics.

Evaluation included:
- Classification Report
- Confusion Matrix
- Per-class Precision, Recall and F1-score
- Misclassification Analysis
- Prediction Verification on unseen resumes

The trained pipeline was then saved using **Joblib** for deployment.



## 7. Resume Analyzer

Along with resume classification, an additional resume analyzer module was developed to extract useful candidate information.

The analyzer automatically detects:
- Skills
- Education
- Experience
- Email Address
- Phone Number
- GitHub Profile
- LinkedIn Profile

This transforms the project from a simple classifier into a practical AI-powered resume analysis tool.



## 8. PDF Resume Parsing

Implemented PDF parsing using **PyMuPDF**.

Pipeline:
- Upload PDF Resume
- Extract Text
- Clean Resume
- Predict Category
- Analyze Resume
- Display Results

The system works directly with real-world PDF resumes without requiring manual text input.



## 9. Flask Web Application

Developed a lightweight Flask application to provide an interactive interface.

Users can:
- Upload a PDF resume
- Predict the resume category
- View Top-3 matching categories
- View extracted resume insights

The application has been designed with a simple and responsive interface for ease of use.



#  Model Performance

| Model | Accuracy |
|--------|---------:|
| Linear SVM | **72.23%** |
| Random Forest | 72.23% |
| Logistic Regression | 63.38% |
| Naive Bayes | 55.94% |

**Final Selected Model:** Linear Support Vector Machine (Linear SVM)

Why Linear SVM?
- Highest overall performance
- Better generalization
- Faster inference
- Well suited for high-dimensional sparse TF-IDF features





#  Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Resume-Screening-AI.git
```

Navigate into the project directory

```bash
cd Resume-Screening-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

Upload a resume PDF and start analyzing!




#  Future Improvements

The current system uses **TF-IDF + Linear SVM**, which provides strong performance while remaining lightweight and efficient. Future enhancements may include:

-  Fine-tuning **BERT** or **RoBERTa** for improved contextual understanding
-  Resume-to-Job Description (JD) matching
-  ATS (Applicant Tracking System) compatibility scoring
-  Resume ranking based on job requirements
-  Multiple resume comparison and candidate ranking
-  Skill gap analysis and personalized recommendations
-  CI/CD pipeline for automated testing and deployment
-  Cloud deployment using AWS, Azure, or Google Cloud

---

#  Author

**Bupendra Devegade**

BBA (Hons) – Business Analytics

Machine Learning | Data Science | AI | NLP

⭐ If you found this project useful, consider giving it a star!



#  Acknowledgements

- **Scikit-learn** for machine learning algorithms and TF-IDF vectorization
- **NLTK** for natural language preprocessing
- **PyMuPDF** for PDF text extraction
- **Flask** for the web application framework
- **Render** for application deployment
- **Hugging Face Spaces** for interactive AI model hosting
- The creators of the **Resume Classification Dataset** used in this project




