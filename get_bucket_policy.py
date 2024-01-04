import boto3
s3 = boto3.client('s3')

try :  
    rslt = s3.get_bucket_policy(Bucket='')
except Exception as e:
    print("Error Encounter")
    
print(rslt['Policy'])