import boto3

def lambda_handler(event, context):
    # Initialize S3 client
    s3 = boto3.client('s3')
    
    # Specify your bucket and file details
    bucket_name = "your-bucket-name"
    file_key = "your-folder/your-file.txt"  # path inside bucket
    
    try:
        # Read the existing file content
        response = s3.get_object(Bucket=bucket_name, Key=file_key)
        content = response['Body'].read().decode('utf-8')
        
        # Add new text
        new_text = "\nThis is the new text added from Lambda!"
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