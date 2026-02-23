# Quick Start Guide - AI Market Research Analyst

## 🚀 Get Running in 5 Minutes

### Step 1: Get Your Gemini API Key (2 minutes)

1. Go to https://makersuite.google.com
2. Sign in with your Google account (create one if needed)
3. Click "Get API Key"
4. Click "Create new API key"
5. Copy the key to your clipboard

### Step 2: Set Up Environment (1 minute)

1. Open `.env` file in the project root
2. Replace `your_gemini_api_key_here` with your actual API key
3. Save the file

**Example `.env` file:**
```
GEMINI_API_KEY=AIzaSyD...your_actual_key...
FLASK_ENV=development
DEBUG=True
```

### Step 3: Run the Application (2 minutes)

**On Windows:**
```bash
run.bat
```

**On Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

**Manual Setup (Any OS):**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r backend/requirements.txt

# Set environment variable
export GEMINI_API_KEY=your_key_here  # Mac/Linux
set GEMINI_API_KEY=your_key_here      # Windows

# Run the app
python backend/app.py
```

### Step 4: Open in Browser

Navigate to: **http://localhost:5000**

---

## 📝 Using the Application

### Option A: Test with Sample Data
1. Click "Load Sample Analysis"
2. View the analysis results
3. Explore charts and export options

### Option B: Analyze Your Own Report
1. Click the upload area
2. Select a PDF file (max 50MB)
3. Click "Analyze Report"
4. Wait for analysis to complete
5. View results with visualizations

### Export Results
- **JSON**: Click "Export as JSON" to download structured data
- **CSV**: Click "Export as CSV" for spreadsheet format

---

## 🔧 Troubleshooting

### Issue: "Python not found"
**Solution:** Install Python from https://www.python.org (version 3.8 or higher)

### Issue: "GEMINI_API_KEY not set"
**Solution:** 
1. Check `.env` file exists
2. Verify API key is not blank
3. Restart the application

### Issue: "Port 5000 already in use"
**Solution:** Edit `backend/app.py` line 105:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to 5001
```

### Issue: PDF extraction fails
**Solution:**
- Ensure PDF is valid (not corrupted)
- Try with a different PDF
- Check file size is under 50MB

### Issue: "Connection refused" error
**Solution:**
- Make sure backend is running
- Check URL is `http://localhost:5000`
- Wait a few seconds for server to start

---

## 📊 What You Can Do

✅ Upload business reports (PDF format)
✅ Get AI-powered analysis instantly
✅ View structured insights in JSON
✅ See visualizations with charts
✅ Export results as JSON/CSV
✅ Test with sample data

---

## 🎯 Example Analysis

The AI analyzes reports for:

```json
{
  "current_business_situation": "Company overview and market position",
  "strong_points": ["Strength 1", "Strength 2", ...],
  "weak_points": ["Weakness 1", "Weakness 2", ...],
  "suggestions_for_improvement": ["Suggestion 1", "Suggestion 2", ...],
  "next_strategic_moves": ["Move 1", "Move 2", ...]
}
```

---

## 📚 Project Structure

```
ai_market_agent/
├── backend/          # Python Flask backend
│   ├── app.py           # Main application
│   ├── pdf_extractor.py # PDF text extraction
│   ├── gemini_analyzer.py # AI analysis
│   └── requirements.txt  # Python packages
├── frontend/         # Web dashboard
│   ├── index.html       # Main page
│   ├── app.js           # JavaScript logic
│   └── styles.css       # Styling
├── uploads/          # Uploaded PDFs (auto-created)
├── run.bat           # Windows launcher
├── run.sh            # Mac/Linux launcher
├── .env              # API key configuration
└── README.md         # Full documentation
```

---

## 🆘 Need Help?

1. **Check the README.md** for detailed documentation
2. **Open browser console** (F12) to see error messages
3. **Check backend logs** (running terminal)
4. **Verify API key** in .env file

---

## 🚫 Important Notes

- **Never** share your `.env` file
- **Never** commit `.env` to git/GitHub
- Keep your API key **private and secure**
- API key appears in `.env` only (not committed)

---

## 📞 Getting Help

If you encounter issues:

1. **Check Internet Connection** - Required for Gemini API
2. **Verify API Key** - Ensure it's valid and active
3. **Check Port 5000** - Make sure it's not blocked/in-use
4. **Review Error Messages** - Check browser console and terminal
5. **Try Sample Data** - Test with built-in sample first

---

## ✨ Next Steps

Once running successfully:

1. Upload a test business report (PDF)
2. Review the AI analysis
3. Export results as JSON/CSV
4. Explore the dashboard features
5. Customize for your use case

---

**Version:** 1.0.0  
**Updated:** February 19, 2026
