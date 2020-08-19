from pyspark import SparkContext
from pyspark.sql import functions as F
import sys

spark = SparkContext(appName="EventsRawToProcessed")

log4j_logger = spark._jvm.org.apache.log4j
logger = log4j_logger.LogManager.getLogger('CookingData')
logger.info("Pyspark script logger initialized.")

if __name__ == "__main__":
    logger.info(f"Sys Arguments: {sys.argv}")
    streamName, regionName = sys.argv[1:]
    logger.info(f"Sys Arguments: {streamName}, {regionName}")

    kinesisDF = spark \
        .readStream \
        .format("kinesis") \
        .option("streamName", streamName) \
        .option("endpointUrl", f"https://kinesis.{regionName}.amazonaws.com") \
        .option("startingposition", "earliest") \
        .load()

    logger.info(f"Read Stream")

    kinesisDF.selectExpr("cast (data as STRING) jsonData") \
        .withColumn("event_date", F.to_date(F.col("event_timestamp"))) \
        .withColumn('_processed_etl_timestamp', F.current_timestamp()) \
        .writeStream \
        .partitionBy("event_date") \
        .format("parquet") \
        .option("checkpointLocation", "s3://s3-belisco-production-emr/checkpoints/atomic_events") \
        .start("s3://s3-belisco-production-data-lake-processed/atomic_events")
