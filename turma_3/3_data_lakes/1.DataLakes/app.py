#!/usr/bin/env python3
from aws_cdk import core

from data_lake import DataLakeStack
from data_platform import active_environment


app = core.App()
data_lake = DataLakeStack(app, deploy_env=active_environment)
app.synth()
