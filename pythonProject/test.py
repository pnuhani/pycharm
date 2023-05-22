import os
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,expr, sum
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
import pandas as pd
spark = SparkSession.builder \
    .appName("Excel to DataFrame") \
    .getOrCreate()
# Example file path in Windows
file_path = 'C:\\app\\sample.xlsx'
excel_data = pd.read_excel(file_path)
spark_df = spark.createDataFrame(excel_data)
spark_df = spark_df.withColumn('num_of_days', col('num_of_days').cast('integer'))

sum_open_price = spark_df.filter(col('business_date') >= expr('date_sub(business_date, num_of_days)')) \
                   .groupBy() \
                   .agg(sum('open_price').alias('sum_open_price'))

sum_open_price.show()
spark.stop()