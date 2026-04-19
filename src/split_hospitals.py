import pandas as pd

df = pd.read_csv("data/cleaned.csv")

# IMPORTANT FIX: reset index
df = df.reset_index(drop=True)

# shuffle dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# split into hospitals
h1 = df.iloc[:int(0.3 * len(df))]
h2 = df.iloc[int(0.3 * len(df)):int(0.6 * len(df))]
h3 = df.iloc[int(0.6 * len(df)):]

h1.to_csv("data/hospital1.csv", index=False)
h2.to_csv("data/hospital2.csv", index=False)
h3.to_csv("data/hospital3.csv", index=False)

print("Hospitals created successfully ✅")
