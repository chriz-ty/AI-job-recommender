# resume_parser.py

import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

def extract_skills(text):
    skill_keywords = [
        # Technical Skills
        "python", "java", "c++", "c#", "sql", "mysql", "postgresql", "mongodb",
        "html", "css", "javascript", "typescript", "react", "angular", "vue", "node.js",
        "flask", "django", "spring", "express", "git", "github", "bitbucket",
        "aws", "azure", "gcp", "linux", "docker", "kubernetes", "jenkins",
        "tensorflow", "keras", "pytorch", "sklearn", "opencv", "nlp", "llm",
        "machine learning", "deep learning", "data analysis", "data science",
        "power bi", "tableau", "excel", "pandas", "numpy", "matplotlib", "seaborn",
        "hadoop", "spark", "airflow", "etl", "bigquery", "snowflake",
        "api", "rest", "graphql", "firebase", "supabase", "testing", "unit testing",

        # Business & Non-Technical
        "project management", "business analysis", "marketing", "digital marketing",
        "seo", "sem", "content writing", "copywriting", "email marketing", 
        "social media", "market research", "crm", "salesforce", "hubspot",
        "financial analysis", "accounting", "bookkeeping", "customer service",
        "data entry", "operations", "logistics", "supply chain", "administration",
        "product management", "user research", "ux", "ui", "design thinking",

        # Soft Skills
        "communication", "leadership", "teamwork", "problem solving", 
        "adaptability", "creativity", "time management", "critical thinking",
        "collaboration", "empathy", "attention to detail", "multitasking", 
        "negotiation", "public speaking", "presentation", "work ethic",
        "decision making", "emotional intelligence", "conflict resolution"
    ]
    text = text.lower()
    found = set()
    for skill in skill_keywords:
        if skill in text:
            found.add(skill)
    return list(found)
