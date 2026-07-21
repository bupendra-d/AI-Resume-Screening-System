import fitz


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from all pages of a PDF resume.

    Parameters
    ----------
    pdf_path : str
        Path to the PDF file.

    Returns
    -------
    str
        Extracted text.

    Raises
    ------
    RuntimeError
        If the PDF cannot be opened or read.
    """

    try:

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    except Exception as e:

        raise RuntimeError(
            f"Error reading PDF: {e}"
        )