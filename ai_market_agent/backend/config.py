"""
Environment Configuration
Create .env file in the root directory with your API key:
GEMINI_API_KEY=your_api_key_here
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')

# Flask Configuration
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'

# File Upload Configuration
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), '../uploads')
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB

# API Configuration
API_TIMEOUT = 60
MAX_PDF_CHARS = 10000
