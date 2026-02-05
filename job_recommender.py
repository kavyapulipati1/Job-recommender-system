import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_jobs():
    return pd.read_csv('data/jobs.csv')

def recommend_jobs(user_skills, top_n=3):
    df = load_jobs()
    # Combine JobTitle and JobDescription for better matching
    df['combined'] = df['JobTitle'] + ' ' + df['JobDescription']
    
    # Vectorize
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined'])
    
    # Vectorize user input
    user_vector = vectorizer.transform([user_skills])
    
    # Compute similarity
    similarities = cosine_similarity(user_vector, tfidf_matrix).flatten()
    
    # Get top matches
    top_indices = similarities.argsort()[-top_n:][::-1]
    
    recommendations = []
    for idx in top_indices:
        recommendations.append({
            'title': df.iloc[idx]['JobTitle'],
            'description': df.iloc[idx]['JobDescription'],
            'similarity': similarities[idx]
        })
    
    return recommendations