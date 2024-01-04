import boto3

# # Retrieve the website configuration
s3 = boto3.client('s3')
# result = s3.get_bucket_website(Bucket='ali9389309330')

# Upload 'index.html' with public-read ACL
s3.upload_file('index.html', 'dkjdosdlsll', 'index.html')

# Upload 'error.html' with public-read ACL
s3.upload_file('error.html', 'dkjdosdlsll', 'error.html')


# Define the website configuration
website_configuration = {
    'ErrorDocument': {'Key': 'error.html'},
    'IndexDocument': {'Suffix': 'index.html'},
}

# Set the website configuration
s3.put_bucket_website(Bucket=' ',
                      WebsiteConfiguration=website_configuration)



# Delete the website configuration
s3 = boto3.client('s3')
s3.delete_bucket_website(Bucket=' ')