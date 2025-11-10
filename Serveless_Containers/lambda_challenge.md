# 🧠 AWS Word Count Automation — Serverless Project

[![AWS](https://img.shields.io/badge/AWS-Lambda%20%7C%20S3%20%7C%20SNS-orange?logo=amazon-aws)](https://aws.amazon.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **Automating File Processing with S3, Lambda & SNS**

A serverless automation workflow that counts words in uploaded text files and sends real-time email notifications using AWS services.

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Architecture](#-architecture)
- [Prerequisites](#-prerequisites)
- [AWS Services Used](#️-aws-services-used)
- [Setup Instructions](#-setup-instructions)
- [Lambda Function Code](#-lambda-function-code)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
- [Expected Output](#-expected-output)
- [Cost Considerations](#-cost-considerations)
- [Contributing](#-contributing)

---

## 🚀 Overview

This project demonstrates a **serverless, event-driven architecture** on AWS that:

1. **Automatically detects** when a `.txt` file is uploaded to an S3 bucket
2. **Processes the file** using a Lambda function to count words
3. **Sends an email notification** with the word count result via Amazon SNS

This is a practical example of cloud automation that can be extended for log processing, document analysis, data validation, and more.

---

## 🏗️ Architecture

```
┌─────────────┐         ┌──────────────────┐         ┌─────────────────┐
│             │         │                  │         │                 │
│    User     │  PUT    │   Amazon S3      │ Trigger │  AWS Lambda     │
│  Uploads    ├────────►│   Bucket         ├────────►│  Function       │
│  file.txt   │         │                  │         │  (Python 3.9+)  │
│             │         │                  │         │                 │
└─────────────┘         └──────────────────┘         └────────┬────────┘
                                                               │
                                                               │ Publish
                                                               ▼
                                                      ┌─────────────────┐
                                                      │                 │
                                                      │  Amazon SNS     │
                                                      │  Topic          │
                                                      │                 │
                                                      └────────┬────────┘
                                                               │
                                                               │ Email
                                                               ▼
                                                      ┌─────────────────┐
                                                      │                 │
                                                      │  User's Email   │
                                                      │  Inbox          │
                                                      │                 │
                                                      └─────────────────┘
```

**Event Flow:**
1. File uploaded to S3 bucket triggers an event
2. Lambda function is invoked automatically
3. Lambda reads file, counts words, publishes to SNS
4. SNS sends email notification to subscriber(s)

---

## 📚 Prerequisites

- **AWS Account** with appropriate permissions
- **Verified email address** for SNS notifications
- **Basic knowledge** of AWS Console, Python, and serverless concepts
- **AWS CLI** (optional, for advanced setup)

---

## ⚙️ AWS Services Used

| Service | Purpose | Cost |
|---------|---------|------|
| **Amazon S3** | Object storage for `.txt` files and event trigger source | Pay per GB stored |
| **AWS Lambda** | Serverless compute to process files and count words | Free tier: 1M requests/month |
| **Amazon SNS** | Pub/Sub messaging service for email notifications | Free tier: 1,000 emails/month |
| **Amazon CloudWatch** | Monitoring, logging, and debugging Lambda execution | Free tier: 5GB logs/month |
| **AWS IAM** | Identity and access management for Lambda permissions | Free |

---

## 🛠️ Setup Instructions

### Step 1: Create S3 Bucket

1. Navigate to **S3 Console** → Click **Create bucket**
2. **Bucket name:** `wordcount-bucket-<your-unique-id>`
3. **Region:** Choose your preferred region (e.g., `us-east-1`)
4. Keep default settings → Click **Create bucket**
5. **Important:** We'll configure the trigger after creating the Lambda function

---

### Step 2: Create SNS Topic and Subscription

1. Navigate to **SNS Console** → Click **Create topic**
2. **Type:** Standard
3. **Name:** `wordcount-topic`
4. Click **Create topic**
5. In the topic details page, click **Create subscription**
6. **Protocol:** Email
7. **Endpoint:** Enter your email address
8. Click **Create subscription**
9. **⚠️ IMPORTANT:** Check your email and click the confirmation link

---

### Step 3: Create IAM Role for Lambda

1. Navigate to **IAM Console** → **Roles** → **Create role**
2. **Trusted entity type:** AWS service
3. **Use case:** Lambda → Click **Next**
4. **Attach policies:**
   - `AWSLambdaBasicExecutionRole` (for CloudWatch Logs)
   - `AmazonS3ReadOnlyAccess` (or create custom policy for specific bucket)
   - `AmazonSNSFullAccess` (or create custom policy for specific topic)
5. **Role name:** `WordCountLambdaRole`
6. Click **Create role**

**🔐 Security Best Practice:** Replace `FullAccess` policies with least-privilege custom policies in production:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject"],
      "Resource": "arn:aws:s3:::wordcount-bucket-*/*"
    },
    {
      "Effect": "Allow",
      "Action": ["sns:Publish"],
      "Resource": "arn:aws:sns:*:*:wordcount-topic"
    }
  ]
}
```

---

### Step 4: Create Lambda Function

1. Navigate to **Lambda Console** → Click **Create function**
2. **Function name:** `WordCountLambda`
3. **Runtime:** Python 3.9 (or later)
4. **Execution role:** Use existing role → Select `WordCountLambdaRole`
5. Click **Create function**
6. Copy the code from the [Lambda Function Code](#-lambda-function-code) section below
7. **⚠️ CRITICAL:** Update the `topic_arn` variable with your actual SNS topic ARN:
   - Find it in **SNS Console** → **Topics** → Copy the ARN
8. Click **Deploy**

---

### Step 5: Configure S3 Event Trigger

1. In your Lambda function page, click **Add trigger**
2. **Source:** S3
3. **Bucket:** Select `wordcount-bucket-<your-unique-id>`
4. **Event type:** All object create events
5. **Prefix:** (leave empty to process all files)
6. **Suffix:** `.txt` (optional, to process only text files)
7. **Acknowledge** the recursive invocation warning
8. Click **Add**

---

## 💻 Lambda Function Code

```python
import boto3
import os

# Initialize AWS service clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

def lambda_handler(event, context):
    """
    Lambda function to count words in uploaded text files
    and send results via SNS email notification.
    """
    try:
        # Extract S3 event information
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        print(f"Processing file: {file_key} from bucket: {bucket_name}")
        
        # Download file to Lambda's /tmp directory
        tmp_file = f'/tmp/{os.path.basename(file_key)}'
        s3.download_file(bucket_name, file_key, tmp_file)
        
        # Read file and count words
        with open(tmp_file, 'r', encoding='utf-8') as f:
            text = f.read()
            word_count = len(text.split())
        
        # Prepare SNS notification
        message = (
            f"Word Count Analysis Complete!\n\n"
            f"File: {file_key}\n"
            f"Bucket: {bucket_name}\n"
            f"Word Count: {word_count}\n\n"
            f"Processed by AWS Lambda"
        )
        subject = f"📊 Word Count Result: {os.path.basename(file_key)}"
        
        # ⚠️ REPLACE WITH YOUR SNS TOPIC ARN
        topic_arn = "arn:aws:sns:REGION:ACCOUNT_ID:wordcount-topic"
        
        # Publish to SNS
        sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject
        )
        
        print(f"SUCCESS: Word count = {word_count}")
        
        return {
            "statusCode": 200,
            "body": f"Word count: {word_count}"
        }
    
    except Exception as e:
        error_msg = f"ERROR: {str(e)}"
        print(error_msg)
        raise e
```

**Key Points:**
- Uses `/tmp` directory (512 MB available in Lambda)
- Handles UTF-8 encoding for international characters
- Comprehensive error logging for debugging
- Returns proper HTTP status codes

---

## 🧪 Testing

### Manual Test

1. Create a test file named `sample.txt` with some content:
   ```
   This is a sample text file for testing
   the AWS serverless word count automation.
   ```

2. Upload to S3:
   - Go to your S3 bucket
   - Click **Upload** → Select `sample.txt`
   - Click **Upload**

3. **Check CloudWatch Logs:**
   - Lambda Console → **Monitor** tab → **View CloudWatch logs**
   - Look for `SUCCESS: Word count = X` message

4. **Check your email** for the notification (may take 1-2 minutes)

### Expected Email Format

```
Subject: 📊 Word Count Result: sample.txt

Body:
Word Count Analysis Complete!

File: sample.txt
Bucket: wordcount-bucket-12345
Word Count: 14

Processed by AWS Lambda
```

---

## 🔧 Troubleshooting

### Issue: Lambda not triggered

**Symptoms:** File uploaded but no email received

**Solutions:**
- ✅ Verify S3 trigger is configured (Lambda → Configuration → Triggers)
- ✅ Check file extension matches trigger suffix (e.g., `.txt`)
- ✅ Review CloudWatch Logs for invocation records

---

### Issue: Permission denied errors

**Symptoms:** Lambda logs show `AccessDenied` errors

**Solutions:**
- ✅ Verify IAM role has S3 read permissions
- ✅ Verify IAM role has SNS publish permissions
- ✅ Check S3 bucket policy doesn't block Lambda
- ✅ Ensure Lambda execution role is attached to function

---

### Issue: No email received

**Symptoms:** Lambda executes successfully but no email arrives

**Solutions:**
- ✅ Confirm SNS subscription status is "Confirmed" (not Pending)
- ✅ Check spam/junk folder
- ✅ Verify `topic_arn` in code matches actual SNS topic ARN
- ✅ Check SNS delivery logs in CloudWatch

---

### Issue: Unicode/encoding errors

**Symptoms:** Lambda fails when processing certain text files

**Solutions:**
- ✅ Add `encoding='utf-8'` parameter to `open()` function
- ✅ Handle binary files with