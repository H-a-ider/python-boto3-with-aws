import boto3

ec2 = boto3.client('ec2')

try:
    response = ec2.release_address(AllocationId='')
    print('Address released')
except Exception as e:
    print(e)