# Complete Setup Guide - AI Market Research Analyst

## 🎯 Objective
Set up and run the AI Market Research Analyst application on your computer.

---

## ⏱️ Time Required
- **API Key Setup:** 2 minutes
- **Environment Setup:** 3 minutes
- **First Run:** 2 minutes
- **Total:** ~7 minutes

---

## 📋 Prerequisites

### Required Software
- ✅ Windows 10/11 (or Mac/Linux)
- ✅ Python 3.8+ (download from https://www.python.org)
- ✅ Internet connection (for Gemini API)
- ✅ Modern web browser (Chrome, Firefox, Safari, Edge)
- ✅ Text editor (Notepad, VS Code, etc.)

### Verify Prerequisites

**Check Python Installation:**
```powershell
python --version
```
Should show: `Python 3.8.x` or higher

If not found, install from: https://www.python.org

---

## 🔑 Step 1: Get Your Gemini API Key (2 minutes)

### Instructions:

1. **Open Browser**
   - Go to: https://makersuite.google.com
   - Sign in with Google account (create if needed)

2. **Create API Key**
   - Click "Get API Key" button
   - Click "Create new API key" 
   - Copy the API key to clipboard

3. **Save for Later**
   - Write it down or keep it copied
   - You'll need it in the next step

### Important:
⚠️ **Keep your API key private!**
⚠️ **Never share it with anyone!**
⚠️ **Don't commit it to git!**

---

## 📂 Step 2: Locate Project Files (1 minute)

The project is in:
```
d:\Internship\ai_market_agent\
```

### Verify Files Exist:
Navigate to the folder and check for:
- ✅ `backend/` folder
- ✅ `frontend/` folder
- ✅ `run.bat` file
- ✅ `.env.example` file
- ✅ `README.md` file

---

## 🔧 Step 3: Configure Environment (1 minute)

### Windows (Notepad Method):

1. **Open File Explorer**
   - Navigate to: `d:\Internship\ai_market_agent\`

2. **Create `.env` File**
   - Right-click in empty space
   - Select "New" → "Text Document"
   - Name it: `.env`
   - Press Enter

3. **Edit the File**
   - Right-click `.env`
   - Select "Open with" → "Notepad"
   - Type:
   ```
   GEMINI_API_KEY=paste_your_api_key_here
   FLASK_ENV=development
   DEBUG=True
   ```
   - Replace `paste_your_api_key_here` with your actual key
   - Save (Ctrl+S)
   - Close Notepad

### Example `.env` Content:
```
GEMINI_API_KEY=your_api_key_here
FLASK_ENV=development
DEBUG=True
```

### Alternative: Copy from Template

```powershell
copy .env.example .env
# Then edit .env with your API key
```

---

## 🚀 Step 4: Run the Application (2 minutes)

### Option A: Using Startup Script (Recommended)

1. **Open File Explorer**
   - Navigate to: `d:\Internship\ai_market_agent\`

2. **Double-Click `run.bat`**
   - A command window will open
   - It will:
     - Check Python installation
     - Create virtual environment
     - Install dependencies
     - Start the server

3. **Wait for Message:**
   ```
   Backend running on http://localhost:5000
   ```

### Option B: Manual Setup (Advanced)

```powershell
# Open PowerShell or Command Prompt
# Navigate to project folder
cd d:\Internship\ai_market_agent

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r backend\requirements.txt

# Set environment variable
$env:GEMINI_API_KEY="your_api_key_here"

# Run application
python backend\app.py
```

---

## 🌐 Step 5: Access Dashboard (1 minute)

1. **Open Web Browser**
   - Use: Chrome, Firefox, Safari, or Edge

2. **Go to URL:**
   ```
   http://localhost:5000
   ```

3. **You Should See:**
   - "🤖 AI Market Research Analyst" heading
   - Upload area for PDF files
   - "Load Sample Analysis" button

---

## ✅ Verification Checklist

Before proceeding, verify:

- ✅ `.env` file created with API key
- ✅ `run.bat` window shows "Backend running on http://localhost:5000"
- ✅ Browser shows the dashboard
- ✅ Upload area is visible
- ✅ "Load Sample Analysis" button is clickable

---

## 🧪 Test 1: Sample Analysis (No PDF Needed)

1. **Click "Load Sample Analysis"**
   - Button shows loading indicator
   - Results appear on page

2. **Verify Results Show:**
   - Current Business Situation
   - Strong Points
   - Weak Points
   - Suggestions for Improvement
   - Next Strategic Moves

3. **Check Charts:**
   - "Strengths vs Weaknesses" bar chart
   - "Analysis Breakdown" pie chart

4. **Test Export:**
   - Click "Export as JSON"
   - Check downloads folder
   - File should be: `business_analysis.json`

---

## 🧪 Test 2: Analyze Your PDF

### Get a Sample PDF:
1. Create a simple text document
2. Type some business information
3. Save as PDF (or use any PDF you have)

### Upload and Analyze:
1. Click upload area or drag-drop PDF
2. Select your PDF file
3. Click "Analyze Report"
4. Wait for analysis (30-60 seconds)
5. View results

---

## 🎯 Common Tasks

### How to Stop the Server
- Press `Ctrl+C` in the command window
- Or close the command window

### How to Restart Server
- Close command window (if open)
- Double-click `run.bat` again

### How to Access from Another Computer
1. Find your computer's IP address:
   ```powershell
   ipconfig
   ```
   Look for "IPv4 Address" (like 192.168.1.100)

2. On other computer, go to:
   ```
   http://your_ip_address:5000
   ```

---

## 🐛 Troubleshooting

### Problem: "python is not recognized"

**Solution:**
1. Install Python from https://www.python.org
2. **Important:** Check "Add Python to PATH" during installation
3. Restart command prompt
4. Try again

### Problem: ".env file not found"

**Solution:**
1. Create `.env` file manually in text editor
2. Copy content from `.env.example`
3. Replace API key placeholder
4. Save and close

### Problem: "GEMINI_API_KEY not set"

**Solution:**
1. Verify `.env` file exists
2. Open `.env` and check API key is there
3. Make sure line is: `GEMINI_API_KEY=your_key`
4. Restart server

### Problem: "Address already in use"

**Solution:**
1. Close other command windows running app
2. Or change port in `backend/app.py` line 105:
   ```python
   app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to 5001
   ```

### Problem: Browser shows "Connection refused"

**Solution:**
1. Check command window shows "Backend running..."
2. Wait 5 seconds for server to fully start
3. Refresh browser (F5)
4. Try different port (see above)

### Problem: PDF upload fails

**Solution:**
1. Ensure file is a valid PDF
2. Check file size is under 50MB
3. Try with different PDF
4. Check internet connection

### Problem: Analysis shows error

**Solution:**
1. Check API key in `.env` is correct
2. Verify internet connection
3. Check command window for error messages
4. Try sample analysis first

---

## 📊 Expected Output

### Sample Analysis Response:
```json
{
  "current_business_situation": "The company operates in a competitive market...",
  "strong_points": [
    "Strong brand recognition",
    "Efficient operations",
    "..."
  ],
  "weak_points": [
    "Limited presence in emerging markets",
    "..."
  ],
  "suggestions_for_improvement": [
    "Invest in cloud infrastructure",
    "..."
  ],
  "next_strategic_moves": [
    "Q1 2026: Launch digital innovation lab",
    "..."
  ]
}
```

---

## 📚 File Locations

| File | Location | Purpose |
|------|----------|---------|
| `.env` | Project root | API key configuration |
| `run.bat` | Project root | Windows launcher |
| `backend/app.py` | backend/ | Main Flask app |
| `frontend/index.html` | frontend/ | Dashboard UI |
| `uploads/` | Project root | Stores uploaded PDFs |

---

## 🔐 Security Reminders

### Do's ✅
- ✅ Keep `.env` file private
- ✅ Use environment variables
- ✅ Keep API key secure
- ✅ Add `.env` to `.gitignore`

### Don'ts ❌
- ❌ Don't commit `.env` to git
- ❌ Don't share API key
- ❌ Don't hardcode secrets
- ❌ Don't expose API key in code

---

## 💡 Tips & Tricks

### Tip 1: Use Sample Data First
Always test with sample data before uploading PDFs to verify everything works.

### Tip 2: Monitor Console Logs
Keep the command window visible to see logs and errors.

### Tip 3: Check Browser Console
Press F12 in browser to see client-side errors and logs.

### Tip 4: Test with Different PDFs
Different PDFs may extract text differently. Try multiple files.

### Tip 5: Export Results
Always export results you want to keep (JSON or CSV format).

---

## 📞 Getting More Help

### Check Documentation:
1. **QUICKSTART.md** - Quick reference
2. **README.md** - Full documentation
3. **ARCHITECTURE.md** - System design
4. **IMPLEMENTATION.md** - Complete details

### Debug Steps:
1. Check if API key is set correctly
2. Verify internet connection
3. Check browser console (F12)
4. Check command window logs
5. Try sample analysis first

---

## ✨ Next Steps After Setup

1. ✅ Test with sample analysis
2. ✅ Upload your first PDF
3. ✅ Export results
4. ✅ Explore all features
5. ✅ Read documentation
6. ✅ Customize for your needs

---

## 🎓 Learning Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Google Gemini API](https://ai.google.dev/)
- [Chart.js Documentation](https://www.chartjs.org/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)

---

## 📝 Notes

### For Windows Users:
- Use `.bat` file for easiest setup
- PowerShell or Command Prompt both work
- Make sure Python is added to PATH

### For Mac/Linux Users:
- Use `run.sh` instead of `run.bat`
- May need to run: `chmod +x run.sh`
- Python3 is usually pre-installed

### For All Users:
- Internet connection required
- API key required (free from Google)
- Browser must support modern web features

---

## 🏁 You're All Set!

Your AI Market Research Analyst is now ready to use! 🚀

### Quick Reminder:
1. **Run:** `run.bat` (or `./run.sh` on Mac/Linux)
2. **Open:** http://localhost:5000
3. **Test:** Load sample analysis
4. **Upload:** Your first PDF
5. **Export:** Results as JSON/CSV

---

**Need help?** Check the troubleshooting section or review the documentation files.

**Happy analyzing!** 🤖📊✨

---

**Version:** 1.0.0  
**Created:** February 19, 2026  
**Status:** ✅ Production Ready
