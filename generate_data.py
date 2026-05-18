"""
generate_data.py
Generates a realistic dummy patient dataset for readmission prediction.
"""

import pandas as pd
import numpy as np
import random
import os

random.seed(42)
np.random.seed(42)

DIAGNOSES = ["Heart Failure", "Diabetes", "COPD", "Pneumonia", "Sepsis",
             "Kidney Disease", "Stroke", "Hip Fracture", "Cardiac Arrhythmia", "Hypertension"]

DISCHARGE_DISPOSITIONS = ["Home", "Home with Home Health", "SNF", "Rehab Facility", "AMA"]
ADMISSION_TYPES = ["Emergency", "Elective", "Urgent", "Newborn"]
INSURANCE_TYPES = ["Medicare", "Medicaid", "Private", "Self-Pay"]
STATES = ["CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "AZ"]


def _readmission_probability(row):
    """Simulates realistic readmission probability based on clinical factors."""
    prob = 0.10
    if row["age"] > 75:              prob += 0.08
    if row["num_previous_admissions"] > 2: prob += 0.10
    if row["length_of_stay"] > 7:    prob += 0.06
    if row["num_comorbidities"] >= 3: prob += 0.07
    if row["discharge_disposition"] in ["AMA", "SNF"]: prob += 0.08
    if row["insurance_type"] == "Self-Pay": prob += 0.05
    if row["admission_type"] == "Emergency": prob += 0.04
    if row["num_medications"] > 10:  prob += 0.05
    if row["num_lab_procedures"] > 50: prob += 0.03
    if row["num_diagnoses"] > 7:     prob += 0.04
    if row["hba1c_result"] == "Abnormal": prob += 0.04
    return min(prob, 0.75)


def generate_patients(n=10000):
    rows = []
    for i in range(1, n + 1):
        age = int(np.random.normal(65, 15))
        age = max(18, min(95, age))

        num_comorbidities = np.random.poisson(2)
        num_medications = int(np.random.normal(8, 4))
        num_medications = max(1, min(25, num_medications))

        row = {
            "patient_id": f"PAT{i:07d}",
            "age": age,
            "age_group": _age_group(age),
            "gender": random.choice(["M", "F"]),
            "race": random.choices(
                ["White", "Black", "Hispanic", "Asian", "Other"],
                weights=[0.60, 0.18, 0.14, 0.05, 0.03]
            )[0],
            "insurance_type": random.choices(
                INSURANCE_TYPES, weights=[0.45, 0.20, 0.30, 0.05]
            )[0],
            "state": random.choice(STATES),
            "primary_diagnosis": random.choice(DIAGNOSES),
            "admission_type": random.choices(
                ADMISSION_TYPES, weights=[0.55, 0.25, 0.18, 0.02]
            )[0],
            "discharge_disposition": random.choices(
                DISCHARGE_DISPOSITIONS, weights=[0.45, 0.25, 0.15, 0.12, 0.03]
            )[0],
            "length_of_stay": max(1, int(np.random.exponential(5))),
            "num_previous_admissions": np.random.poisson(1),
            "num_comorbidities": num_comorbidities,
            "num_medications": num_medications,
            "num_lab_procedures": int(np.random.normal(45, 20)),
            "num_diagnoses": random.randint(1, 12),
            "hba1c_result": random.choices(["Normal", "Abnormal", "Not Tested"], weights=[0.30, 0.35, 0.35])[0],
            "glucose_result": random.choices(["Normal", "Abnormal", "Not Tested"], weights=[0.35, 0.40, 0.25])[0],
        }

        prob = _readmission_probability(row)
        row["readmitted_30_days"] = int(random.random() < prob)
        rows.append(row)

    return pd.DataFrame(rows)


def _age_group(age):
    if age < 30:  return "18-29"
    if age < 45:  return "30-44"
    if age < 60:  return "45-59"
    if age < 75:  return "60-74"
    return "75+"


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    print("Generating patient dataset...")
    df = generate_patients(10000)

    readmit_rate = df["readmitted_30_days"].mean() * 100
    print(f"  Total patients:     {len(df):,}")
    print(f"  Readmission rate:   {readmit_rate:.1f}%")
    print(f"  Class balance:      {df['readmitted_30_days'].value_counts().to_dict()}")

    df.to_csv("data/patients.csv", index=False)
    print(f"\n  Saved → data/patients.csv  ({os.path.getsize('data/patients.csv')/1024:.1f} KB)")
