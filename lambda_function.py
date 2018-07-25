import json
import preSignedUrl

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    if 'queryStringParameters' in event: # call is from API Gateway
        bucket = event['queryStringParameters']['bucket']
        objectKey = event['queryStringParameters']['object_key']
        expire = int(event['queryStringParameters']['expire'])
    else: # call is from AWS console
        bucket = event['bucket']
        objectKey = event['object_key']
        expire = int(event['expire'])
    psUrl = preSignedUrl.getPreSignedUrl(bucket, objectKey, expire);

    print("psURL = " + psUrl + " !")

    return {"statusCode": 200, \
        "headers": {"Content-Type": "application/json"}, \
        "body": psUrl }
