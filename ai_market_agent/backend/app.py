"""
AI Market Research Analyst - Main Application
Backend using Antigravity Framework
"""

from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime
from pdf_extractor import extract_text_from_pdf
from gemini_analyzer import analyze_with_gemini

# Initialize Flask app with static folder
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_folder = os.path.join(base_dir, 'frontend')
app = Flask(__name__, static_folder=static_folder, static_url_path='')

# Configuration
UPLOAD_FOLDER = os.path.join(base_dir, 'uploads')
ALLOWED_EXTENSIONS = {'pdf'}
MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 50MB max file size

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH


def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'AI Market Research Analyst'
    }), 200


@app.route('/api/analyze', methods=['POST'])
def analyze_report():
    """
    Main endpoint for analyzing business reports
    Accepts PDF file upload and returns analysis in JSON format
    """
    try:
        # Check if file is in request
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        if not allowed_file(file.filename):
            return jsonify({'error': 'Only PDF files are allowed'}), 400

        # Save uploaded file
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], timestamp + filename)
        file.save(filepath)

        # Extract text from PDF
        pdf_text = extract_text_from_pdf(filepath)
        
        if not pdf_text or len(pdf_text.strip()) == 0:
            return jsonify({'error': 'Could not extract text from PDF'}), 400
        print(f"Extracted text length: {len(pdf_text)} characters PDF text is {pdf_text}  ")
        # Analyze with Gemini API
        analysis_result = analyze_with_gemini(pdf_text)

        # Return analysis result
        return jsonify({
            'status': 'success',
            'filename': filename,
            'timestamp': datetime.now().isoformat(),
            'analysis': analysis_result
        }), 200

    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'failed'
        }), 500


@app.route('/api/sample-analysis', methods=['GET'])
def get_sample_analysis():
    """
    Returns a sample analysis for testing
    """
    sample_analysis = {
        "current_business_situation": "The company operates in a competitive market with growing demand. Current revenue streams are stable but facing pressure from emerging competitors. Market share remains solid at 22% in the primary segment.",
        "strong_points": [
            "Strong brand recognition and customer loyalty",
            "Efficient operational processes with 15% YoY efficiency gains",
            "Diversified product portfolio across 5 major categories",
            "Strong financial position with positive cash flow",
            "Experienced management team with 20+ years in industry"
        ],
        "weak_points": [
            "Limited presence in emerging markets",
            "High dependency on legacy technology platforms",
            "Limited R&D investment compared to competitors",
            "Supply chain vulnerabilities in key regions",
            "Slow digital transformation progress"
        ],
        "suggestions_for_improvement": [
            "Invest in cloud infrastructure and modernize legacy systems",
            "Increase R&D budget by 25% to focus on AI/ML capabilities",
            "Expand into emerging markets with localized strategies",
            "Strengthen supply chain resilience through diversification",
            "Launch digital transformation initiative with clear KPIs",
            "Build strategic partnerships with tech companies",
            "Enhance customer data analytics capabilities"
        ],
        "next_strategic_moves": [
            "Q1 2026: Launch digital innovation lab",
            "Q2 2026: Begin supply chain restructuring",
            "Q3 2026: Enter 3 new emerging markets",
            "Q4 2026: Complete Phase 1 of tech modernization",
            "2027: Scale successful digital products"
        ]
    }
    return jsonify({
        'status': 'success',
        'analysis': sample_analysis
    }), 200


@app.route('/', methods=['GET'])
def index():
    """Serve the frontend dashboard"""
    return send_from_directory(static_folder, 'index.html')


@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS)"""
    return send_from_directory(static_folder, filename)


if __name__ == '__main__':
    # Run with Antigravity framework
    print("Starting AI Market Research Analyst...")
    print("Backend running on http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
