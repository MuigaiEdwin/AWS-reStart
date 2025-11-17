# Working with Amazon S3 - File Sharing Lab

## Overview

This lab demonstrates how to create and configure an Amazon S3 bucket for secure file sharing with external users. The solution includes automated email notifications when bucket contents are modified, using Amazon SNS for event notifications.

## Architecture

The lab implements a secure file-sharing workflow:

1. **External User Access**: An IAM user (`mediacouser`) representing an external media company uploads, modifies, or deletes images
2. **Multiple Access Methods**: Users can interact via AWS Management Console or AWS CLI
3. **Event Notifications**: S3 detects changes and publishes notifications to an SNS topic
4. **Email Alerts**: Administrators receive detailed email notifications about bucket modifications

## Learning Objectives

By completing this lab, you will learn to:

- Create and configure S3 buckets using AWS CLI (`s3api` and `s3` commands)
- Implement secure IAM policies for granular bucket access control
- Verify and test user permissions on S3 buckets
- Configure S3 event notifications with SNS integration
- Set up email subscriptions for bucket change notifications

## Prerequisites

- AWS Account with appropriate permissions
- Basic understanding of AWS S3, IAM, and SNS
- Familiarity with AWS CLI
- Email address for receiving notifications

## Lab Duration

**Approximately 90 minutes**

## Key Components

### IAM Configuration
- **User Group**: `mediaco` - Manages permissions for external users
- **IAM User**: `mediacouser` - External user with specific S3 permissions
- **Policies**: Custom policies restricting access to specific bucket prefixes

### S3 Bucket Structure
```
cafe-xxxnnn/
└── images/
    ├── Donuts.jpg
    ├── Cup-of-Hot-Chocolate.jpg
    ├── Caramel-Delight.jpg
    └── [other image files]
```

### SNS Topic
- **Name**: `s3NotificationTopic`
- **Purpose**: Receives S3 event notifications and distributes to subscribers
- **Events Monitored**: Object creation and deletion in `images/` prefix

## Tasks Overview

### Task 1: Connect to CLI Host
- Connect to EC2 instance using EC2 Instance Connect
- Configure AWS CLI with credentials

### Task 2: Create and Initialize S3 Bucket
```bash
# Create bucket
aws s3 mb s3://cafe-xxxnnn --region 'us-west-2'

# Upload initial images
aws s3 sync ~/initial-images/ s3://cafe-xxxnnn/images

# Verify upload
aws s3 ls s3://cafe-xxxnnn/images/ --human-readable --summarize
```

### Task 3: Review IAM Permissions
- Examine `mediaco` IAM group policies
- Review `mediacouser` permissions and inheritance
- Test user permissions through AWS Console

### Task 4: Configure Event Notifications
- Create SNS topic (`s3NotificationTopic`)
- Configure topic access policy for S3
- Subscribe to topic via email
- Attach event notification configuration to S3 bucket

### Task 5: Test Event Notifications
- Upload objects and verify notifications
- Delete objects and verify notifications
- Test unauthorized operations (should fail)

## Security Features

### Principle of Least Privilege
- Users can only perform specific actions (`GetObject`, `PutObject`, `DeleteObject`)
- Access limited to `images/*` prefix only
- No permission to modify bucket settings

### Access Policy Example
```json
{
  "Sid": "AllowUserSpecificActionsOnlyInTheSpecificPrefix",
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject",
    "s3:DeleteObject"
  ],
  "Resource": "arn:aws:s3:::cafe-*/images/*"
}
```

## Event Notification Configuration

The S3 bucket monitors the following events:
- `s3:ObjectCreated:*` - Any object creation event
- `s3:ObjectRemoved:*` - Any object deletion event

Notifications are filtered to the `images/` prefix only.

## Testing Scenarios

### Authorized Operations ✅
- View images in the bucket
- Upload new images
- Delete existing images
- Download images

### Unauthorized Operations ❌
- Modify bucket permissions
- Upload files to bucket root
- Change object ACLs
- Delete the bucket

## Common Commands

```bash
# Configure AWS CLI
aws configure

# Upload object
aws s3api put-object --bucket cafe-xxxnnn --key images/file.jpg --body ~/path/to/file.jpg

# Get object
aws s3api get-object --bucket cafe-xxxnnn --key images/file.jpg output.jpg

# Delete object
aws s3api delete-object --bucket cafe-xxxnnn --key images/file.jpg

# List bucket contents
aws s3 ls s3://cafe-xxxnnn/images/ --human-readable
```

## Email Notifications

You will receive email notifications for:
- **Test Event**: Initial configuration test from AWS
- **ObjectCreated Events**: When files are uploaded
- **ObjectRemoved Events**: When files are deleted

Each notification includes:
- Event type
- Timestamp
- Bucket name
- Object key
- Request ID

## Troubleshooting

### Bucket Creation Fails
- Ensure bucket name is globally unique
- Verify bucket name contains no uppercase letters
- Check that bucket name starts with `cafe-`

### No Email Notifications
- Verify email subscription is confirmed
- Check SNS topic policy allows S3 to publish
- Ensure event configuration is correctly attached to bucket

### Access Denied Errors
- Verify IAM user credentials are correct
- Check that user is member of `mediaco` group
- Ensure operations are performed on `images/*` prefix

## Best Practices

1. **Bucket Naming**: Use descriptive, unique names with prefixes
2. **IAM Policies**: Apply least privilege principle
3. **Event Filtering**: Use prefixes to limit notification scope
4. **Email Subscriptions**: Use distribution lists for team notifications
5. **Testing**: Always test both authorized and unauthorized access

## Cleanup

After completing the lab:
1. Delete objects from the S3 bucket
2. Delete the S3 bucket
3. Unsubscribe from SNS topic
4. Delete SNS topic
5. Remove IAM user access keys

## Additional Resources

- [Amazon S3 Documentation](https://docs.aws.amazon.com/s3/)
- [AWS CLI S3 Commands](https://docs.aws.amazon.com/cli/latest/reference/s3/)
- [Amazon SNS Documentation](https://docs.aws.amazon.com/sns/)
- [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

## Notes

- Replace `<cafe-xxxnnn>` with your actual bucket name in all commands
- Store credentials securely and never commit them to version control
- This is a lab environment - production implementations should include additional security measures
- External users in real-world scenarios typically wouldn't have direct CLI Host access

## License

This lab is part of AWS training materials.

---

**Lab Status**: Ready for deployment
**Last Updated**: November 2025
**AWS Region**: us-west-2