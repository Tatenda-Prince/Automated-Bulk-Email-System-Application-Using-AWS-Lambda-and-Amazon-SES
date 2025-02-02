# Automated-Bulk-Email-System-Application-Using-AWS-Lambda-and-Amazon-SES

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

![image_alt]()








