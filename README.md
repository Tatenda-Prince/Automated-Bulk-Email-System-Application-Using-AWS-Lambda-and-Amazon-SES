# Automated Bulk Email System with AWS Lambda and Amazon SES

"Sending Bulk Emails"

# Technical Architecture

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/ffe25d83eb1b43d6611bfeab4288b90695ba3a8b/img/Screenshot%202025-02-02%20103313.png)


## Project Overview

This project automates bulk email notifications using AWS serverless services, ensuring scalability, cost-effectiveness, and efficiency. Users upload files (e.g., CSVs with email addresses and messages) to an Amazon S3 bucket, which triggers an AWS Lambda function. The function processes the file, extracts relevant data, and sends emails via Amazon Simple Email Service (SES). Simultaneously, it logs email events in Amazon DynamoDB for tracking and auditing. The emails are then delivered to recipients via Gmail or other email providers. This system is ideal for automated customer notifications, marketing campaigns, user verification, and event invitations, offering a secure, reliable, and fully managed solution.

## Project Objectives

1.Automate Bulk Email Processing – Enable seamless, automated email dispatch based on user-uploaded files without manual intervention.

2.Leverage Serverless Architecture – Utilize AWS services like S3, Lambda, SES, and DynamoDB to build a cost-efficient, scalable, and maintenance-free solution.

3.Ensure Reliable Email Delivery – Use Amazon SES for high deliverability and avoid spam filters, ensuring emails reach the intended recipients.

4.Implement Event Logging & Tracking – Store email event logs in Amazon DynamoDB for monitoring, troubleshooting, and reporting purposes.

## Prerequisites

1.AWS Account: Create an AWS Account

2.AWS CLI Installed and Configured: Install & configure AWS CLI to programatically interact with AWS

## Technologies

1.Amazon S3

2.AWS Lambda

3.Amazon SES 

4.Amazon DynamoDB

5.Amazon CloudWatch 


## Step 1: Configure Amazon S3 Bucket

1.1.Login to AWS Console:

Access the AWS Management Console and search for Amazon S3.

1.2.Create a bucket and give it name that is globally unique

Choose create bucket and leave everything as default


![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/79d260892808acaa4c5e34a48af62ff6488bd3f9/img/Screenshot%202025-02-02%20104928.png)


1.3.Now that our bucket is successfully created see example, leave the bucket empty becuase lambda will trigger an event when we upload a file.

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/6b16c34c57d53057b6d3f3ff3cae17337c4180db/img/Screenshot%202025-02-02%20104947.png)


## Step 2: Configure DynamoDB table


2.1.Lets Navigate to DynamoDB:

Go to the DynamoDB service in the AWS Management Console.

Click "Create table"

2.2.Configure the Table

We will give our table a name  `EmailLogs`

Partition key: `MessageId` Type "String"

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/cd4bd85c1dc7fe348f414872ab8c3a97b369a30c/img/Screenshot%202025-02-02%20110447.png)


Click Create Table 




2.3.As you can our table active now see example below-

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/1f04849ec5ebcec56ace78b9fdc39e2cee118a3f/img/Screenshot%202025-02-02%20110526.png)


## Step 3: Configure IAM Role for AWS Lambda

3.1.We Navigate to IAM:

Go to the IAM service.

Click on "Roles" in the left-hand menu.

Click "Create role".

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/ce8f387e5dd4435d8af2cb430b320b4cfc169328/img/Screenshot%202025-02-02%20105048.png)


3.2.Select AWS Lambda as the service that will use this role.

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/09c272dafc7aff5a5e1cbd3f9b75111df43ceecb/img/Screenshot%202025-02-02%20105111.png)


3.3.Attach Policies:

Attach the following policies:

`AmazonS3FullAccess`

`AmazonSESFullAccess`

`AWSLambdaBasicExecutionRole`

`AmazonDynamoDBFullAccess`

3.4.Review and Create:

Provide a name for the role (e.g., LambdaSESS3Role).

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/9477735d55a0698339bbae0f02ddb4d97d196b62/img/Screenshot%202025-02-02%20105213.png)


Click "Create role".


## Step 4: Configure a AWS Lambda function

4.1.Navigate to Lambda:

Go to the Lambda service.

Click "Create function".

4.2.Configure Function:

Choose "Author from scratch".

Provide a name for your function (e.g., S3ToSESLambda).

Choose the runtime (e.g., Python 3.8).

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/2c7a0491cd73f0c7f1442fc295b2010110bf9150/img/Screenshot%202025-02-02%20105331.png)


Under "Permissions", choose the IAM role you created earlier (LambdaSESS3Role).

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/59c1864a31c0ddcc3f045f19f07642fd00341b4d/img/Screenshot%202025-02-02%20105350.png)


Click "Create function".


4.3.Add Trigger from S3 Bucket

Now head back to your S3 Bucket you created ealier click the "Properties" properties tab

Scroll down till you the "Event Notification" then click create event 

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/ae3278ae5eb5d91ad51625a83532274583419180/img/Screenshot%202025-02-02%20110730.png)

create a event name leave everything as default settings

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/795ded741ac3145416f1289b086efed2da3ed3e9/img/Screenshot%202025-02-02%20110813.png)


On destination choose lambda and select our lambda we created earlier

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/587bb2c53a915ef69753140f3ec8e1088d424308/img/Screenshot%202025-02-02%20110831.png)

click  Save 

## Step 5: Write a AWS Lambda function

4.1.Edit the Lambda Function:

Scroll down to the "Function code" section.

Replace the default code with the following Python code:

```python
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

```

4.2.Deploy the Function:

Click "Deploy" to save and deploy your Lambda function.



## Step 5: Verify Email Addresses in SES

5.1.Navigate to SES

Go to the SES service.

Click on "Email Addresses" in the left-hand menu.

Click "Verify a New Email Address".

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/5f8f890ffd60eb92523d1d8e0c01b5c79584ac0f/img/Screenshot%202025-02-02%20105653.png)


Enter the email addresses you used in the Lambda function (both sender and recipient).

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/31040b5b1733a9daefc0028fcc7f68098f2fc030/img/Screenshot%202025-02-02%20105740.png)


Click "Verify This Email Address".

Check your email inbox and click the verification link sent by AWS.


![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/957d640379b74762f62dca2d1c69d3c88052f121/img/Screenshot%202025-02-02%20105821.png)


## Step 6: Test the Setup

6.1.Upload a File to S3:

Go to the S3 bucket you created.

Upload a file to the bucket.

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/73a54b908314307964e17bf838ae336caa84d02c/img/Screenshot%202025-02-02%20111049.png)


6.2.Check Email

The recipient email has received an email notification about the new file upload.

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/306266322c09e4b8a78d77950e337260e823e2fc/img/Screenshot%202025-02-02%20111142.png)


## Step 7:Verify DynamoDB Logs

7.1.Navigate to DynamoDB:

Go to the DynamoDB service.

Click on the `EmailLogs` table.

Click "Explore table items".

You should see a new entry with the email details, including the `MessageId`, `Sender`, `Recipient`, `Subject`, `Timestamp`, and S3 details.

![image_alt](https://github.com/Tatenda-Prince/Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES/blob/87cced51d4142c72783ecb29e859c9120f0923e2/img/Screenshot%202025-02-02%20112103.png)


# Congratulations 

We have successfully set up an AWS project using AWS Lambda,Dynamodb, Amazon SES, and Amazon S3. This setup automatically sends an email notification whenever a new file is uploaded to the S3 bucket.























