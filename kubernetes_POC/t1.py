from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf

spark = SparkSession.builder.appName(
    'Rcsv_read').getOrCreate()

taxi_ds = spark.read.csv('data/taxi_tripdata.csv', sep=',', inferSchema=True, header=True)


print('Filter of data travelled more than 5 km')
df_filtered = taxi_ds.filter(taxi_ds["trip_distance"] > 5)
df_filtered.show(10, False)
print('Result from t1')
