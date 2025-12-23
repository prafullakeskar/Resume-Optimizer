# =========================
# nlp_utils.py
# =========================
import spacy
nlp = spacy.load("en_core_web_sm")


def preprocess(text):
    doc = nlp(text.lower())
    return " ".join(t.lemma_ for t in doc if t.is_alpha and not t.is_stop)