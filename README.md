# Resume Tracking System

## Overview

The Resume Tracking System is a Streamlit-based web application designed to analyze resumes and provide insights based on job descriptions. The application leverages PDF processing to extract information from resumes and uses Google Generative AI for various analyses and enhancements.

## Features

- **Upload Resume:** Users can upload a PDF resume for analysis.
- **Job Description Input:** Users can enter a job description for comparison.
- **Generate Insights:**
  - Analyze the resume in relation to the job description.
  - Provide suggestions for improving skills.
  - Calculate the percentage match between the resume and job description.
  - Revise the resume to enhance its appeal for an internship.

## Technologies Used

- **Streamlit:** For building the interactive web interface.
- **PDF Processing:** Using `pdf2image` or `PyMuPDF` to convert PDF pages to images.
- **Google Generative AI:** For generating responses and analysis based on the resume and job description.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/resume-tracking-system.git
cd resume-tracking-system
