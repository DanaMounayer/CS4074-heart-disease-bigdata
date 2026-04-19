from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("HeartDiseaseBigData") \
    .getOrCreate()

# Load ONE hospital (we simulate distributed system later)
df1 = spark.read.csv("data/hospital1.csv", header=True, inferSchema=True)
df2 = spark.read.csv("data/hospital2.csv", header=True, inferSchema=True)
df3 = spark.read.csv("data/hospital3.csv", header=True, inferSchema=True)

# Combine all hospitals (simulating distributed ingestion)
df = df1.union(df2).union(df3)

df.printSchema()
df.show(5)

print("Spark pipeline running successfully ✅")

spark.stop()
