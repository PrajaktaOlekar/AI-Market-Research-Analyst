// Frontend Application JavaScript
let currentAnalysis = null;
let strengthsChart = null;
let breakdownChart = null;

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    setupUploadArea();
    setupEventListeners();
    console.log('Application initialized');
});

// Setup upload area drag and drop
function setupUploadArea() {
    const uploadArea = document.getElementById('uploadArea');
    const fileInput = document.getElementById('fileInput');

    // Click to select file
    uploadArea.addEventListener('click', () => fileInput.click());

    // Drag and drop
    uploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        uploadArea.classList.add('dragover');
    });

    uploadArea.addEventListener('dragleave', () => {
        uploadArea.classList.remove('dragover');
    });

    uploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadArea.classList.remove('dragover');
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            handleFileSelect(files[0]);
        }
    });

    // File input change
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            handleFileSelect(e.target.files[0]);
        }
    });
}

// Handle file selection
function handleFileSelect(file) {
    const uploadArea = document.getElementById('uploadArea');
    const fileInfo = document.getElementById('fileInfo');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const btnText = document.getElementById('btnText');

    if (file.type !== 'application/pdf') {
        showError('Please select a PDF file');
        return;
    }

    if (file.size > 50 * 1024 * 1024) {
        showError('File size exceeds 50MB limit');
        return;
    }

    // Store file for later use
    window.selectedFile = file;

    // Update UI
    fileInfo.style.display = 'block';
    fileInfo.innerHTML = `
        ✅ <strong>${file.name}</strong> 
        <span style="color: var(--text-light);">(${formatFileSize(file.size)})</span>
    `;

    analyzeBtn.disabled = false;
    btnText.textContent = 'Analyze Report';

    console.log('File selected:', file.name);
}

// Setup event listeners
function setupEventListeners() {
    document.getElementById('analyzeBtn').addEventListener('click', analyzeReport);
    document.getElementById('sampleBtn').addEventListener('click', loadSampleAnalysis);
    document.getElementById('newAnalysisBtn').addEventListener('click', resetForm);
    document.getElementById('exportJsonBtn').addEventListener('click', exportAsJSON);
    document.getElementById('exportCsvBtn').addEventListener('click', exportAsCSV);
}

// Analyze report
async function analyzeReport() {
    if (!window.selectedFile) {
        showError('Please select a file');
        return;
    }

    const analyzeBtn = document.getElementById('analyzeBtn');
    const btnText = document.getElementById('btnText');
    const spinner = document.getElementById('spinner');

    // Disable button and show loading
    analyzeBtn.disabled = true;
    btnText.textContent = 'Analyzing...';
    spinner.style.display = 'inline-block';

    try {
        const formData = new FormData();
        formData.append('file', window.selectedFile);

        console.log('Sending request to /api/analyze');

        const response = await fetch('/api/analyze', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (response.ok && data.analysis) {
            currentAnalysis = data.analysis;
            displayResults(data.analysis);
            hideError();
        } else {
            showError(data.error || 'Failed to analyze report');
        }
    } catch (error) {
        console.error('Error:', error);
        showError('Network error: ' + error.message);
    } finally {
        analyzeBtn.disabled = false;
        btnText.textContent = 'Analyze Report';
        spinner.style.display = 'none';
    }
}

// Load sample analysis
async function loadSampleAnalysis() {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const btnText = document.getElementById('btnText');
    const spinner = document.getElementById('spinner');

    analyzeBtn.disabled = true;
    btnText.textContent = 'Loading Sample...';
    spinner.style.display = 'inline-block';

    try {
        console.log('Loading sample analysis');

        const response = await fetch('/api/sample-analysis');
        const data = await response.json();

        if (response.ok && data.analysis) {
            currentAnalysis = data.analysis;
            displayResults(data.analysis);
            hideError();

            // Update file info
            document.getElementById('fileInfo').style.display = 'block';
            document.getElementById('fileInfo').innerHTML = '📋 Sample Business Report Analysis';
        } else {
            showError('Failed to load sample data');
        }
    } catch (error) {
        console.error('Error:', error);
        showError('Error loading sample: ' + error.message);
    } finally {
        analyzeBtn.disabled = false;
        btnText.textContent = 'Analyze Report';
        spinner.style.display = 'none';
    }
}

// Display results
function displayResults(analysis) {
    const uploadSection = document.querySelector('.upload-section');
    const resultsSection = document.getElementById('resultsSection');
    const errorSection = document.getElementById('errorSection');

    // Hide upload and error sections
    uploadSection.style.display = 'none';
    errorSection.style.display = 'none';

    // Display results
    resultsSection.style.display = 'block';

    // Populate current situation
    document.getElementById('currentSituation').textContent = 
        analysis.current_business_situation || 'No data available';

    // Populate strong points
    populatePoints('strongPointsContainer', analysis.strong_points || []);

    // Populate weak points
    populatePoints('weakPointsContainer', analysis.weak_points || []);

    // Populate suggestions
    populatePoints('suggestionsContainer', analysis.suggestions_for_improvement || []);

    // Populate strategic moves
    populatePoints('movesContainer', analysis.next_strategic_moves || []);

    // Create charts
    createCharts(analysis);

    console.log('Results displayed successfully');
}

// Populate points
function populatePoints(containerId, points) {
    const container = document.getElementById(containerId);
    container.innerHTML = '';

    if (!Array.isArray(points)) {
        points = [points];
    }

    points.forEach(point => {
        const pointElement = document.createElement('div');
        pointElement.className = 'point-item';
        pointElement.textContent = point;
        container.appendChild(pointElement);
    });
}

// Create charts
function createCharts(analysis) {
    const strongPoints = Array.isArray(analysis.strong_points) ? analysis.strong_points.length : 1;
    const weakPoints = Array.isArray(analysis.weak_points) ? analysis.weak_points.length : 1;

    // Destroy existing charts
    if (strengthsChart) strengthsChart.destroy();
    if (breakdownChart) breakdownChart.destroy();

    // Strengths vs Weaknesses Chart
    const strengthsCtx = document.getElementById('strengthsChart').getContext('2d');
    strengthsChart = new Chart(strengthsCtx, {
        type: 'bar',
        data: {
            labels: ['Strengths', 'Weaknesses'],
            datasets: [{
                label: 'Count',
                data: [strongPoints, weakPoints],
                backgroundColor: [
                    'rgba(16, 185, 129, 0.8)',
                    'rgba(245, 158, 11, 0.8)'
                ],
                borderColor: [
                    'rgb(16, 185, 129)',
                    'rgb(245, 158, 11)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    max: Math.max(strongPoints, weakPoints) + 1
                }
            }
        }
    });

    // Analysis Breakdown Pie Chart
    const breakdownCtx = document.getElementById('breakdownChart').getContext('2d');
    breakdownChart = new Chart(breakdownCtx, {
        type: 'doughnut',
        data: {
            labels: [
                'Strong Points',
                'Weak Points',
                'Suggestions',
                'Strategic Moves'
            ],
            datasets: [{
                data: [
                    strongPoints,
                    weakPoints,
                    Array.isArray(analysis.suggestions_for_improvement) ? 
                        analysis.suggestions_for_improvement.length : 1,
                    Array.isArray(analysis.next_strategic_moves) ? 
                        analysis.next_strategic_moves.length : 1
                ],
                backgroundColor: [
                    'rgba(16, 185, 129, 0.8)',
                    'rgba(245, 158, 11, 0.8)',
                    'rgba(99, 102, 241, 0.8)',
                    'rgba(236, 72, 153, 0.8)'
                ],
                borderColor: [
                    'rgb(16, 185, 129)',
                    'rgb(245, 158, 11)',
                    'rgb(99, 102, 241)',
                    'rgb(236, 72, 153)'
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom'
                }
            }
        }
    });
}

// Export as JSON
function exportAsJSON() {
    if (!currentAnalysis) {
        showError('No analysis data to export');
        return;
    }

    const dataStr = JSON.stringify(currentAnalysis, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    downloadFile(dataBlob, 'business_analysis.json');
}

// Export as CSV
function exportAsCSV() {
    if (!currentAnalysis) {
        showError('No analysis data to export');
        return;
    }

    let csvContent = 'Category,Details\n';
    csvContent += `"Current Situation","${escapeCSV(currentAnalysis.current_business_situation)}"\n`;

    if (Array.isArray(currentAnalysis.strong_points)) {
        currentAnalysis.strong_points.forEach(point => {
            csvContent += `"Strong Point","${escapeCSV(point)}"\n`;
        });
    }

    if (Array.isArray(currentAnalysis.weak_points)) {
        currentAnalysis.weak_points.forEach(point => {
            csvContent += `"Weak Point","${escapeCSV(point)}"\n`;
        });
    }

    if (Array.isArray(currentAnalysis.suggestions_for_improvement)) {
        currentAnalysis.suggestions_for_improvement.forEach(point => {
            csvContent += `"Suggestion","${escapeCSV(point)}"\n`;
        });
    }

    if (Array.isArray(currentAnalysis.next_strategic_moves)) {
        currentAnalysis.next_strategic_moves.forEach(point => {
            csvContent += `"Strategic Move","${escapeCSV(point)}"\n`;
        });
    }

    const csvBlob = new Blob([csvContent], { type: 'text/csv' });
    downloadFile(csvBlob, 'business_analysis.csv');
}

// Helper to escape CSV values
function escapeCSV(str) {
    return String(str).replace(/"/g, '""');
}

// Helper to download file
function downloadFile(blob, filename) {
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);
}

// Show error
function showError(message) {
    const errorSection = document.getElementById('errorSection');
    const errorMessage = document.getElementById('errorMessage');
    const uploadSection = document.querySelector('.upload-section');
    const resultsSection = document.getElementById('resultsSection');

    errorMessage.textContent = message;
    errorSection.style.display = 'block';
    uploadSection.style.display = 'block';
    resultsSection.style.display = 'none';

    console.error('Error:', message);
}

// Hide error
function hideError() {
    const errorSection = document.getElementById('errorSection');
    errorSection.style.display = 'none';
}

// Reset form
function resetForm() {
    const uploadSection = document.querySelector('.upload-section');
    const resultsSection = document.getElementById('resultsSection');
    const errorSection = document.getElementById('errorSection');
    const fileInput = document.getElementById('fileInput');
    const fileInfo = document.getElementById('fileInfo');
    const analyzeBtn = document.getElementById('analyzeBtn');

    uploadSection.style.display = 'block';
    resultsSection.style.display = 'none';
    errorSection.style.display = 'none';

    fileInput.value = '';
    fileInfo.style.display = 'none';
    analyzeBtn.disabled = true;

    window.selectedFile = null;
    currentAnalysis = null;

    console.log('Form reset');
}

// Format file size
function formatFileSize(bytes) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round(bytes / Math.pow(k, i) * 100) / 100 + ' ' + sizes[i];
}

// API Base URL (for production)
const API_BASE_URL = window.location.origin;
