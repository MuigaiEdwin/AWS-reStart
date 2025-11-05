# AWS CLI Installation and Configuration Lab

[![AWS](https://img.shields.io/badge/AWS-IAM-orange.svg)](https://aws.amazon.com/)
[![CLI](https://img.shields.io/badge/AWS-CLI-blue.svg)](https://aws.amazon.com/cli/)
[![Linux](https://img.shields.io/badge/OS-Red%20Hat%20Linux-red.svg)](https://www.redhat.com/)

## 📋 Table of Contents
- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Lab Architecture](#lab-architecture)
- [Prerequisites](#prerequisites)
- [Lab Tasks](#lab-tasks)
- [Challenge Activity](#challenge-activity)
- [Key Commands](#key-commands)
- [Lab Solution](#lab-solution)
- [Key Takeaways](#key-takeaways)
- [Resources](#resources)

## 🎯 Overview

This hands-on lab demonstrates how to install and configure the AWS Command Line Interface (AWS CLI) on a Red Hat Linux EC2 instance. You'll learn to authenticate with AWS using access keys and interact with AWS Identity and Access Management (IAM) services through the command line.

**Duration:** ~45 minutes

## 🎓 Learning Objectives

After completing this lab, you will be able to:
- ✅ Install and configure the AWS CLI on a Red Hat Linux instance
- ✅ Connect the AWS CLI to an AWS account using access keys
- ✅ Access and manage IAM resources using the AWS CLI
- ✅ Retrieve and export IAM policy documents programmatically

## 🏗️ Lab Architecture

```
┌─────────────────────────────────────────┐
│           AWS Cloud                      │
│  ┌───────────────────────────────────┐  │
│  │            VPC                     │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │   Red Hat EC2 Instance      │  │  │
│  │  │   ┌─────────────────────┐   │  │  │
│  │  │   │     AWS CLI         │   │  │  │
│  │  │   │   (Configured)      │   │  │  │
│  │  │   └─────────────────────┘   │  │  │
│  │  │           ↕                  │  │  │
│  │  │         IAM                  │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
           ↑
      SSH Connection
           ↑
      Your Machine
```

## 📦 Prerequisites

- Access to AWS Lab environment
- SSH client:
  - **Windows:** PuTTY
  - **macOS/Linux:** Terminal (built-in)
- Basic command line knowledge
- AWS account credentials (provided in lab)

## 🚀 Lab Tasks

### Task 1: Connect to EC2 Instance via SSH

#### Windows Users
1. Download the `labsuser.ppk` file from lab Details
2. Note the PublicIP address
3. Use PuTTY to connect to the instance

#### macOS/Linux Users
```bash
# Download labsuser.pem from lab Details
cd ~/Downloads

# Set correct permissions
chmod 400 labsuser.pem

# Connect via SSH (replace <ip-address> with actual IP)
ssh -i labsuser.pem ec2-user@<ip-address>
```

### Task 2: Install AWS CLI

```bash
# Download AWS CLI installer
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# Unzip the installer
unzip -u awscliv2.zip

# Install AWS CLI
sudo ./aws/install

# Verify installation
aws --version

# View help documentation
aws help
```

**Expected Output:**
```
aws-cli/2.x.x Python/3.x.x Linux/x.x.x botocore/2.x.x
```

### Task 3: Observe IAM in AWS Console

1. Navigate to IAM service in AWS Console
2. Select **Users** → **awsstudent**
3. View **Permissions** tab → Expand **lab_policy** → Click **{} JSON**
4. Switch to **Security credentials** tab
5. Locate the Access Key ID

### Task 4: Configure AWS CLI

```bash
aws configure
```

Enter the following when prompted:
- **AWS Access Key ID:** [From lab Details]
- **AWS Secret Access Key:** [From lab Details]
- **Default region name:** `us-west-2`
- **Default output format:** `json`

### Task 5: Test IAM Access

```bash
# List IAM users
aws iam list-users
```

**Expected Output:** JSON response with list of IAM users

## 🏆 Challenge Activity

**Goal:** Download the `lab_policy.json` document using only AWS CLI commands.

### Hints
- Use `aws iam list-policies --scope Local` to find customer-managed policies
- Use `aws iam get-policy-version` to retrieve the policy document
- Use `>` to redirect output to a file
- Reference the [IAM CLI documentation](https://docs.aws.amazon.com/cli/latest/reference/iam/)

## 💡 Lab Solution

### Step 1: List Customer-Managed Policies
```bash
aws iam list-policies --scope Local
```

### Step 2: Retrieve Policy JSON
```bash
aws iam get-policy-version \
  --policy-arn arn:aws:iam::038946776283:policy/lab_policy \
  --version-id v1 \
  > lab_policy.json
```

### Step 3: Verify the File
```bash
cat lab_policy.json
```

## 🔑 Key Commands

| Command | Description |
|---------|-------------|
| `aws configure` | Configure AWS CLI credentials |
| `aws --version` | Check AWS CLI version |
| `aws help` | View AWS CLI documentation |
| `aws iam list-users` | List all IAM users |
| `aws iam list-policies --scope Local` | List customer-managed policies |
| `aws iam get-policy-version` | Retrieve specific policy version |

## 📚 Key Takeaways

- ✨ AWS CLI provides programmatic access to AWS services
- 🔐 AWS CLI uses **Access Keys** (Access Key ID + Secret Access Key)
- 🖥️ AWS Console uses **Username + Password**
- 📝 IAM policies can be managed through both Console and CLI
- 🔄 AWS CLI is an alternative interface to the AWS Management Console

## 🔗 Resources

- [AWS CLI Official Documentation](https://docs.aws.amazon.com/cli/)
- [AWS CLI Command Reference - IAM](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html)
- [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/)
- [AWS CLI Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## 📝 Files in This Repository

```
.
├── README.md                 # This file
├── lab_policy.json          # Retrieved IAM policy document
└── screenshots/             # Lab screenshots (optional)
    ├── ssh-connection.png
    ├── aws-cli-install.png
    └── policy-retrieval.png
⚠️ Important Notes

🚫 Do not change the lab Region unless instructed
🔒 Never commit AWS credentials to version control
⏱️ Lab environment has a time limit
💾 Secret access keys are only shown once at creation

✅ Lab Completion Checklist

 SSH connection established
 AWS CLI installed and verified
 AWS CLI configured with credentials
 IAM user list retrieved successfully
 lab_policy.json downloaded via CLI

🎓 Author
Lab completed as part of AWS CLI training curriculum.
📄 License
This lab is for educational purposes only.

Lab Status: ✅ Complete