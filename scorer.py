# =========================
# scorer
# =========================
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def ats_score(resume, jd):
    vec = TfidfVectorizer()
    tfidf = vec.fit_transform([resume, jd])
    return round(cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]*100, 2)