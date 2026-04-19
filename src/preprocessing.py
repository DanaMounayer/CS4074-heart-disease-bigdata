import pandas as pd

df = pd.read_csv("data/heart.csv", header=None)

df.columns = [
    "age","sex","cp","trestbps","chol","fbs","restecg",
    "thalach","exang","oldpeak","slope","ca","thal","target"
]

df = df.replace("?", None)
df = df.dropna()

df["target"] = df["target"].apply(lambda x: 1 if int(x) > 0 else 0)

df.to_csv("data/cleaned.csv", index=False)

print("DONE CLEANING ✅")
