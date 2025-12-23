# =========================
# app (Flask API)
# =========================
from flask import Flask, render_template, request
import os

from parser import extract_pdf_text
from nlp_utils import preprocess
from scorer import ats_score
from optimizer import missing_skills, bullet_suggestion

UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        # ---- Resume file ----
        resume_file = request.files["resume"]
        resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
        resume_file.save(resume_path)

        resume_text = extract_pdf_text(resume_path)

        # ---- Job Description (pasted from web) ----
        jd_text = request.form["jd"]

        # ---- Preprocess ----
        resume_clean = preprocess(resume_text)
        jd_clean = preprocess(jd_text)

        # ---- ATS Score ----
        score = ats_score(resume_clean, jd_clean)

        # ---- Missing Skills ----
        missing = missing_skills(resume_text, jd_text)

        # ---- Suggestions ----
        suggestions = [bullet_suggestion(skill) for skill in missing]

        result = {
            "score": score,
            "missing_skills": missing,
            "suggestions": suggestions
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)
