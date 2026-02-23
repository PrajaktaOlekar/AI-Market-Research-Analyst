# System Architecture Documentation

## AI Market Research Analyst System Design

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Frontend Dashboard                        │
│  (HTML5, CSS3, JavaScript + Chart.js)                       │
│                                                              │
│  • File Upload Interface                                    │
│  • Analysis Display                                         │
│  • Data Visualization (Charts)                              │
│  • Export Functionality                                     │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP/REST API
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  Flask Backend (Python)                      │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Flask Application (app.py)                          │  │
│  │  • HTTP Endpoints                                    │  │
│  │  • File Upload Handling                              │  │
│  │  • Request/Response Management                       │  │
│  └──────────────────────────────────────────────────────┘  │
│                       │                                     │
│  ┌────────────────────┼────────────────────┐               │
│  ▼                    ▼                    ▼               │
│ ┌──────────┐   ┌──────────────────┐  ┌─────────────┐      │
│ │   PDF    │   │  AI Analysis     │  │  JSON/CSV   │      │
│ │Extractor │   │   Module         │  │  Response   │      │
│ │          │   │  (Gemini API)    │  │   Handler   │      │
│ │PyPDF2    │   │                  │  │             │      │
│ └──────────┘   └──────────────────┘  └─────────────┘      │
└─────────────────────────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│           Google Gemini API (Cloud Service)                  │
│                                                              │
│  • Text Analysis                                            │
│  • Business Insights Generation                             │
│  • JSON Response Formatting                                 │
└─────────────────────────────────────────────────────────────┘
```

### Component Details

#### 1. Frontend Layer

**Files:**
- `index.html` - Main UI structure
- `app.js` - Client-side logic
- `styles.css` - Styling and layout

**Responsibilities:**
- Display upload interface
- Handle file selection/drag-drop
- Make API calls
- Display analysis results
- Render charts with Chart.js
- Export functionality

**Key Features:**
- Responsive design (mobile-friendly)
- Real-time validation
- Visual feedback (loading states)
- Chart visualizations
- JSON/CSV export

#### 2. Backend Layer

**Files:**
- `app.py` - Flask application
- `pdf_extractor.py` - PDF text extraction
- `gemini_analyzer.py` - AI analysis
- `config.py` - Configuration
- `requirements.txt` - Dependencies

**Endpoints:**

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/` | GET | Serve frontend |
| `/api/analyze` | POST | Analyze PDF |
| `/api/sample-analysis` | GET | Get sample data |
| `/health` | GET | Health check |
| `/<path>` | GET | Static files |

#### 3. Data Flow

```
1. User uploads PDF
   └─> Frontend sends POST to /api/analyze

2. Backend receives file
   └─> Validate file type/size
   └─> Save to uploads/

3. Extract text from PDF
   └─> PDF Extractor (PyPDF2)
   └─> Returns: text content

4. Send to Gemini API
   └─> System prompt (business analyst role)
   └─> PDF text content
   └─> Returns: JSON analysis

5. Process response
   └─> Validate JSON
   └─> Return to frontend

6. Display results
   └─> Parse JSON
   └─> Render analysis
   └─> Create charts
```

### Analysis Output Structure

```json
{
  "current_business_situation": "Detailed summary",
  "strong_points": ["Point 1", "Point 2", ...],
  "weak_points": ["Point 1", "Point 2", ...],
  "suggestions_for_improvement": ["Suggestion 1", ...],
  "next_strategic_moves": ["Move 1", ...]
}
```

### API Integration Flow

```
User Input (PDF)
    ↓
PDF Extraction Module
    ↓
Text + System Prompt
    ↓
Gemini API Request
    ↓
JSON Response
    ↓
Validation & Processing
    ↓
Frontend Display
    ↓
User Views Analysis + Charts
    ↓
Export (JSON/CSV)
```

### Configuration Management

```
.env (Environment Variables)
├── GEMINI_API_KEY
├── FLASK_ENV
└── DEBUG

config.py (Python Configuration)
├── API settings
├── File upload settings
├── Path configuration
└── Size limits
```

### Security Measures

1. **File Upload:**
   - Whitelist PDF extension
   - Size limit (50MB)
   - Secure filename handling
   - Malware scanning (optional)

2. **API Key:**
   - Stored in .env (not committed)
   - Environment variable loading
   - Never exposed in frontend

3. **Input Validation:**
   - File type checking
   - Size validation
   - Content validation

4. **Error Handling:**
   - Graceful error messages
   - Try-catch blocks
   - Logging for debugging

### Performance Considerations

| Aspect | Strategy |
|--------|----------|
| PDF Size | Limit to 50MB |
| Text Extraction | Stream processing |
| API Calls | Single sync request |
| Frontend Load | Responsive UI |
| Caching | Session-based |

### Scalability Options

For future scaling:

1. **Batch Processing:**
   - Queue system (Redis/Celery)
   - Multiple workers
   - Async analysis

2. **Caching:**
   - Store analyses (database)
   - Result history
   - User analytics

3. **Load Balancing:**
   - Multiple backend instances
   - Load balancer
   - Session management

4. **Storage:**
   - Cloud storage (S3)
   - Database (PostgreSQL)
   - Archive old PDFs

### Deployment Considerations

**Development:**
- Local Flask server
- Debug mode enabled
- Live reload

**Production:**
- Gunicorn/uWSGI
- Nginx reverse proxy
- SSL/TLS
- Environment variables
- Logging system
- Error tracking

### Technology Stack

| Layer | Technology |
|-------|------------|
| Frontend | HTML5, CSS3, JavaScript, Chart.js |
| Backend | Python, Flask |
| AI/ML | Google Gemini API |
| PDF Processing | PyPDF2 |
| Server | Flask (dev), Gunicorn (prod) |
| Data Format | JSON, CSV |

### Error Handling

```
User Request
    ↓
Validate Input
    ├─ Invalid? → Error Response (400)
    └─ Valid → Process
        ↓
    Extract Text
    ├─ Failed? → Error Response (500)
    └─ Success → Continue
        ↓
    Call Gemini API
    ├─ Failed? → Error Response (503)
    └─ Success → Continue
        ↓
    Parse Response
    ├─ Invalid JSON? → Error Response (500)
    └─ Valid → Return (200)
```

### Database Design (Future)

```sql
-- User table
CREATE TABLE users (
    id INT PRIMARY KEY,
    email VARCHAR,
    created_at TIMESTAMP
);

-- Analysis table
CREATE TABLE analyses (
    id INT PRIMARY KEY,
    user_id INT,
    filename VARCHAR,
    analysis JSON,
    created_at TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- PDF storage (reference)
CREATE TABLE pdfs (
    id INT PRIMARY KEY,
    analysis_id INT,
    filename VARCHAR,
    size INT,
    s3_path VARCHAR,
    FOREIGN KEY (analysis_id) REFERENCES analyses(id)
);
```

---

This architecture ensures:
✅ Clean separation of concerns
✅ Easy to maintain and extend
✅ Secure API key handling
✅ Responsive user experience
✅ Scalable for future growth
