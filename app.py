import streamlit as st
from job_recommender import recommend_jobs

st.title("Job Recommendation System")

st.write("Enter your skills below to get job recommendations!")

user_skills = st.text_input("Your skills (comma-separated):")

if st.button("Get Recommendations"):
    if user_skills:
        recommendations = recommend_jobs(user_skills)
        
        st.subheader("Recommended Jobs:")
        for rec in recommendations:
            st.write(f"**{rec['title']}**")
            st.write(f"Description: {rec['description']}")
            st.write(f"Similarity: {rec['similarity']:.2f}")
            st.write("---")
    else:
        st.warning("Please enter your skills.")