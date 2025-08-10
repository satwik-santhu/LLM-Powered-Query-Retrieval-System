<<<<<<< HEAD
import requests
import pdfplumber
import io
from typing import Union
from fastapi import UploadFile

def extract_text_from_pdf_url(url: str) -> str:
    """
    Downloads a PDF from the given URL and extracts readable text from each page.

    Args:
        url (str): Direct URL to the PDF file (must be accessible and downloadable).

    Returns:
        str: Combined text content extracted from all PDF pages.

    Raises:
        Exception: If the file cannot be downloaded or opened.
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch PDF: HTTP {response.status_code}")
        
        with pdfplumber.open(io.BytesIO(response.content)) as pdf:
            text = "\n".join(
                [page.extract_text() for page in pdf.pages if page.extract_text()]
            )
        
        if not text.strip():
            raise Exception("PDF was downloaded but no text could be extracted.")
        
        return text

    except Exception as e:
        raise Exception(f"Error while processing PDF: {e}")


def extract_text_from_uploaded_file(file: UploadFile) -> str:
    """
    Extracts text from an uploaded PDF file.

    Args:
        file (UploadFile): The uploaded PDF file object.

    Returns:
        str: Combined text content extracted from all PDF pages.

    Raises:
        Exception: If the file cannot be processed or opened.
    """
    try:
        # Validate file type
        if not file.filename.lower().endswith('.pdf'):
            raise Exception("Only PDF files are supported.")
        
        # Read file content
        file_content = file.file.read()
        
        # Reset file pointer for future use if needed
        file.file.seek(0)
        
        with pdfplumber.open(io.BytesIO(file_content)) as pdf:
            text = "\n".join(
                [page.extract_text() for page in pdf.pages if page.extract_text()]
            )
        
        if not text.strip():
            raise Exception("PDF was uploaded but no text could be extracted.")
        
        return text

    except Exception as e:
        raise Exception(f"Error while processing uploaded PDF: {e}")
=======
import requests
import pdfplumber
import io

def extract_text_from_pdf_url(url: str) -> str:
    """
    Downloads a PDF from the given URL and extracts readable text from each page.

    Args:
        url (str): Direct URL to the PDF file (must be accessible and downloadable).

    Returns:
        str: Combined text content extracted from all PDF pages.

    Raises:
        Exception: If the file cannot be downloaded or opened.
    """
    try:
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch PDF: HTTP {response.status_code}")
        
        with pdfplumber.open(io.BytesIO(response.content)) as pdf:
            text = "\n".join(
                [page.extract_text() for page in pdf.pages if page.extract_text()]
            )
        
        if not text.strip():
            raise Exception("PDF was downloaded but no text could be extracted.")
        
        return text

    except Exception as e:
        raise Exception(f"Error while processing PDF: {e}")
>>>>>>> 403fe5837f5e87f357ce88dcdd60c34961fed4eb
