import boto3

s3_client = boto3.client('s3')

def getPreSignedUrl(bucket, objectKey, expire):
    return s3_client.generate_presigned_url('get_object', Params = {"Bucket": bucket, "Key": objectKey}, ExpiresIn = expire, HttpMethod='GET')
