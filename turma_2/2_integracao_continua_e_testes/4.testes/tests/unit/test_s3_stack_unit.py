import json
from aws_cdk import core
from s3_stack.s3_stack import S3Stack


def get_template():
    app = core.App()
    S3Stack(app, "s3-stack-cdk")
    return json.dumps(app.synth().get_stack("s3-stack-cdk").template)


def test_bucket_created_unit():
    assert("AWS::S3::Bucket" in get_template())


def test_bucket_belisco_created_unit():
    assert("meu-bucket-belisco-cdk" in get_template())

