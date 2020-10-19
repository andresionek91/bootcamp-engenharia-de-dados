import boto3
import json
from datetime import datetime
import logging

logging.getLogger().setLevel(logging.INFO)

client = boto3.client('s3')


def upload_to_s3(bucket, schema, table, partition, json_data):
    """
    Upload json file to S3 using Boto3
    """
    now = datetime.now()
    now_string = now.strftime("%Y-%m-%d-%H-%M-%S-%f")
    key = f'{schema}/{table}/execution_date={partition}/{schema}_{table}_{now_string}.json'

    logging.info(f'Uploading file to S3 with key: {key}')

    bin_data = json.dumps(json_data).encode('utf-8')
    return client.put_object(Body=bin_data, Bucket=bucket, Key=key)
