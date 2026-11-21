# Run from the repo root: python3 patch_data.py
# 1) fixes the requirements of O05 and O06 in data/offers.json
# 2) adds 5 synthetic CVs (C06-C10) to data/cvs.json
import json
NEW_REQ = {"O05": ["powerbi", "databases"],
           "O06": ["html", "css", "javascript", "frontend_framework", "backend"]}
NEW_CVS = [
 {"id": "C06", "skills": ["html","css","javascript","react","typescript","nextjs","python","fastapi","rest_apis","git"],
  "text": "Final-year student in software engineering. Built web applications with React, TypeScript and Next.js for a course project and an internship project. Wrote REST APIs with Python and FastAPI. Uses HTML, CSS, JavaScript and Git daily."},
 {"id": "C07", "skills": ["html","css","javascript","react","typescript","python","fastapi","rest_apis","git"],
  "text": "Third-year computer science student. Built a front-end with React and TypeScript and a small REST API with Python and FastAPI for a group project. Comfortable with HTML, CSS, JavaScript and Git. Has not used Next.js."},
 {"id": "C08", "skills": ["python","machine_learning","deep_learning","tensorflow","pandas","sql"],
  "text": "Final-year student with a data science focus. Trained neural networks (deep learning) with TensorFlow and classical machine learning models in Python. Prepares data with pandas and queries a SQL database. No dashboard or reporting tools."},
 {"id": "C09", "skills": ["devops","docker","linux","networking","bash","python","git"],
  "text": "Final-year student in systems and networks. Set up a small CI/CD pipeline and Docker containers (DevOps) for a course project, administers Linux servers, knows networking basics, writes Bash and Python scripts, and uses Git."},
 {"id": "C10", "skills": ["sql","powerbi","python","statistics"],
  "text": "Final-year data student. Built Power BI dashboards for a class project, wrote SQL queries and Python scripts, and applied basic statistics. Has not worked with Excel beyond simple tables."},
]
offers = json.load(open("data/offers.json", encoding="utf-8"))
for o in offers:
    if o["id"] in NEW_REQ:
        o["requirements"] = NEW_REQ[o["id"]]
json.dump(offers, open("data/offers.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
cvs = json.load(open("data/cvs.json", encoding="utf-8"))
have = {c["id"] for c in cvs}
cvs += [c for c in NEW_CVS if c["id"] not in have]
json.dump(cvs, open("data/cvs.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("offers:", len(offers), "cvs:", len(cvs))
