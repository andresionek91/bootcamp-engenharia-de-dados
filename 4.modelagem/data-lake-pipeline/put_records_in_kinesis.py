import boto3
import json
from fake_web_events import Simulation
import os


client = boto3.client('kinesis')


def put_record(event):
    data = json.dumps(event).encode('utf-8')
    response = client.put_record(
        StreamName='kinesis-raw-events-stream',
        Data=data
    )
    return response


simulation = Simulation(user_pool_size=100, sessions_per_day=10000)
events = simulation.run(duration_seconds=600)

for event in events:
    put_record(event)
