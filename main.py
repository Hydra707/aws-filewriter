import boto3
from datetime import datetime

def writefile(event, context):
    s3 = boto3.client('s3')

    bucket_name = "prakhar-02071998-bucket"
    file_key = "prakhar_test.txt"

    try:
        # Read existing file
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')

        # Add timestamped line
        now = datetime.now()
        new_line = f"\nDate: {now.strftime('%Y-%m-%d')} Time: {now.strftime('%H:%M:%S')} Hello World"
        updated_content = content + new_line

        # Write back
        s3.put_object(Bucket=bucket_name, Key=file_key, Body=updated_content.encode('utf-8'))

        return {
            'statusCode': 200,
            'body': f"Updated {file_key} in {bucket_name}"
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
