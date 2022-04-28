#!/usr/bin/env python3

import aws_cdk as cdk

from s3Event.stack import LambdaStack


app = cdk.App()
LambdaStack(app, "S3-Lambda-Event")
#ralmal2022
app.synth()
