from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_similarity(resume, jd):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([resume, jd])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)

def get_missing_keywords(resume, jd):
    jd_words = set(jd.lower().split())
    resume_words = set(resume.lower().split())

    missing = jd_words - resume_words
    return list(missing)[:20]
