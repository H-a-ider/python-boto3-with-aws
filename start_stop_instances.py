import sys
import boto3

instance_id = sys.argv[2]
action = sys.argv[1].upper()

ec2 = boto3.client('ec2')

if action == 'ON':
    res = ec2.start_instances(InstanceIds=[instance_id])
else:
    res = ec2.stop_instances(InstanceIds=[instance_id])

print(res)