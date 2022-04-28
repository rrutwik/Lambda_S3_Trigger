import boto3
s3_client = boto3.client("s3")
def handler(event, context):
    input = event["Records"][0]
    s3BucketName = input["s3"]["bucket"]["name"]
    key = input["s3"]["object"]["key"]
    content = s3_client.get_object(Bucket=s3BucketName, Key=key)["Body"].read().decode("utf-8") 
    print(content)
    return {
        "content": content
    }