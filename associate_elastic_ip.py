import boto3

ec2 = boto3.client('ec2')


# This creates a new Elastic ip and associates it to the given instance
try:
    allocation = ec2.allocate_address(Domain='vpc')
    response = ec2.associate_address(AllocationId=allocation['AllocationId'],
                                     InstanceId='')
    print(response)
except Exception as e:
    print(e)