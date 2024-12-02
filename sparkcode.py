pip install pyspark

from pyspark.sql import SparkSession

spark=SparkSession.builder.getOrCreate()

data1 = [("Alice", 1, 1000, "Address1"),
         ("Bob", 2, 2000, "Address2"),
         ("Charlie", 3, 3000, "Address3"),
         ("David", 4, 4000, "Address4"),
         ("Eve", 5, 5000, "Address5")]

data2 = [(1, 25, "Married"),
         (2, 30, "Single"),
         (3, 28, "Married"),
         (4, 32, "Single"),
         (5, 27, "Married")]

df1 = spark.createDataFrame(data1, ["student_name", "id", "salary", "address"])
df2 = spark.createDataFrame(data2, ["id", "age", "married_status"])

joined_df=df1.join(df2,"id")

joined_df.show()
spark.stop()
