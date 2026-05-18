# 🏥 Patient 30-Day Readmission Predictor

An end-to-end machine learning pipeline that predicts 30-day hospital readmission risk using patient clinical and demographic data.

---

## 📊 Project Overview

Hospital readmissions within 30 days are a key quality indicator and a major cost driver in healthcare. This project builds and evaluates multiple ML models to identify high-risk patients at discharge, enabling care teams to intervene proactively.

**Stack:** Python · scikit-learn · pandas · matplotlib · Jupyter

---

## 🎯 Models Compared

| Model | ROC-AUC | Notes |
|-------|---------|-------|
| Logistic Regression | ~0.72 | Strong baseline, interpretable |
| Decision Tree | ~0.70 | Clinically explainable rules |
| Random Forest | ~0.78 | Best overall performance ✅ |
| Gradient Boosting | ~0.77 | Close second |

---

## 📁 Repository Structure

```
patient-readmission-predictor/
├── generate_data.py                      # Generates realistic dummy patient dataset
├── notebooks/
│   └── readmission_predictor.ipynb       # Full ML pipeline: EDA → models → evaluation
├── data/                                 # Generated CSV + output charts (git-ignored)
├── requirements.txt
└── .gitignore
```

---

## 🔍 Key Features Used

- Age, gender, race, insurance type
- Primary diagnosis, admission type, discharge disposition
- Length of stay, number of previous admissions
- Number of comorbidities, medications, diagnoses, lab procedures
- HbA1c result, glucose result

---

## 💡 Key Clinical Findings

- **Previous admissions** and **length of stay** are the strongest readmission predictors
- Patients discharged **Against Medical Advice (AMA)** have significantly higher risk
- **Abnormal HbA1c** is a major risk factor — diabetic management at discharge is critical
- **Medicare/Medicaid** patients show higher readmission rates vs private insurance
- Higher **comorbidity burden** substantially increases 30-day readmission probability

---

## 🚀 Setup & Usage

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Generate the dataset
```bash
python generate_data.py
```

### 3. Run the full ML pipeline
```bash
jupyter notebook notebooks/readmission_predictor.ipynb
```
Run all cells — the notebook covers EDA, preprocessing, model training, ROC curves, confusion matrix, and feature importance.

---

## 👤 Author

**Mahek Patel**
- GitHub: [@mahekpatelmdp](https://github.com/mahekpatelmdp)
- LinkedIn: [https://linkedin.com/in/yourprofile](https://www.linkedin.com/in/mahek-patel-8ba264286)

---

## 📝 License

MIT License
