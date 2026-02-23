"""
PDF Extraction Module
Extracts text content from PDF files
"""

import PyPDF2
import os


def extract_text_from_pdf(filepath):
    """
    Extract text from a PDF file
    
    Args:
        filepath (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF
    """
    try:
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"PDF file not found: {filepath}")
        
        text_content = []
        
        with open(filepath, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            num_pages = len(pdf_reader.pages)
            
            print(f"Extracting text from {num_pages} pages...")
            
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                page_text = page.extract_text()
                text_content.append(page_text)
        
        extracted_text = "\n".join(text_content)
        
        # Clean up the text
        extracted_text = extracted_text.strip()
        
        print(f"Successfully extracted {len(extracted_text)} characters from PDF")
        
        return extracted_text
    
    except Exception as e:
        print(f"Error extracting text from PDF: {str(e)}")
        raise


def extract_text_with_limit(filepath, max_chars=10000):
    """
    Extract text from PDF with character limit
    Useful for API constraints
    
    Args:
        filepath (str): Path to the PDF file
        max_chars (int): Maximum characters to extract
        
    Returns:
        str: Extracted text (limited to max_chars)
    """
    full_text = extract_text_from_pdf(filepath)
    return full_text[:max_chars]
