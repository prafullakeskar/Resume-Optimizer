# =========================
# optimizer
# =========================
from skills_db import SKILLS_DB


def extract_skills(text):
    found = set()
    text = text.lower()
    for skills in SKILLS_DB.values():
        for s in skills:
            if s in text:
                found.add(s)
    return found




def missing_skills(resume, jd):
    return extract_skills(jd) - extract_skills(resume)




def bullet_suggestion(skill):
    return f"Designed and delivered solutions leveraging {skill} aligned with business and production requirements."