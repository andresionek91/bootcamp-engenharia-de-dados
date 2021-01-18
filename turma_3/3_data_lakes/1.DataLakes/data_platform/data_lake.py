from aws_cdk import core
from aws_cdk import (
    aws_s3 as s3,
)

from data_platform import Environment
from data_lake_base import BaseDataLakeBucket, DataLakeLayer, BaseDataLakeGlueDatabase, BaseDataLakeGlueRole


class DataLakeStack(core.Stack):
    def __init__(self, scope: core.Construct, deploy_env: Environment, **kwargs) -> None:
        self.deploy_env = deploy_env
        super().__init__(scope, id=f'{self.deploy_env.value}-data-lake', **kwargs)

        # Data Lake Raw
        self.data_lake_raw_bucket = BaseDataLakeBucket(
            self,
            deploy_env=self.deploy_env,
            layer=DataLakeLayer.RAW
        )

        self.data_lake_raw_bucket.add_lifecycle_rule(
            transitions=[
                s3.Transition(
                    storage_class=s3.StorageClass.INTELLIGENT_TIERING,
                    transition_after=core.Duration.days(90)
                ),
                s3.Transition(
                    storage_class=s3.StorageClass.GLACIER,
                    transition_after=core.Duration.days(360)
                )
            ],
            enabled=True
        )

        self.data_lake_raw_database = BaseDataLakeGlueDatabase(
            self,
            data_lake_bucket=self.data_lake_raw_bucket
        )

        self.data_lake_raw_glue_role = BaseDataLakeGlueRole(
            self,
            data_lake_bucket=self.data_lake_raw_bucket
        )

        # Data Lake Processed
        self.data_lake_processed_bucket = BaseDataLakeBucket(
            self,
            deploy_env=self.deploy_env,
            layer=DataLakeLayer.PROCESSED
        )

        self.data_lake_processed_database = BaseDataLakeGlueDatabase(
            self,
            data_lake_bucket=self.data_lake_processed_bucket
        )

        self.data_lake_processed_glue_role = BaseDataLakeGlueRole(
            self,
            data_lake_bucket=self.data_lake_processed_bucket
        )

        # Data Lake Curated
        self.data_lake_curated_bucket = BaseDataLakeBucket(
            self,
            deploy_env=self.deploy_env,
            layer=DataLakeLayer.CURATED
        )

        self.data_lake_curated_database = BaseDataLakeGlueDatabase(
            self,
            data_lake_bucket=self.data_lake_curated_bucket
        )

        self.data_lake_curated_glue_role = BaseDataLakeGlueRole(
            self,
            data_lake_bucket=self.data_lake_curated_bucket
        )

