import boto3
from botocore.exceptions import NoCredentialsError
from datetime import datetime

def lambda_handler(event, context):
    # Initialize clients for SES and DynamoDB
    ses_client = boto3.client('ses', region_name='us-east-1')  # Change region if necessary
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('EmailLogs')  # Replace with your DynamoDB table name

    # S3 bucket and object details
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Email details
    sender_email = "tatendamoyo539@gmail.com"  # Replace with your verified SES email
    recipient_email = "moyot7663@gmail.com"  # Replace with recipient email
    subject = "New File Uploaded to S3"
    body = f"A new file has been uploaded to your S3 bucket.\n\nBucket: {bucket_name}\nFile: {object_key}"
    
    try:
        # Send email using SES
        response = ses_client.send_email(
            Source=sender_email,
            Destination={
                'ToAddresses': [recipient_email]
            },
            Message={
                'Subject': {
                    'Data': subject
                },
                'Body': {
                    'Text': {
                        'Data': body
                    }
                }
            }
        )
        
        # Log the email details into DynamoDB
        message_id = response['MessageId']
        timestamp = datetime.utcnow().isoformat()
        
        table.put_item(
            Item={
                'MessageId': message_id,  # Partition key
                'Sender': sender_email,
                'Recipient': recipient_email,
                'Subject': subject,
                'Timestamp': timestamp,
                'Status': 'Sent',
                'S3Bucket': bucket_name,
                'S3ObjectKey': object_key
            }
        )
        
        print("Email sent and logged to DynamoDB! Message ID:", message_id)
        return {
            'statusCode': 200,
            'body': 'Email sent and logged successfully'
        }
    
    except NoCredentialsError:
        print("Credentials not available")
        return {
            'statusCode': 500,
            'body': 'Error sending email'
        }
    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': 'Error sending email or logging to DynamoDB'
        }