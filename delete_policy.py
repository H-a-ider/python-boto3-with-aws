import boto3

# Create IAM client
iam = boto3.client('iam')

# Detach a role policy
iam.detach_role_policy(
    PolicyArn='',
    RoleName='AmazonDynamoDBFullAccess'
)