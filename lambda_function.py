import boto3

client = boto3.client('rekognition')

def lambda_handler(event, context):
    bucket = "csc-project32205(your s3 bucket name)"
    file_name = "name of the image"

    response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': file_name}}, Attributes=['ALL'])

    for face in response['FaceDetails']:
        print(json.dumps(face, indent=2))