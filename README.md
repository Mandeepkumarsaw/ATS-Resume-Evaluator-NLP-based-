# 📄 ATS Resume Analyzer (NLP-Based)

An AI-powered Resume Analyzer that evaluates resumes against job descriptions and generates an ATS (Applicant Tracking System) score. This project helps job seekers optimize their resumes by identifying missing keywords and improving alignment with job requirements.

---

## 🚀 Features

* 📤 Upload Resume (PDF)
* 🧾 Paste Job Description
* 📊 ATS Score Calculation
* ✅ Matched Keywords
* ❌ Missing Keywords
* ⚡ Fast and interactive UI using Streamlit

---

## Live Demo🚀
https://resume-analyzer-ats-nlp.streamlit.app/                 

## 🧠 How It Works

1. Extracts text from the uploaded PDF resume
2. Cleans and preprocesses text using NLP techniques
3. Converts text into vectors using **CountVectorizer**
4. Calculates similarity using **Cosine Similarity**
5. Displays ATS score and keyword analysis

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Libraries:**

  * PyPDF2
  * NLTK
  * Scikit-learn

---

## 📁 Project Structure

```
resume-analyzer/
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```
git clone https://github.com/your-username/resume-analyzer.git
```

2. Navigate to the project folder:

```
cd resume-analyzer
```

3. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the App

```
streamlit run app.py
```

---

## 🌐 Output

After running, open your browser and go to:

```
http://localhost:8501
```

---

## 📊 Example

**Job Description:**

> Looking for a Python developer with experience in Machine Learning, SQL, and Data Analysis.

**Output:**

* ATS Score: 75%
* Matched Keywords: Python, Machine Learning
* Missing Keywords: SQL, Data Analysis

---

## 🚀 Future Enhancements

* 🔍 Advanced NLP using spaCy
* 🤖 AI-based resume suggestions
* 📥 Downloadable report (PDF)
* 🌙 Dark/Light mode toggle
* 📈 Skill categorization (Python, ML, SQL, etc.)

---

## 🎯 Use Cases

* Students preparing for placements
* Job seekers optimizing resumes
* HR teams for quick resume screening

---

## 🤝 Contributing

Feel free to fork this repository and improve the project.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Developed by Mandeep Kumar

---

⭐ If you like this project, don't forget to give it a star!
