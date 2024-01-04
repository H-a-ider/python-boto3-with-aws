import boto3

s3 = boto3.client('ec2')
response = s3.describe_instances()
print(response)