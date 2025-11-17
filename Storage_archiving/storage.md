# AWS Storage Management Lab

A hands-on lab for learning AWS storage management using EBS snapshots, S3 sync, and automated backup strategies.

## 📋 Overview

This lab demonstrates practical AWS storage management techniques including:
- Creating and managing EBS volume snapshots
- Automating snapshot creation with cron jobs
- Synchronizing files between EC2 instances and S3 buckets
- Implementing S3 versioning for data recovery

## 🏗️ Architecture

![Lab Dashboard Screenshot](/screenshots/storage.png)

## ⏱️ Duration

Approximately 45 minutes

## 🎯 Learning Objectives

By completing this lab, you will:
- Create and maintain snapshots for Amazon EC2 instances
- Use Amazon S3 sync to copy files from EBS volumes to S3 buckets
- Implement Amazon S3 versioning to retrieve deleted files
- Automate backup processes using Python and cron

## 📚 Prerequisites

- AWS Account with appropriate permissions
- Basic familiarity with:
  - AWS CLI
  - Linux command line
  - Python basics
  - EC2 and S3 concepts

## 🚀 Lab Tasks

### Task 1: Resource Setup
- Create an S3 bucket for file synchronization
- Attach IAM role to EC2 instance for AWS service access

### Task 2: EBS Snapshot Management

#### 2.1 Initial Snapshot
- Identify EBS volume attached to Processor instance
- Stop instance safely
- Create initial volume snapshot
- Restart instance

#### 2.2 Automated Snapshots
- Configure cron job for recurring snapshots
- Schedule snapshot creation every minute for testing

#### 2.3 Snapshot Retention
- Implement Python script to maintain only last 2 snapshots
- Automatically delete older snapshots

### Task 3: S3 File Synchronization (Challenge)
- Enable S3 bucket versioning
- Sync local directory to S3 bucket
- Delete files with sync --delete option
- Recover deleted files using versioning

## 🛠️ Key Commands

### EBS Snapshot Commands
```bash
# Get volume ID
aws ec2 describe-instances --filter 'Name=tag:Name,Values=Processor' \
  --query 'Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.{VolumeId:VolumeId}'

# Create snapshot
aws ec2 create-snapshot --volume-id VOLUME-ID

# Check snapshot status
aws ec2 wait snapshot-completed --snapshot-id SNAPSHOT-ID

# List snapshots
aws ec2 describe-snapshots --filters "Name=volume-id,Values=VOLUME-ID"
```

### S3 Sync Commands
```bash
# Enable versioning
aws s3api put-bucket-versioning --bucket BUCKET-NAME \
  --versioning-configuration Status=Enabled

# Sync directory to S3
aws s3 sync files s3://BUCKET-NAME/files/

# Sync with delete
aws s3 sync files s3://BUCKET-NAME/files/ --delete

# List object versions
aws s3api list-object-versions --bucket BUCKET-NAME --prefix files/file1.txt

# Restore specific version
aws s3api get-object --bucket BUCKET-NAME --key files/file1.txt \
  --version-id VERSION-ID files/file1.txt
```

### Cron Job Setup
```bash
# Create cron job for snapshots
echo "* * * * *  aws ec2 create-snapshot --volume-id VOLUME-ID 2>&1 >> /tmp/cronlog" > cronjob
crontab cronjob

# Remove cron job
crontab -r
```

## 📝 Python Script

The lab includes `snapshotter_v2.py` which:
- Discovers all EBS volumes in your account
- Takes snapshots of each volume
- Sorts snapshots by creation date
- Retains only the 2 most recent snapshots
- Deletes older snapshots automatically

## 🔒 Security Notes

- IAM role `S3BucketAccess` provides necessary permissions
- Instance profile attached to Processor EC2 instance
- No hardcoded credentials required
- Uses AWS CLI with instance role authentication

## 📦 Sample Files

Download sample files for S3 sync testing:
```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-3-124627/183-lab-JAWS-managing-storage/s3/files.zip
unzip files.zip
```

Contains:
- file1.txt
- file2.txt
- file3.txt

## ✅ Success Criteria

- [ ] Successfully created initial EBS snapshot
- [ ] Automated snapshot creation running via cron
- [ ] Snapshot retention script maintains only 2 snapshots
- [ ] S3 bucket versioning enabled
- [ ] Files synchronized from local directory to S3
- [ ] Successfully recovered deleted file using versioning

## 🧹 Cleanup

Remember to clean up resources after completing the lab:
- Stop/terminate EC2 instances
- Delete EBS snapshots
- Empty and delete S3 bucket
- Remove IAM roles (if created manually)

## 📖 Additional Resources

- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/)
- [EBS Snapshots Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
- [S3 Sync Documentation](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
- [S3 Versioning Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

## 🤝 Contributing

Feel free to submit issues or pull requests to improve this lab guide.

## 📄 License

This lab is provided for educational purposes.

---

**Note**: Replace placeholder values (VOLUME-ID, BUCKET-NAME, INSTANCE-ID, etc.) with actual values from your AWS environment.