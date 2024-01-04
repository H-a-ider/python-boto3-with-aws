import boto3


# Create IAM client
iam = boto3.client('iam')

# Get a policy
response = iam.get_policy(
    PolicyArn=''
)
print(response['Policy'])