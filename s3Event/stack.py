from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_lambda,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_s3 as s3,
    aws_s3_notifications as s3n,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
)
import os

class LambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        __dirname = os.getcwd()
        print(__dirname)
        s3Bucket = s3.Bucket(self, "s3-bucket")
        s3Lambda = aws_lambda.Function(self, "S3Lambda",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="s3Lambda.handler",
            code=aws_lambda.Code.from_asset(__dirname+"\python_cdk_project")
        )
        s3Lambda.add_environment("S3_BUCKET", s3Bucket.bucket_name)
        cloudWatchLambda = aws_lambda.Function(self, "cloudWatchLambda",
            runtime=aws_lambda.Runtime.PYTHON_3_9,
            handler="cloudWatchLambda.handler",
            code=aws_lambda.Code.from_asset(__dirname+"\python_cdk_project")
        )
        s3Bucket.add_event_notification(s3.EventType.OBJECT_CREATED, s3n.LambdaDestination(cloudWatchLambda))
        s3Bucket.grant_read(cloudWatchLambda.role)
        s3Bucket.grant_read_write(s3Lambda.role)
