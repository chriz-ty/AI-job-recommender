# job_matcher.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from resume_parser import extract_skills


model = SentenceTransformer("sentence-transformers/paraphrase-mpnet-base-v2")

def clean_text(text):
    return text.replace("\n", " ").strip().lower()

def get_embedding(text):
    return model.encode(clean_text(text))

def load_job_descriptions(filepath):
    df = pd.read_csv(filepath)
    df["description"] = df["description"].astype(str).apply(clean_text)
    df["job_skills"] = df["description"].apply(extract_skills)
    return df

def match_resume_to_jobs(resume_text, job_df, threshold=0.25):
    resume_embedding = get_embedding(resume_text)
    job_embeddings = job_df["description"].apply(get_embedding).tolist()
    
    similarities = cosine_similarity([resume_embedding], job_embeddings)[0]
    job_df["similarity_score"] = similarities
    job_df["scaled_score"] = job_df["similarity_score"] / job_df["similarity_score"].max()

    # Filter weak matches
    job_df = job_df[job_df["similarity_score"] > threshold]

    return job_df.sort_values(by="similarity_score", ascending=False).reset_index(drop=True)
