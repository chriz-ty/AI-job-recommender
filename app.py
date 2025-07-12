# app.py

import streamlit as st
from resume_parser import extract_text_from_pdf, extract_skills
from job_matcher import load_job_descriptions, match_resume_to_jobs

st.set_page_config(page_title="Smart Job Recommender", layout="wide")
st.title("Smart Job Recommender")
st.markdown("Upload your resume and get your top job matches powered by AI! 🔍")

uploaded_file = st.file_uploader("Upload your resume (PDF or .txt)", type=["pdf", "txt"])
job_df = load_job_descriptions("data/sample_jobs.csv")

if uploaded_file:
    with st.spinner("🔍 Extracting resume..."):
        if uploaded_file.type == "application/pdf":
            with open("data/temp_resume.pdf", "wb") as f:
                f.write(uploaded_file.read())
            resume_text = extract_text_from_pdf("data/temp_resume.pdf")
        else:
            resume_text = uploaded_file.read().decode("utf-8")

    st.subheader("📄 Extracted Resume Text")
    st.text_area("", resume_text, height=250)

    resume_skills = extract_skills(resume_text)
    st.subheader("🧠 Skills Detected from Resume")
    if resume_skills:
        st.success(", ".join(resume_skills))
    else:
        st.warning("No recognizable skills found.")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 Top Matches from Job Dataset")
        with st.spinner("🤖 Matching your resume..."):
            matched_jobs = match_resume_to_jobs(resume_text, job_df)

        if not matched_jobs.empty:
            st.dataframe(
                matched_jobs[["title", "similarity_score", "scaled_score"]].head(10).style.format({
                    "similarity_score": "{:.2f}",
                    "scaled_score": "{:.2f}"
                })
            )

            st.download_button(
                "⬇️ Download Full Match Results",
                data=matched_jobs.to_csv(index=False),
                file_name="job_matches.csv",
                mime="text/csv"
            )
        else:
            st.info("No strong job matches found.")

    with col2:
        st.markdown("### 📝 Match with a Custom Job Description")

        custom_job_text = st.text_area("Paste job description from LinkedIn, Indeed, etc.", height=200)
        predict_custom = st.button("🚀 Start Predicting")

        if predict_custom and custom_job_text:

            from job_matcher import clean_text, get_embedding

            resume_emb = get_embedding(resume_text)
            job_emb = get_embedding(custom_job_text)

            from sklearn.metrics.pairwise import cosine_similarity
            sim_score = cosine_similarity([resume_emb], [job_emb])[0][0]

            job_skills = extract_skills(custom_job_text)
            matched_custom = [s for s in resume_skills if s in job_skills]

            st.markdown(f"**🤖 Similarity Score:** `{sim_score:.2f}`")
            if matched_custom:
                st.markdown("**🧠 Matched Skills:**")
                st.success(", ".join(matched_custom))
            else:
                st.warning("No overlapping skills found.")
            st.subheader("🛠 Resume Improvement Suggestions")
            missing_skills = sorted(list(set(job_skills) - set(resume_skills)))

            if missing_skills:
                st.info("You're missing some skills this job requires:")
                st.write(", ".join(missing_skills))
            else:
                st.success("Nice! Your resume covers all key skills from this job.")
