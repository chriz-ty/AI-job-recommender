# 💼 Smart Job Recommender

An AI-powered job recommender system that analyzes a candidate's resume, extracts key skills, and intelligently matches them with suitable job descriptions using NLP and deep learning techniques. It also allows users to compare their resume to any custom job description (e.g., from LinkedIn, Indeed,..) and get similarity scores and skill match insights.

---

## 🚀 Demo Preview

![video](
https://github.com/user-attachments/assets/fdad644b-616e-4b2d-a825-4c9d138bb716
)



---

## Hosted Here: [visit Site](https://ai-job-recommender-bychriz.streamlit.app/)
---
## 📌 Features

✅ Upload your **resume (PDF/txt)**  
✅ Extract and display **skills from your resume**  
✅ Match resume with **99+ job descriptions** using NLP  
✅ Paste a **custom job description** to get a similarity score  
✅ Shows **matched vs missing skills** for improvement  
✅ Download top match results as a **CSV**

---

## 🧠 Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 Python | Core programming language |
| 🧾 Streamlit | Web interface for app |
| 📦 Pandas | Data handling (CSV, DataFrames) |
| 🤖 Sentence-Transformers (BERT) | Text embedding & similarity |
| 📄 PyMuPDF (`fitz`) | PDF parsing |
| 📊 scikit-learn | Cosine similarity |
| 🔍 Regex & NLP | Text cleaning and skill extraction |

---

## 📚 Project Workflow

### 1. **Resume Upload**
- Accepts `.pdf` or `.txt` files
- Extracts raw text using `PyMuPDF` (for PDFs)

### 2. **Skill Extraction**
- Detects both technical and soft skills
- Compares text against a custom keyword list
- Displayed for user reference and further comparison

### 3. **Job Dataset Matching**
- Job descriptions are read from a CSV file (`sample_jobs.csv`)
- Each job description and the resume are embedded using `paraphrase-MiniLM-L6-v2` from `sentence-transformers`
- Cosine similarity is computed
- Results are ranked, scaled, and displayed with download option

### 4. **Custom Job Description Comparison**
- Users can paste a job description from LinkedIn, Indeed, etc.
- The app compares the custom job and the resume
- Shows similarity score and matched/missing skills

### 5. **Resume Improvement Suggestions**
- If a skill is required in the job but missing in the resume, it's suggested as a potential improvement

---

## 📁 Project Structure
```
Smart-Job-Recommender/
│
├── app.py # Main Streamlit app
├── resume_parser.py # Resume text and skill extractor
├── job_matcher.py # Job loading, cleaning, embedding, similarity logic
├── data/
│ └── sample_jobs.csv # Dataset of sample job descriptions
├── requirements.txt
└── README.md
```

---

## 🧪 Sample Jobs Dataset

Your job dataset (`sample_jobs.csv`) includes 99+ jobs across domains:

- 👨‍💻 Software, Data Science, AI, DevOps  
- 📊 Business, Marketing, Sales  
- 🎨 Design, Art, UX  
- 🧪 Research, Education, Content Writing  
- ⚙️ Engineering, Non-tech roles too  

Each job entry has: `job_id`, `title`, `company`, `description`

---

## 🧠 Models Used

### 📌 Sentence Transformer (BERT-based)
- Model: `paraphrase-MiniLM-L6-v2`
- Purpose: Converts resume & job descriptions to dense vector embeddings
- Benefits:
  - Understands meaning/context
  - Works well for semantic matching
  - Lightweight and fast for web apps

### 📌 Cosine Similarity (sklearn)
- Measures vector similarity between resume and job text
- Higher score = better match

---

## ⚙️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/smart-job-recommender.git
cd smart-job-recommender

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🧭 What's next?????
- ✅ Resume keyword highlighting
- ✅ Visual charts (skill match bars, radar plots)
- 🔐 User authentication and profile saving
- 🌐 Multi-language support (translate job/resume)
- 📄 Generate resume suggestions dynamically
- 🧠 Use OpenAI/GPT for deeper resume analysis

## 📜 License
This project is licensed under the MIT License.

Built by:
Christy Maria Sebastian
Linkedin: [Christy Maria Sebastian](https://www.linkedin.com/in/christymariasebastian/)
