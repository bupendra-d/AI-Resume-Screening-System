# Text preprocessing Libraries for Resume Screening AI
import re
import unicodedata

import nltk

nltk.data.path.append(r"C:\Users\bhupi\OneDrive\Desktop\nltk_data")

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


# Download NLTK Resources
# nltk.download("stopwords")
# nltk.download("wordnet")
# nltk.download("omw-1.4")


# Initialize Objects
STOP_WORDS = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()



# Step 1: Lowercase-Text Function:

def lowercase_text(text: str) -> str:
    """
    Convert text to lowercase.

    Parameters
    ----------
    text : str
        Input resume text.

    Returns
    -------
    str
        Lowercase text.
    """

    return text.lower()



# Step 2: Remove-URL Function:

URL_PATTERN = r"https?://\S+|www\.\S+"

def remove_urls(text: str) -> str:
    """
    Remove URLs from resume text.

    Parameters
    ----------
    text : str
        Input resume text.

    Returns
    -------
    str
        Resume text with URLs removed.
    """

    if not isinstance(text, str):
        return ""

    return re.sub(URL_PATTERN, "", text)



# Step 3: Remove Email Addresses Function:

EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

def remove_emails(text: str) -> str:
    """
    Remove email addresses from resume text.

    Parameters
    ----------
    text : str
        Input resume text.

    Returns
    -------
    str
        Resume text with email addresses removed.
    """

    if not isinstance(text, str):
        return ""

    return re.sub(EMAIL_PATTERN, "", text)



# Step 4: Remove Phone Number Function:

PHONE_PATTERN = (
    r"\+?\d{1,3}[-.\s]?"
    r"\(?\d{2,4}\)?[-.\s]?"
    r"\d{3,4}[-.\s]?\d{4}"
)


def remove_phone_numbers(text: str) -> str:
    """
    Remove phone numbers from resume text.

    Parameters
    ----------
    text : str
        Input resume text.

    Returns
    -------
    str
        Resume text with phone numbers removed.
    """

    if not isinstance(text, str):
        return ""

    return re.sub(PHONE_PATTERN, "", text)



# Step 5: Removing HTML Tags:

from bs4 import BeautifulSoup

def remove_html_tags(text: str) -> str:
    """
    Remove HTML tags from text.

    Parameters
    ----------
    text : str
        HTML text.

    Returns
    -------
    str
        Plain text.
    """

    if not isinstance(text, str):
        return ""

    soup = BeautifulSoup(text, "html.parser")

    return soup.get_text(separator=" ")



# Step 6: Unicode Normalization Function:

def normalize_unicode(text: str) -> str:
    """
    Normalize Unicode characters.

    Parameters
    ----------
    text : str
        Input resume text.

    Returns
    -------
    str
        Unicode-normalized text.
    """

    if not isinstance(text, str):
        return ""

    return unicodedata.normalize("NFKC", text)



# Step 7: Whitespace Normalization Function:

def normalize_whitespace(text: str) -> str:
    """
    Normalize whitespace by replacing multiple whitespace
    characters with a single space.

    Parameters
    ----------
    text : str
        Input resume text.

    Returns
    -------
    str
        Cleaned text with normalized whitespace.
    """

    if not isinstance(text, str):
        return ""

    text = re.sub(r"\s+", " ", text)

    return text.strip()



# Step 8: Tokenization Function:

def tokenize_text(text: str) -> list:
    """
    Tokenize text into words.

    Parameters
    ----------
    text : str
        Input resume text.

    Returns
    -------
    list
        List of tokens.
    """

    if not isinstance(text, str):
        return []

    return word_tokenize(text)



# Step 9: Stopwords Removal Function:

def remove_stopwords(tokens: list) -> list:
    """
    Remove English stopwords from a list of tokens.

    Parameters
    ----------
    tokens : list
        List of word tokens.

    Returns
    -------
    list
        Tokens after stopword removal.
    """

    if not isinstance(tokens, list):
        return []

    return [
        token
        for token in tokens
        if token.lower() not in STOP_WORDS
    ]




# Step 10: Remove Punctuation Tokens Function:

import string

def remove_punctuation_tokens(tokens: list) -> list:
    """
    Remove tokens that consist entirely of punctuation.

    Parameters
    ----------
    tokens : list
        List of word tokens.

    Returns
    -------
    list
        Tokens with standalone punctuation removed.
    """

    if not isinstance(tokens, list):
        return []

    return [
        token
        for token in tokens
        if token not in string.punctuation
    ]




# Step 11: Remove Resume Stopwords:

RESUME_STOPWORDS = {
    "summary",
    "objective",
    "objectives",
    "profile",
    "professional",
    "experience",
    "education",
    "skills",
    "skill",
    "employment",
    "company",
    "name",
    "city",
    "state",
    "resume",
    "curriculum",
    "vitae",
    "current",
    "present",
    "'s"
}

# Remove Resume Stopwords Function:
def remove_resume_stopwords(tokens: list) -> list:
    """
    Remove resume-specific boilerplate words.

    Parameters
    ----------
    tokens : list
        Tokenized resume.

    Returns
    -------
    list
        Tokens after removing resume-specific stopwords.
    """

    if not isinstance(tokens, list):
        return []

    return [
        token
        for token in tokens
        if token.lower() not in RESUME_STOPWORDS
    ]



# Step 12: Lemmatization Function:

def lemmatize_tokens(tokens: list) -> list:
    """
    Lemmatize a list of word tokens.

    Parameters
    ----------
    tokens : list
        Tokenized resume.

    Returns
    -------
    list
        Lemmatized tokens.
    """

    if not isinstance(tokens, list):
        return []

    return [
        lemmatizer.lemmatize(token)
        for token in tokens
    ]



# Step 13: Create a Master Function to Call all the Preprocessing Function:

def clean_resume(text: str) -> str:
    """
    Complete preprocessing pipeline for resume text.

    Parameters
    ----------
    text : str
        Raw resume text.

    Returns
    -------
    str
        Fully cleaned resume text.
    """

    # Safety check
    if not isinstance(text, str):
        return ""

    # Text-level preprocessing
    text = lowercase_text(text)
    text = remove_urls(text)
    text = remove_emails(text)
    text = remove_phone_numbers(text)
    text = remove_html_tags(text)
    text = normalize_unicode(text)
    text = normalize_whitespace(text)

    # Token-level preprocessing
    tokens = tokenize_text(text)
    tokens = remove_stopwords(tokens)
    tokens = remove_punctuation_tokens(tokens)
    tokens = remove_resume_stopwords(tokens)
    tokens = lemmatize_tokens(tokens)

    # Convert tokens back into text
    cleaned_text = " ".join(tokens)

    return cleaned_text
