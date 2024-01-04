import boto3

s3 = boto3.client('s3')
# Order is Important
# 1. Bucket Name 2. File you want to download 3. Name u want to give to the downloaded file
s3.download_file('', 'apnafile2', 'myfile')