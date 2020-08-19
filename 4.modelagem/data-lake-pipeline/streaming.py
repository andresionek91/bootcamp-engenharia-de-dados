from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import sys
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName('RawToProcessedStream') \
    .getOrCreate()

log4j_logger = spark._jvm.org.apache.log4j
logger = log4j_logger.LogManager.getLogger('CookingData')
logger.info("Pyspark script logger initialized.")


if __name__ == "__main__":
    logger.info(f"Sys Arguments: {sys.argv}")
    streamName, regionName = sys.argv[1:]
    logger.info(f"Sys Arguments: {streamName}, {regionName}")

    dataSchema = StructType() \
        .add("event_timestamp", TimestampType()) \
        .add("event_type", StringType()) \
        .add("page_url", StringType()) \
        .add("page_url_path", StringType()) \
        .add("referer_url", StringType()) \
        .add("referer_url_scheme", StringType()) \
        .add("referer_url_port", StringType()) \
        .add("referer_medium", StringType()) \
        .add("utm_medium", StringType()) \
        .add("utm_source", StringType()) \
        .add("utm_content", StringType()) \
        .add("utm_campaign", StringType()) \
        .add("click_id", StringType()) \
        .add("geo_latitude", LongType()) \
        .add("geo_longitude", LongType()) \
        .add("geo_country", StringType()) \
        .add("geo_timezone", StringType()) \
        .add("geo_region_name", StringType()) \
        .add("ip_address", StringType()) \
        .add("browser_name", StringType()) \
        .add("browser_user_agent", StringType()) \
        .add("browser_language", StringType()) \
        .add("os", StringType()) \
        .add("os_name", StringType()) \
        .add("os_timezone", StringType()) \
        .add("device_type", StringType()) \
        .add("device_is_mobile", BooleanType()) \
        .add("user_custom_id", StringType())  \
        .add("user_domain_id", StringType())

    logger.info(f"Python Schema")

    kinesisDF = spark \
        .readStream \
        .format("kinesis") \
        .option("streamName", streamName) \
        .option("endpointUrl", f"https://kinesis.{regionName}.amazonaws.com") \
        .option("initialPosition", "TRIM_HORIZON") \
        .load()

    logger.info(f"Read Stream")

    kinesisDF = kinesisDF.selectExpr("cast(data as STRING) as jsonData") \
        .select(F.from_json("jsonData", dataSchema).alias("event")) \
        .select("event.*") \
        .withColumn('_processed_etl_timestamp', F.current_timestamp())

    query = kinesisDF.writeStream \
        .format("parquet") \
        .option("checkpointLocation", "s3://s3-belisco-production-emr/checkpoints/atomic_events") \
        .start("s3://s3-belisco-production-data-lake-processed/atomic_events")

    query.awaitTermination()
