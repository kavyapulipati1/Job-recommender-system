
# 💼 Job Recommendation System (NLP + Machine Learning)

## 📌 Project Overview
This project is an **NLP-based Job Recommendation System** that suggests the most relevant job roles for a candidate by matching their resume text with job descriptions.

The system uses Natural Language Processing techniques to extract important skills and keywords, and recommends jobs based on similarity scoring.

---

## 🎯 Key Features
✅ Resume and job description text preprocessing  
✅ TF-IDF Vectorization for feature extraction  
✅ Cosine Similarity for job-role matching  
✅ Ranked job recommendations based on skill similarity  
✅ Interactive Streamlit Web Application  

---

## 🛠 Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Natural Language Processing (NLP)  
- Streamlit  

---

## 📂 Project Structure

job-recommendation-system/
│
├── data/
│ └── jobs.csv # Job descriptions dataset
│
├── job_recommender.py # Core recommendation script
├── app.py # Streamlit web app
├── requirements.txt # Required libraries
└── README.md # Project documentation


---

## 📊 Dataset
A sample job dataset is used containing job titles and required skills such as:

- Data Scientist  
- AI/ML Engineer  
- Software Engineer  
- Cloud Engineer  
- Business Analyst  
- NLP Engineer  

---

## ⚙️ How It Works
1. Resume text is taken as input  
2. Job descriptions are converted into numerical vectors using **TF-IDF**  
3. **Cosine similarity** is applied to measure relevance  
4. Jobs are ranked and recommended based on similarity score  

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
Run the Streamlit Web App
streamlit run app.py


The application will open in your browser at:

http://localhost:8501

📌 Output

The system generates a ranked list of recommended jobs with similarity scores.

Example:

Job Title	Score
Data Scientist	0.82
Data Analyst	0.76
AI Engineer	0.65
