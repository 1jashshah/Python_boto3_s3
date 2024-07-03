import boto3

source_bucket_name = 'jash-bucket1'
destination_bucket_name = 'test-bucket-harsh-12310'
object_key = 'punjab (5).jpeg'
destination_object_key = 'punjab (5).jpeg'

# Initialize the source S3 
source_s3 = boto3.client(
    's3',
    aws_access_key_id='AKXXXXXXXXXXX',#jash
    aws_secret_access_key='tXXXXXXXXXXXXXX',
    region_name='ap-south-1'
)

# Initialize destination S3 
destination_s3 = boto3.client(
    's3',
    aws_access_key_id='AKXXXXXXXXXXXXG',
    aws_secret_access_key='nXXXXXXXXXXXXXXX',
    region_name='ap-south-1'
)

copy_source = {
    'Bucket': 'jash-bucket1',
    'Key': 'punjab (5).jpeg'
}

destination_s3.copy_object(
    CopySource=copy_source,
    Bucket='test-bucket-harsh-12310',
    Key='punjab (5).jpeg'
)

print("Migration successfull  :)")
