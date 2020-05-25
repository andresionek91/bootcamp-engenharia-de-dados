import boto3
from datetime import datetime
import json
from faker import Faker
from multiprocessing import Pool
from random import randint

client = boto3.client('kinesis')
faker = Faker(['pt_BR'])


def put_record(data):
    response = client.put_record(
        StreamName='kinesis-stream',
        Data=data,
        PartitionKey='test'
    )
    return response


def create_record(idx):
    Faker.seed(randint(0, 2000))
    fake_data = {
        "current_timestamp": datetime.strftime(datetime.utcnow(), "%Y-%m-%d %H:%m:%S.%f"),
        "name": faker.name(),
        "city": faker.city(),
        "state": faker.state(),
        "postcode": faker.postcode(),
        "email": faker.ascii_free_email(),
        "user_name": faker.user_name()
    }
    bytes_data = json.dumps(fake_data).encode('utf-8')

    return bytes_data


for n in range(600):
    fake_records = map(create_record, range(50))
    pool = Pool()
    pool.map(put_record, fake_records)
    print(n)
