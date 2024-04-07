import json
import boto3
import qrcode
import io
import base64

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Parse the URL from the event
    body = json.loads(event['body'])
    url = body['url']
    
    # Generate QR code
    img = qrcode.make(url)
    img_bytes = io.BytesIO()
    img.save(img_bytes)
    img_bytes = img_bytes.getvalue()
    
    # Generate a unique filename
    filename = url.split("://")[1].replace("/", "_") + '.png'
    
    # Upload the QR code to the S3 bucket
    s3.put_object(Bucket='qr-code-generator732', Key=filename, Body=img_bytes, ContentType='image/png', ACL='public-read')
    
    # Generate the URL of the uploaded QR code
    location = s3.get_bucket_location(Bucket='qr-code-generator732')['LocationConstraint']
    region = '' if location is None else f'{location}'
    qr_code_url = f"https://{'qr-code-generator732'}.s3.amazonaws.com/{filename}"
    
    # Construct response with CORS headers
    response = {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        'body': json.dumps(qr_code_url)
    }
    
    return response
