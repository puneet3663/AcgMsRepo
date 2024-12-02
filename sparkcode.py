## Code 1

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


############################### Broad Case Join ************************

data3 = [(1, "DeptA"),
         (2, "DeptB"),
         (3, "DeptC"),
         (4, "DeptD"),
         (5, "DeptE")]

df3=spark.createDataFrame(data3, ["id","department"])

joined_df = df1.join(df2, "id").join(df3.hint("broadcast"), "id")

joined_df.show()

##################### Distinct function #######################

distinctDF = df.distinct()
print("Distinct count: "+str(distinctDF.count()))
distinctDF.show(truncate=False)

##################### Drop Duplicates #######################
df2 = df.dropDuplicates()
print("Distinct count: "+str(df2.count()))
df2.show(truncate=False)

##################### Drop Duplicates on 2 columns only #######################
dropDisDF = df.dropDuplicates(["department","salary"])
print("Distinct count of department & salary : "+str(dropDisDF.count()))
dropDisDF.show(truncate=False)

##################### repartition #######################
df2 = df.repartition(6)
print(df2.rdd.getNumPartitions())

################ UDF example ############################

# reference link from where code is taken https://sparkbyexamples.com/pyspark/pyspark-udf-user-defined-function/
       
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

columns = ["Seqno","Name"]
data = [("1", "john jones"),
    ("2", "tracey smith"),
    ("3", "amy sanders")]

df = spark.createDataFrame(data=data,schema=columns)

df.show(truncate=False)

from pyspark.sql.functions import col, udf
from pyspark.sql.types import StringType

def convertCase(str):
    resStr=""
    arr = str.split(" ")
    for x in arr:
       resStr= resStr + x[0:1].upper() + x[1:len(x)] + " "
    return resStr 

spark.udf.register("convertUDF", convertCase,StringType())
df.createOrReplaceTempView("NAME_TABLE")
spark.sql("select Seqno, convertUDF(Name) as Name from NAME_TABLE") \
     .show(truncate=False)

#output is 
Seqno|Name         |
+-----+-------------+
|1    |John Jones   |
|2    |Tracey Smith |
|3    |Amy Sanders  |
+-----+-------------+
         

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################

############################################
