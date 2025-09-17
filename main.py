import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Specify your bucket and file details
    bucket_name = "prakhar-02071998-bucket"
    file_key = "prakhar_test.txt"  # path inside bucket
    
    try:
        # Read the existing file content
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        
        # Current date and time
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        # Add new text
        new_text = f"\nDate: {date_str} and Time: {time_str} and Hello World"
        updated_content = content + new_text
        
        # Write the updated content back to S3
        s3.put_object(Bucket=bucket_name, Key=file_key, Body=updated_content.encode('utf-8'))
        
        return {
            'statusCode': 200,
            'body': f"Successfully updated {file_key} in {bucket_name}"
        }
        
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
