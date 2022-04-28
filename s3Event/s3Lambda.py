import boto3
import os
s3_client = boto3.client("s3")
def handler(event, context):
    fileName = event["fileName"]
    fileContent = event["fileContent"]
    encodedFileContent = fileContent.encode("utf-8")
    S3_BUCKET = os.environ.get("S3_BUCKET")
    output = s3_client.put_object(Bucket=S3_BUCKET, Key=fileName, Body=encodedFileContent)
    return output