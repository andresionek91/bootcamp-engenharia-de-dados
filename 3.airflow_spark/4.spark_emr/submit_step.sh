aws s3 cp convert_to_parket.py s3://s3-dev-belisco-emr/jobs/convert_to_parket.py --profile andre_aws;
aws emr add-steps  --profile andre_aws --cluster-id j-34AO448V1AAJN --steps Type=Spark,Name="ParquetConversion",ActionOnFailure=CONTINUE,Args=[--deploy-mode,cluster,--master,yarn-cluster,--conf,spark.yarn.submit.waitAppCompletion=true,s3a://s3-dev-belisco-emr/jobs/convert_to_parket.py];
