''' stream reader that perfroms processing on the raw IoT data from a 
Kafka topic '''

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import json

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("IoT Data Streaming") \
    .getOrCreate()

input_topic = "raw_iot_data"
output_topic = "processed_iot_data"

# create DataFrame representing the stream of input lines from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", input_topic) \
    .option("startingOffsets", "earliest") \
    .load()

# # Function to check if a string is valid JSON
# def is_json(myjson):
#     try:
#         json_object = json.loads(myjson)
#     except ValueError as e:
#         return False
#     return True

# # Register the function as a UDF (User Defined Function)
# is_json_udf = udf(is_json)

# # Deserialize JSON data only if it's valid
# iot_data_df = df.selectExpr("CAST(value AS STRING) AS json") \
#     .filter(is_json_udf(col("json"))) \
#     .select(from_json("json", "temperature INT, air_pressure INT, humidity INT, TIMESTAMP").alias("data")) \
#     .select("data.*")

