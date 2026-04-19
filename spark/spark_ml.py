from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression

spark = SparkSession.builder.appName("HeartML").getOrCreate()

# Load hospital data
df = spark.read.csv("data/cleaned.csv", header=True, inferSchema=True)

# Convert target column
df = df.withColumn("target", df["target"].cast("int"))

# Feature columns
feature_cols = df.columns[:-1]

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data = assembler.transform(df).select("features", "target")

# Train/test split
train, test = data.randomSplit([0.8, 0.2], seed=42)

# Model
lr = LogisticRegression(labelCol="target")
model = lr.fit(train)

# Predictions
predictions = model.transform(test)

predictions.select("features", "target", "prediction").show(5)

print("ML MODEL COMPLETED ✅")

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(
    labelCol="target",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(predictions)
print("Accuracy =", accuracy)

spark.stop()
