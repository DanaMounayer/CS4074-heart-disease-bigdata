# 🫀 CS4074 - Heart Disease Big Data Pipeline

## Project Title
**Resilient AI Pipeline for Heart Disease Detection Using Distributed Machine Learning under Adversarial Big Data Conditions**

---

## Team Members
- Dana Mounayer
- Sara Imran

---

## Project Overview
This project implements a scalable big data analytics pipeline for heart disease prediction using Apache Spark and PySpark.

The system simulates a real-world healthcare environment where patient data is distributed across multiple hospitals. It also introduces adversarial conditions such as noise, missing values, and label corruption to evaluate model robustness.

The project follows the meta-theme:
> **Resilient AI Pipelines in Adversarial Big Data Ecosystems**

---

## Technologies Used
- Apache Spark (PySpark)
- Python 3.12
- Pandas / NumPy
- Hadoop-style distributed processing (simulated)
- Machine Learning (Logistic Regression - Spark MLlib)
- Ubuntu VM Environment

---

## Project Pipeline

1. Data Collection (UCI Heart Disease Dataset)
2. Data Cleaning & Preprocessing
3. Distributed Hospital Data Simulation
4. Feature Engineering
5. Spark ML Model Training
6. Adversarial Data Simulation
7. Model Evaluation

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
| Adversarial Data | ~0.85 |

---

## How to Run the Project

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run preprocessing
python3 src/preprocessing.py

# 4. Split hospitals
python3 src/split_hospitals.py

# 5. Train Spark ML model
python3 spark/spark_ml.py

# 6. Run adversarial model
python3 spark/spark_adversarial_ml.py


## 📁 Project Structure
data/
src/
spark/
models/
notebooks/
venv/
README.md
requirements.txt

