"""
Gemini API Analyzer Module
Integrates with Google's Gemini API for business analysis
"""

import google.generativeai as genai
import json
import os
from typing import Dict
import re
from dotenv import load_dotenv
load_dotenv()   # THIS LINE IS REQUIRED

api_key = os.getenv("GEMINI_API_KEY")

class GeminiAnalyzer:
    """
    Handles communication with Gemini API for business analysis
    """
    
    def __init__(self, api_key: str = None):
        """
        Initialize Gemini API client
        
        Args:
            api_key (str): Gemini API key (if None, uses GEMINI_API_KEY env var)
        """
        if api_key is None:
            api_key = os.getenv('GEMINI_API_KEY')
        
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.api_key = api_key
    
    def create_system_prompt(self) -> str:
        """
        Create a system prompt for market research analysis
        
        Returns:
            str: System prompt for the model
        """
        return """You are a professional Business Analyst and Market Research Expert with 15+ years of experience in strategic business analysis.

Your task is to analyze business reports and provide comprehensive insights in a structured JSON format.

IMPORTANT REQUIREMENTS:
1. Always respond with VALID JSON only - no markdown, no code blocks, no explanations outside JSON
2. Analyze the report systematically
3. Provide actionable, specific insights
4. Use professional business language
5. Base all analysis on the provided report content

RESPONSE FORMAT (must be valid JSON):
{
    "current_business_situation": "Clear, concise summary of the company's current market position, revenue trends, and operational status",
    "strong_points": ["Point 1", "Point 2", "Point 3", ...],
    "weak_points": ["Point 1", "Point 2", "Point 3", ...],
    "suggestions_for_improvement": ["Suggestion 1", "Suggestion 2", "Suggestion 3", ...],
    "next_strategic_moves": ["Move 1", "Move 2", "Move 3", ...]
}

Each field should contain:
- current_business_situation: 2-3 sentences
- strong_points: 2-4 specific, quantifiable strengths
- weak_points: 1-4 specific weaknesses
- suggestions_for_improvement: 2-6 actionable recommendations
- next_strategic_moves: 1-5 specific, time-based strategic initiatives

Ensure all points are derived from the business report provided."""

    def analyze(self, report_text: str) -> Dict:
        """
        Analyze business report using Gemini API
        
        Args:
            report_text (str): Extracted text from business report
            
        Returns:
            dict: Analysis result in JSON format
        """
        try:
            system_prompt = self.create_system_prompt()
            
            # Prepare the full prompt
            full_prompt = f"""{system_prompt}

BUSINESS REPORT TO ANALYZE:
{report_text[:8000]}"""  # Limit to 8000 chars for API
            
            # Call Gemini API
            response = self.model.generate_content(full_prompt)
            
            # Extract response text
            response_text = response.text.strip()
            
            # Try to parse JSON from response
            analysis_json = self._extract_json(response_text)
            
            if analysis_json:
                return analysis_json
            else:
                # If JSON extraction fails, return error
                return self._create_error_response(response_text)
        
        except Exception as e:
            print(f"Error in Gemini analysis: {str(e)}")
            return self._create_error_response(str(e))
    
    def _extract_json(self, text: str) -> Dict:
        """
        Extract JSON from response text
        
        Args:
            text (str): Response text from API
            
        Returns:
            dict: Parsed JSON or None if extraction fails
        """
        try:
            # Try direct JSON parsing first
            return json.loads(text)
        except json.JSONDecodeError:
            # Try to extract JSON from markdown code block
            json_match = re.search(r'```(?:json)?\s*(.*?)```', text, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group(1))
                except json.JSONDecodeError:
                    pass
            
            # Try to find JSON object pattern
            json_match = re.search(r'\{.*\}', text, re.DOTALL)
            if json_match:
                try:
                    return json.loads(json_match.group(0))
                except json.JSONDecodeError:
                    pass
            
            return None
    
    def _create_error_response(self, error_msg: str) -> Dict:
        """
        Create error response in correct format
        
        Args:
            error_msg (str): Error message
            
        Returns:
            dict: Error response
        """
        return {
            "current_business_situation": "Error analyzing report",
            "strong_points": ["Unable to generate analysis"],
            "weak_points": ["API Error"],
            "suggestions_for_improvement": [error_msg],
            "next_strategic_moves": ["Please try again or contact support"]
        }


# Global analyzer instance
_analyzer = None


def get_analyzer(api_key: str = None) -> GeminiAnalyzer:
    """
    Get or create Gemini analyzer instance
    
    Args:
        api_key (str): Optional API key
        
    Returns:
        GeminiAnalyzer: Analyzer instance
    """
    global _analyzer
    if _analyzer is None:
        _analyzer = GeminiAnalyzer(api_key)
    return _analyzer


def analyze_with_gemini(report_text: str, api_key: str = None) -> Dict:
    """
    Analyze business report with Gemini API
    
    Args:
        report_text (str): Extracted report text
        api_key (str): Optional API key
        
    Returns:
        dict: Analysis result
    """
    analyzer = get_analyzer(api_key)
    return analyzer.analyze(report_text)
