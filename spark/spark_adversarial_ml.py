from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

spark = SparkSession.builder.appName("AdversarialML").getOrCreate()

df = spark.read.csv("data/cleaned.csv", header=True, inferSchema=True)

df = df.dropna()

feature_cols = df.columns[:-1]

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
data = assembler.transform(df).select("features", "target")

train, test = data.randomSplit([0.8, 0.2], seed=42)
from pyspark.sql.functions import rand, when, col

train = train.withColumn(
    "target",
    when(rand() > 0.9, 1 - col("target")).otherwise(col("target"))
)
train = train.sample(withReplacement=True, fraction=1.0, seed=42)  

lr = LogisticRegression(labelCol="target")
model = lr.fit(train)

pred = model.transform(test)

evaluator = MulticlassClassificationEvaluator(
    labelCol="target",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(pred)

print("Adversarial Accuracy =", accuracy)

spark.stop()
