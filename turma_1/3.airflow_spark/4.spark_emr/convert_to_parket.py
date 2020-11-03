from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName('to_parquet') \
    .getOrCreate()

for coin in ['BTC', 'BCH', 'ETH', 'LTC']:
    df = spark.read.format('json').load(f's3a://s3-belisco-production-data-lake-raw/cryptocurrency/{coin}')
    df.write.format('parquet').save(path=f's3a://s3-belisco-production-data-lake-processed/cryptocurrency/{coin}', mode='overwrite')
