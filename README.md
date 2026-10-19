# AI Market Research Analyst

A simple, functional AI-based software for analyzing business reports using the Antigravity framework and Google's Gemini API.

## Overview

This application analyzes company business reports and provides intelligent insights in JSON format with dashboard visualization.

### Features

- ✅ PDF file upload and text extraction
- ✅ AI-powered analysis using Gemini API
- ✅ Structured JSON output
- ✅ Interactive dashboard with charts
- ✅ Export results as JSON and CSV
- ✅ Sample data for testing

## Project Structure

```
ai_market_agent/
├── backend/
│   ├── app.py                 # Main Antigravity application
│   ├── pdf_extractor.py       # PDF text extraction
│   ├── gemini_analyzer.py     # Gemini API integration
│   ├── config.py              # Configuration
│   └── requirements.txt        # Python dependencies
├── frontend/
│   ├── index.html             # Main dashboard
│   ├── app.js                 # Frontend logic
│   └── styles.css             # Styling
├── uploads/                   # Folder for uploaded PDFs
└── .env                       # Environment variables (create this)
```

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Google Gemini API key (free from [Google AI Studio](https://makersuite.google.com))
- Modern web browser

## Installation & Setup

### 1. Clone/Extract the Project

Navigate to the project directory:

```bash
cd ai_market_agent
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
GEMINI_API_KEY=your_api_key_here
FLASK_ENV=development
DEBUG=True
```

Replace `your_api_key_here` with your actual Gemini API key.

### 3. Install Python Dependencies

Create a virtual environment (recommended):

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

Install required packages:

```bash
pip install -r backend/requirements.txt
```

## Running the Application

### Start the Backend Server

From the project root:

```bash
python backend/app.py
```

You should see:
```
Starting AI Market Research Analyst...
Backend running on http://localhost:5000
```

### Access the Frontend

Open your browser and go to:

```
http://localhost:5000
```

## How to Use

### Method 1: Upload a Business Report

1. Go to the dashboard
2. Click the upload area or drag-and-drop a PDF file
3. Click "Analyze Report"
4. Wait for the analysis to complete
5. View results with charts and visualizations
6. Export as JSON or CSV

### Method 2: Use Sample Data

1. Click "Load Sample Analysis"
2. View sample analysis results
3. Explore the dashboard and export options

## API Endpoints

### `POST /api/analyze`
Analyzes an uploaded business report PDF.

**Request:**
- Form data with `file` (PDF file)

**Response:**
```json
{
  "status": "success",
  "filename": "report.pdf",
  "timestamp": "2026-02-19T10:30:00",
  "analysis": {
    "current_business_situation": "...",
    "strong_points": ["..."],
    "weak_points": ["..."],
    "suggestions_for_improvement": ["..."],
    "next_strategic_moves": ["..."]
  }
}
```

### `GET /api/sample-analysis`
Returns a sample analysis for testing.

### `GET /health`
Health check endpoint.

## Analysis Output Format

All analyses are returned in JSON format:

```json
{
  "current_business_situation": "Clear summary of current status",
  "strong_points": ["Point 1", "Point 2", ...],
  "weak_points": ["Point 1", "Point 2", ...],
  "suggestions_for_improvement": ["Suggestion 1", "Suggestion 2", ...],
  "next_strategic_moves": ["Move 1", "Move 2", ...]
}
```

## Configuration

Edit `backend/config.py` to customize:

- `GEMINI_API_KEY` - Your API key
- `FLASK_ENV` - Development or production
- `DEBUG` - Enable/disable debug mode
- `MAX_CONTENT_LENGTH` - Max file upload size
- `MAX_PDF_CHARS` - Max characters to extract from PDF

## Troubleshooting

### "GEMINI_API_KEY not set"
- Make sure `.env` file exists in project root
- Verify your API key is correctly copied
- Restart the server after adding `.env`

### Port 5000 already in use
- Change port in `app.py`: `app.run(port=5001)`
- Or kill the process using port 5000

### PDF extraction fails
- Ensure PDF is valid and not encrypted
- Check file size (max 50MB)
- Try with a different PDF

### "Network error"
- Check backend is running
- Verify correct URL in browser
- Check browser console for errors

## Technologies Used

- **Backend:** Flask, Python, Antigravity
- **AI/ML:** Google Gemini API
- **Frontend:** HTML5, CSS3, JavaScript
- **Charts:** Chart.js
- **PDF Processing:** PyPDF2

## File Size Limits

- Max upload size: 50MB
- Max PDF text extraction: 10,000 characters (for API)

## Security Notes

- Never commit `.env` file to version control
- Sanitize file uploads
- Use HTTPS in production
- Keep API key confidential
- Implement rate limiting for production

## Future Enhancements

- [ ] Multiple PDF upload
- [ ] Batch processing
- [ ] Custom analysis templates
- [ ] User authentication
- [ ] Result history/storage
- [ ] Email reports
- [ ] More export formats (PDF, Word)
- [ ] Real-time analysis progress
- [ ] Multi-language support

## License

This project is provided as-is for educational and business use.

## Support

For issues or questions:
1. Check troubleshooting section
2. Review error messages in browser console
3. Check backend server logs
4. Verify `.env` configuration

## Getting Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com)
2. Click "Get API Key"
3. Create new API key
4. Copy and paste into `.env` file

---

**Version:** 1.0.0  
**Last Updated:** February 19, 2026
