# Resilient AI Pipeline for Heart Disease Prediction under Adversarial Big Data Conditions

**Effat University — CS4074 Big Data Analytics**  
Dana Mounayer · Sara Imran

---

## Overview

This project builds a scalable big data analytics pipeline for heart disease prediction using **Apache Spark (PySpark)** and **Kafka-style streaming**. It simulates a real-world multi-hospital healthcare environment where patient data is distributed across three hospital nodes and evaluated under adversarial conditions — sensor noise, label poisoning, missing values, and feature drift.

A **federated learning** extension trains models locally per hospital and aggregates weights using the FedAvg algorithm, enabling collaborative training without any hospital sharing raw patient data.

**Best result:** Logistic Regression — **84.85% baseline accuracy** · Federated model within **1.5% of centralised baseline**

---

## Repository Structure

```
CS4074-heart-disease-bigdata/
│
├── data/
│   ├── cleaned.csv               # Full preprocessed UCI dataset (297 records)
│   ├── hospital1.csv             # Hospital A partition (99 records)
│   ├── hospital2.csv             # Hospital B partition (99 records)
│   └── hospital3.csv             # Hospital C partition (99 records)
│
├── spark/
│   ├── spark_ml.py               # Spark MLlib Logistic Regression pipeline
│   └── spark_adversarial_ml.py   # Adversarial testing with Spark ML
│
├── src/
│   ├── preprocessing.py          # Data cleaning and StandardScaler normalisation
│   └── split_hospitals.py        # Splits cleaned.csv into 3 hospital partitions
│
├── Final_System_Demo.ipynb                  # Complete end-to-end demo notebook
├── KafkaStreaming_federatedLearning.ipynb   # Kafka simulation + federated learning
├── heart_disease_federated_learning.ipynb  # Federated learning (FedAvg, 5 rounds)
│
├── requirements.txt
└── README.md
```

---

## Dataset

**UCI Heart Disease Dataset** — 297 records, 13 clinical features, binary target (heart disease yes/no)

| Feature | Description |
|---|---|
| `age` | Patient age in years |
| `sex` | Sex (1=male, 0=female) |
| `cp` | Chest pain type (1–4) |
| `trestbps` | Resting blood pressure (mmHg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl |
| `restecg` | Resting ECG results |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of peak exercise ST segment |
| `ca` | Number of major vessels (0–3) |
| `thal` | Thalassemia type |
| `target` | **0 = No Disease, 1 = Disease** |

**Class distribution:** 160 healthy (53.9%) · 137 disease (46.1%)  
Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)

---

## Installation

```bash
# 1. Clone
git clone https://github.com/DanaMounayer/CS4074-heart-disease-bigdata.git
cd CS4074-heart-disease-bigdata

# 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt
```

---

## How to Run

### Option A — Full demo notebook (recommended)
```bash
jupyter notebook Final_System_Demo.ipynb
```
Run all cells in order. The notebook walks through every stage with explanations.

### Option B — Run pipeline scripts individually
```bash
# Step 1: Preprocess data
python3 src/preprocessing.py

# Step 2: Split into hospital partitions
python3 src/split_hospitals.py

# Step 3: Train Spark ML model
python3 spark/spark_ml.py

# Step 4: Adversarial testing
python3 spark/spark_adversarial_ml.py
```

### Option C — Federated learning
```bash
jupyter notebook heart_disease_federated_learning.ipynb
```

---

## Pipeline Architecture

```
Patient Data (3 Hospitals)
        │
        ▼
┌─────────────────────┐
│  Data Ingestion     │  Load CSV, schema validation
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Preprocessing      │  StandardScaler, median imputation, hospital split
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Kafka Streaming    │  Sliding window buffer, real-time record ingestion
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Spark ML Training  │  Logistic Regression (MLlib) — 84.85% accuracy
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Adversarial Test   │  Noise + label flip + missing values
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Federated Learning │  FedAvg across 3 hospitals, 5 rounds
└─────────────────────┘
```

---

## Key Results

| Condition | Accuracy | Drop |
|---|---|---|
| Baseline (clean data) | **84.85%** | — |
| Feature noise (σ=15) | 83.50% | −1.4% |
| Label poisoning (5%) | 81.90% | −3.0% |
| Missing values (10%) | 83.10% | −1.8% |
| Federated model | 83.35% | −1.5% |

**Key finding:** Label poisoning is the most damaging adversarial condition — even a 5% label flip rate degrades accuracy more than sensor noise or missing values. Annotation quality review is more impactful than sensor calibration for model performance.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Apache Spark / PySpark | Distributed ML training (MLlib) |
| Kafka (simulated) | Real-time streaming ingestion |
| scikit-learn | Local model training, preprocessing |
| Pandas / NumPy | Data manipulation |
| Matplotlib / Seaborn | Visualisations |
| Jupyter Notebook | Interactive development and demo |

---

## Authors

| Name | Email |
|---|---|
| Dana Mounayer | dtalmounayer@effat.edu.sa |
| Sara Imran | saraimran@effat.edu.sa |

Effat University — CS4074 Big Data Analytics — 2025

