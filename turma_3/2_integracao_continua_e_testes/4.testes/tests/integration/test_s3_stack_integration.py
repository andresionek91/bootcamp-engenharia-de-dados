import boto3

client = boto3.client('s3')


def list_buckets_names():
    response = client.list_buckets()
    buckets_list = response.get('Buckets')
    return [b.get('Name') for b in buckets_list]


def test_bucket_belisco_created_integration():
    assert("meu-bucket-belisco-cdk-testes" in list_buckets_names())

