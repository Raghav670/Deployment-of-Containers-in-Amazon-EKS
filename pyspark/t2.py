from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when


spark = SparkSession.builder.appName('Transformations').getOrCreate()


taxi_ds = spark.read.csv('data/taxi_tripdata.csv', sep=',', inferSchema=True, header=True)


df_kms = taxi_ds.withColumn('trip_distance_km', col('trip_distance') * 1.60934)


df_classified = df_kms.withColumn('trip_category', when(col('trip_distance_km') < 5, 'Short') \
                                           .when((col('trip_distance_km') >= 5) & (col('trip_distance_km') < 10), 'Medium') \
                                           .otherwise('Long'))


print('Total Fare data')

df_total_fare = df_classified.withColumn('total_fare', col('fare_amount') + col('tip_amount'))


df_total_fare.show(10, False)

print('Result from t2')
