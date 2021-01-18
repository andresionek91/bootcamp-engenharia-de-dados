#!/usr/bin/env python3
from enum import Enum
from typing import Type

from aws_cdk import core
from aws_cdk import (
    aws_s3 as s3,
    aws_glue as glue,
    aws_iam as iam
)
from environment import Environment


class DataLakeLayer(Enum):
    RAW = 'raw'
    PROCESSED = 'processed'
    CURATED = 'curated'


class BaseDataLakeBucket(s3.Bucket):
    """
    Base class to create a data lake bucket
    """
    def __init__(self, scope: core.Construct, deploy_env: Environment, layer: DataLakeLayer, **kwargs) -> None:
        self.deploy_env = deploy_env
        self.layer = layer
        self.name = f's3-belisco-{self.deploy_env.value}-data-lake-{self.layer.value}'

        super().__init__(
            scope,
            self.name,
            bucket_name=self.name,
            block_public_access=self.default_block_public_access(),
            encryption=self.default_encryption(),
            versioned=True,
            **kwargs
        )

        self.set_default_lifecycle_rules()

    @staticmethod
    def default_block_public_access():
        """
        Block public access by default
        """
        block_public_access = s3.BlockPublicAccess(
            block_public_acls=True,
            block_public_policy=True,
            ignore_public_acls=True,
            restrict_public_buckets=True
        )
        return block_public_access

    @staticmethod
    def default_encryption():
        """
        Enables encryption by default
        """
        encryption = s3.BucketEncryption(s3.BucketEncryption.S3_MANAGED)
        return encryption

    def set_default_lifecycle_rules(self):
        """
        Sets lifecycle rule by default
        """
        self.add_lifecycle_rule(
            abort_incomplete_multipart_upload_after=core.Duration.days(7),
            enabled=True
        )

        self.add_lifecycle_rule(
            noncurrent_version_transitions=[
                s3.NoncurrentVersionTransition(
                    storage_class=s3.StorageClass.INFREQUENT_ACCESS,
                    transition_after=core.Duration.days(30)
                ),
                s3.NoncurrentVersionTransition(
                    storage_class=s3.StorageClass.GLACIER,
                    transition_after=core.Duration.days(60)
                )
            ]
        )

        self.add_lifecycle_rule(
            noncurrent_version_expiration=core.Duration.days(360)
        )


class BaseDataLakeGlueDatabase(glue.Database):
    """
    Creates a glue database associated to a data lake bucket
    """

    def __init__(self, scope: core.Construct, data_lake_bucket: BaseDataLakeBucket, **kwargs) -> None:
        self.data_lake_bucket = data_lake_bucket
        self.name = f'glue-belisco-{self.data_lake_bucket.deploy_env.value}-data-lake-{self.data_lake_bucket.layer.value}'

        super().__init__(
            scope,
            self.name,
            database_name=self.database_name,
            location_uri=self.location_uri
        )

    @property
    def database_name(self):
        """
        Returns the glue database name
        """
        return self.name.replace("-", "_")

    @property
    def location_uri(self):
        """
        Returns the database location
        """
        return f's3://{self.data_lake_bucket.bucket_name}'


class BaseDataLakeGlueRole(iam.Role):

    def __init__(self, scope: core.Construct, data_lake_bucket: BaseDataLakeBucket, **kwargs) -> None:
        self.data_lake_bucket = data_lake_bucket
        self.deploy_env = self.data_lake_bucket.deploy_env
        self.layer = self.data_lake_bucket.layer
        super().__init__(
            scope,
            id=f'iam-{self.deploy_env.value}-glue-data-lake-{self.layer.value}-role',
            assumed_by=iam.ServicePrincipal('glue.amazonaws.com'),
            description=f'Allows using Glue on Data Lake {self.layer.value}',
        )
        self.bucket_arn = self.data_lake_bucket.bucket_arn
        self.add_policy()
        self.add_instance_profile()

    def add_policy(self):
        policy = iam.Policy(
            self,
            id=f'iam-{self.deploy_env.value}-glue-data-lake-{self.layer.value}-policy',
            policy_name=f'iam-{self.deploy_env.value}-glue-data-lake-{self.layer.value}-policy',
            statements=[
                iam.PolicyStatement(
                    actions=[
                        's3:ListBucket',
                        's3:GetObject',
                        's3:PutObject'
                    ],
                    resources=[self.bucket_arn, f'{self.bucket_arn}/*']
                ),
                iam.PolicyStatement(
                    actions=[
                        'cloudwatch:PutMetricData'
                    ],
                    resources=[
                        'arn:aws:cloudwatch:*'
                    ]
                ),
                iam.PolicyStatement(
                    actions=[
                        'glue:*'
                    ],
                    resources=[
                        'arn:aws:glue:*'
                    ]
                ),
                iam.PolicyStatement(
                    actions=[
                        'logs:CreateLogGroup',
                        'logs:CreateLogStream',
                        'logs:PutLogEvents'
                    ],
                    resources=[
                        'arn:aws:logs:*:*:/aws-glue/*'
                    ]
                ),
            ]
        )
        self.attach_inline_policy(policy)

    def add_instance_profile(self):
        iam.CfnInstanceProfile(
            self,
            id=f'iam-{self.deploy_env.value}-glue-data-lake-{self.layer.value}-instance-profile',
            instance_profile_name=f'iam-{self.deploy_env.value}-glue-data-lake-{self.layer.value}-instance-profile',
            roles=[
                self.role_name
            ]
        )
