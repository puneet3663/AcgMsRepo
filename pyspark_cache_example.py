from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum

# Create a SparkSession
spark = SparkSession.builder.appName("CachingExample").getOrCreate()

# Read the large dataset
df = spark.read.format("csv").load("path/to/your/data.csv", header=True, inferSchema=True)

# Filter the data (expensive operation)
filtered_df = df.filter(col("column_name") > 1000)

# Cache the filtered DataFrame
filtered_df.cache()

# Aggregate the filtered data (expensive operation)
aggregated_df = filtered_df.groupBy("category").agg(sum("amount").alias("total_amount"))

# Cache the aggregated DataFrame
aggregated_df.cache()

# Join the aggregated DataFrame with another DataFrame multiple times
small_df = spark.read.format("csv").load("path/to/small_data.csv", header=True, inferSchema=True)

# First join
joined_df1 = aggregated_df.join(small_df, "common_column")

# Second join
joined_df2 = aggregated_df.join(small_df, "common_column")

# Third join
joined_df3 = aggregated_df.join(small_df, "common_column")

# Trigger the actions to force caching
joined_df1.show()
joined_df2.show()
joined_df3.show()

# Unpersist the cached DataFrames when no longer needed
filtered_df.unpersist()
aggregated_df.unpersist()
