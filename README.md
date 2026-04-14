# 🫀 CS4074 - Heart Disease Big Data Pipeline

## Project Title
Resilient AI Pipeline for Heart Disease Prediction under Adversarial Big Data Conditions

---

## Team Members
- Dana Mounayer
- Sara Imran

---

## Project Overview
This project builds a scalable big data analytics pipeline for heart disease prediction using Apache Spark (PySpark).

It simulates a real-world healthcare environment where patient data is distributed across multiple hospitals and evaluated under adversarial conditions such as noise, missing values, and label corruption.

---

## Objectives
- Build distributed ML pipeline using Spark
- Simulate multi-hospital healthcare data system
- Evaluate model robustness under adversarial conditions
- Demonstrate big data ETL pipeline design

---

## 🛠 Technologies Used
- Apache Spark (PySpark)
- Python 3.12
- Pandas, NumPy
- Spark MLlib (Logistic Regression)
- Ubuntu Linux
- Git & GitHub

---

## Pipeline Architecture

Data → Cleaning → Hospital Split → Spark ML → Adversarial Testing → Evaluation

---

## Dataset
- UCI Heart Disease Dataset  
https://archive.ics.uci.edu/ml/datasets/heart+Disease

---

## Machine Learning Model
- Logistic Regression (Spark MLlib)
- Input: 13 clinical features
- Output: Binary classification (Heart Disease / No Disease)

---

## Adversarial Component
We simulate real-world data issues:
- Missing values
- Noise injection
- Label flipping
- Data inconsistency across hospitals

---

## Results

| Scenario | Accuracy |
|----------|----------|
| Clean Data | ~0.78 |
| Adversarial Data | ~0.76 |

---
 
## 📁 Project Structure
data/
src/
spark/
models/
notebooks/
venv/
requirements.txt
README.md
---

## How to Run

```bash
# activate environment
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run preprocessing
python3 src/preprocessing.py

# split hospitals
python3 src/split_hospitals.py

# train model
python3 spark/spark_ml.py

# adversarial testing
python3 spark/spark_adversarial_ml.py

