import pandas as pd
import numpy as np

df = pd.read_csv("data/cleaned.csv")

# ==============================
# 1. DATA QUALITY DEGRADATION
# ==============================

df_bad = df.copy()

# inject missing values (10%)
mask = np.random.rand(len(df_bad)) < 0.1
df_bad.loc[mask, "chol"] = np.nan

# ==============================
# 2. NOISE INJECTION
# ==============================

noise = np.random.normal(0, 15, len(df_bad))
df_bad["trestbps"] = df_bad["trestbps"] + noise

# ==============================
# 3. LABEL FLIPPING (ADVERSARIAL)
# ==============================

flip_mask = np.random.rand(len(df_bad)) < 0.05
df_bad.loc[flip_mask, "target"] = 1 - df_bad.loc[flip_mask, "target"]

# ==============================
# 4. SAVE ADVERSARIAL DATA
# ==============================

df_bad.to_csv("data/adversarial_data.csv", index=False)

print("Adversarial dataset created ✔")
