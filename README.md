# ⚖️ Contract Analysis and Risk Assessment Bot

## 🔍 Problem
Small and medium businesses often sign legal contracts without understanding hidden risks, complex clauses, and unfair terms. This leads to legal disputes, financial loss, and compliance issues.

## 💡 Solution
NyayaGen is a GenAI-powered legal assistant that analyzes business contracts and explains complex clauses in simple business language. It detects risky clauses, assigns risk scores, flags ambiguous terms, and generates a downloadable PDF report for legal consultation.

## 🚀 Features
- Contract type detection  
- Clause-by-clause explanation  
- Risk scoring (Low / Medium / High)  
- Risk visualization (bar + pie chart)  
- Ambiguity detection  
- Risky clause highlighting  
- PDF export report  
- Multilingual-ready pipeline (English + Hindi support-ready)  
- No external legal databases used (compliant with hackathon rules)

## 🛠 Tech Stack
- UI: Streamlit  
- NLP: spaCy  
- LLM: GPT-4 / Claude (reasoning layer)  
- PDF Export: FPDF  
- Language: Python  

## 🧩 Architecture
User Upload → Text Extraction → Clause Splitting → NLP Analysis → Risk Detection → LLM Explanation → UI Visualization → PDF Export

## 📌 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py

