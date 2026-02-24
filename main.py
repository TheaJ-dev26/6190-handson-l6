# main.py
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("MusicAnalysis").getOrCreate().conf("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.RawLocalFileSystem")


# Load datasets
logs = spark.read.csv("listening_logs.csv", header=True, inferSchema=True)
meta = spark.read.csv("songs_metadata.csv", header=True, inferSchema=True)

# Join logs with metadata for tasks that need genre
logs_with_meta = logs.join(meta, on="song_id", how="left")


# Task 1: User Favorite Genres
user_genre_time = (
    logs_with_meta
    .groupBy("user_id", "genre")
    .agg(spark_sum("duration_sec").alias("total_genre_time")) 
) 
w = Window.partitionBy("user_id").orderBy(desc("total_genre_time")) 

favorite_genres = ( 
    user_genre_time 
    .withColumn("rank", row_number().over(w)) 
    .filter(col("rank") == 1) 
    .drop("rank") 
)

favorite_genres.write.mode("overwrite").csv("outputs/task1")


# Task 2: Average Listen Time



# Task 3: Create your own Genre Loyalty Scores and rank them and list out top 10


# Task 4: Identify users who listen between 12 AM and 5 AM
