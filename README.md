# 🚀 AI Resume Analyzer + ATS Scorer
---

## 📌 Overview

**AI Resume Analyzer + ATS Scorer** is an intelligent web application that evaluates resumes against job descriptions using **Natural Language Processing (NLP)** and **Large Language Models (LLMs)**.

It helps job seekers improve their resumes by:

* Calculating an **ATS (Applicant Tracking System) score**
* Identifying **missing keywords and skills**
* Providing **AI-powered suggestions and improvements**
* Rewriting resume bullet points for better impact

---

## ✨ Features

* 📄 Upload Resume (PDF)
* 📊 ATS Score (TF-IDF + Cosine Similarity)
* 🔍 Missing Keyword Detection
* 🤖 AI-Powered Resume Feedback
* ✍️ Smart Bullet Point Rewriting
* ⚡ Fast and Simple UI using Streamlit

---

## 🧠 Tech Stack

* **Python**
* **Streamlit**
* **Scikit-learn (TF-IDF, Cosine Similarity)**
* **OpenAI API (LLM Integration)**
* **PyPDF2 (Resume Parsing)**

---

## 🏗️ Project Architecture

```
Resume (PDF)
   ↓
Text Extraction (PyPDF2)
   ↓
TF-IDF Vectorization
   ↓
Cosine Similarity → ATS Score
   ↓
LLM Analysis → Suggestions & Improvements
   ↓
Streamlit UI → Display Results
```

---

## 📂 Project Structure

```
ai-resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── utils/
│   ├── parser.py
│   ├── similarity.py
│   └── llm.py
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Set OpenAI API Key

#### 🔹 Mac/Linux:

```bash
export OPENAI_API_KEY=your_api_key
```

#### 🔹 Windows:

```bash
set OPENAI_API_KEY=your_api_key
```

---

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🎯 Use Case

* Students applying for internships
* Job seekers optimizing resumes
* Professionals switching careers
* Anyone preparing for ATS-based screening

---

## 🚀 Future Improvements

* 📌 Section-wise resume analysis
* 📊 Detailed scoring breakdown
* 🧠 Advanced keyword extraction (NER)
* 🌐 Deployment (Streamlit Cloud / Render)
* 🔐 User login & dashboard
* 📁 Resume history tracking

---

##  Author

**Joncy Keda - AI Developer**

