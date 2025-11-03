# AWS EC2 Instance Creation Lab 🚀

![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Amazon EC2](https://img.shields.io/badge/Amazon%20EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

A comprehensive hands-on lab demonstrating two methods for launching Amazon EC2 instances: using the AWS Management Console and the AWS Command Line Interface (CLI).

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Lab Tasks](#lab-tasks)
  - [Task 1: Launch Bastion Host (Console)](#task-1-launch-bastion-host-console)
  - [Task 2: Connect to Bastion Host](#task-2-connect-to-bastion-host)
  - [Task 3: Launch Web Server (CLI)](#task-3-launch-web-server-cli)
- [Optional Challenges](#optional-challenges)
- [Key Takeaways](#key-takeaways)
- [Troubleshooting](#troubleshooting)
- [Resources](#resources)

## 🎯 Overview

This lab teaches you how to:
- ✅ Launch EC2 instances using AWS Management Console
- ✅ Connect securely using EC2 Instance Connect
- ✅ Automate EC2 deployment with AWS CLI
- ✅ Configure web servers with user data scripts
- ✅ Manage security groups and IAM roles

**Duration:** ~45 minutes

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Lab VPC                          │
│                                                     │
│  ┌──────────────────────────────────────────────┐  │
│  │           Public Subnet                      │  │
│  │                                               │  │
│  │   ┌─────────────────┐                        │  │
│  │   │  Bastion Host   │                        │  │
│  │   │  Amazon Linux 2 │◄─── EC2 Instance       │  │
│  │   │  t3.micro       │     Connect            │  │
│  │   └────────┬────────┘                        │  │
│  │            │                                  │  │
│  │            │ AWS CLI                          │  │
│  │            ▼                                  │  │
│  │   ┌─────────────────┐                        │  │
│  │   │   Web Server    │                        │  │
│  │   │  Amazon Linux 2 │◄─── HTTP Traffic       │  │
│  │   │  t3.micro       │                        │  │
│  │   └─────────────────┘                        │  │
│  │                                               │  │
│  └──────────────────────────────────────────────┘  │
│                                                     │
└─────────────────────────────────────────────────────┘
```

## 📦 Prerequisites

- AWS Account with lab environment access
- Basic understanding of:
  - EC2 concepts
  - Linux command line
  - Networking fundamentals
- Web browser (Chrome, Firefox, or Safari recommended)

## 🚀 Getting Started

1. **Launch the Lab**
   ```
   Click "Start Lab" → Wait for "Lab status: ready" → Click "AWS"
   ```

2. **Access AWS Console**
   - The console opens in a new tab
   - You're automatically signed in
   - Arrange windows side-by-side with instructions

> ⚠️ **Important:** Do not change the lab Region unless instructed

## 📝 Lab Tasks

### Task 1: Launch Bastion Host (Console)

#### Step-by-Step Instructions

1. **Navigate to EC2**
   - Search for `EC2` in AWS Console
   - Click **Launch instance**

2. **Configure Instance**

   | Setting | Value |
   |---------|-------|
   | **Name** | `Bastion host` |
   | **AMI** | Amazon Linux 2 |
   | **Instance Type** | t3.micro |
   | **Key Pair** | Proceed without key pair |
   | **VPC** | Lab VPC |
   | **Subnet** | Public Subnet |
   | **Auto-assign IP** | Enable |

3. **Security Group**
   ```
   Name: Bastion security group
   Description: Permit SSH connections
   ```

4. **Advanced Details**
   - **IAM Instance Profile:** `Bastion-Role`

5. **Launch**
   - Review configuration
   - Click **Launch instance**
   - Click **View all instances**

---

### Task 2: Connect to Bastion Host

1. Select the **Bastion host** instance
2. Click **Connect**
3. Choose **EC2 Instance Connect** tab
4. Click **Connect**

🎉 You now have a browser-based terminal!

---

### Task 3: Launch Web Server (CLI)

#### 1️⃣ Retrieve AMI ID

```bash
# Set the Region
AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
export AWS_DEFAULT_REGION=${AZ::-1}

# Retrieve latest Linux AMI
AMI=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query 'Parameters[0].[Value]' --output text)
echo $AMI
```

**Expected Output:** `ami-xxxxxxxxxxxxxxxxx`

#### 2️⃣ Retrieve Subnet ID

```bash
SUBNET=$(aws ec2 describe-subnets --filters 'Name=tag:Name,Values=Public Subnet' --query Subnets[].SubnetId --output text)
echo $SUBNET
```

**Expected Output:** `subnet-xxxxxxxxxxxxxxxxx`

#### 3️⃣ Retrieve Security Group ID

```bash
SG=$(aws ec2 describe-security-groups --filters Name=group-name,Values=WebSecurityGroup --query SecurityGroups[].GroupId --output text)
echo $SG
```

**Expected Output:** `sg-xxxxxxxxxxxxxxxxx`

#### 4️⃣ Download User Data Script

```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-1-23732/171-lab-JAWS-create-ec2/s3/UserData.txt
```

View the script:
```bash
cat UserData.txt
```

This script installs Apache and deploys a web application.

#### 5️⃣ Launch the Instance

```bash
INSTANCE=$(\
aws ec2 run-instances \
--image-id $AMI \
--subnet-id $SUBNET \
--security-group-ids $SG \
--user-data file:///home/ec2-user/UserData.txt \
--instance-type t3.micro \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Web Server}]' \
--query 'Instances[*].InstanceId' \
--output text \
)
echo $INSTANCE
```

**Expected Output:** `i-xxxxxxxxxxxxxxxxx`

#### 6️⃣ Monitor Instance Status

```bash
aws ec2 describe-instances --instance-ids $INSTANCE --query 'Reservations[].Instances[].State.Name' --output text
```

🔄 **Repeat until status = `running`**

#### 7️⃣ Get Public DNS & Test

```bash
aws ec2 describe-instances --instance-ids $INSTANCE --query Reservations[].Instances[].PublicDnsName --output text
```

Copy the DNS name and open it in your browser!

**Example:** `http://ec2-xx-xx-xx-xx.us-west-2.compute.amazonaws.com`

✅ **Success:** You should see a web page!

---

## 🎯 Optional Challenges

### Challenge 1: Fix Connection Issue
- **Task:** Connect to "Misconfigured Web Server" instance
- **Hint:** Check security group SSH rules (port 22)

### Challenge 2: Fix Web Server
- **Task:** Make the misconfigured web server accessible
- **Hint:** Check security group HTTP rules (port 80)

---

## 💡 Key Takeaways

### When to Use Each Method

| Method | Use Case | Benefits |
|--------|----------|----------|
| **AWS Console** | One-off instances | Quick, visual, beginner-friendly |
| **AWS CLI** | Automation | Repeatable, scriptable, consistent |
| **CloudFormation** | Infrastructure as Code | Version control, full stack deployment |

### Important Concepts

- **AMI:** Template containing OS and software
- **Instance Type:** Determines CPU, memory, storage
- **Security Group:** Virtual firewall controlling traffic
- **User Data:** Bootstrap scripts that run at launch
- **IAM Role:** Grants AWS service permissions to instances

---

## 🔧 Troubleshooting

### Cannot Connect to Instance
```
✗ Problem: EC2 Instance Connect fails
✓ Solution: Check security group allows SSH (port 22)
✓ Solution: Verify instance is in running state
✓ Solution: Ensure public IP is assigned
```

### Web Server Not Accessible
```
✗ Problem: Browser shows "Connection refused"
✓ Solution: Add HTTP (port 80) rule to security group
✓ Solution: Check user data script execution logs
✓ Solution: Verify instance is running
```

### CLI Commands Fail
```
✗ Problem: "Access Denied" errors
✓ Solution: Verify Bastion-Role is attached
✓ Solution: Check environment variables are set
✓ Solution: Confirm you're in correct Region
```

### Session Disconnects
```
✗ Problem: Lost environment variables
✓ Solution: Refresh browser and re-run ALL commands
✓ Solution: Start from Step 1 to reset variables
```

---

## 📚 Resources

### AWS Documentation
- [Amazon EC2 User Guide](https://docs.aws.amazon.com/ec2/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/ec2/)
- [EC2 Instance Connect](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html)
- [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

### Learning Resources
- [AWS Training and Certification](https://aws.amazon.com/training/)
- [EC2 Best Practices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html)

---

## 🎓 What You Learned

By completing this lab, you now know how to:

- [x] Launch EC2 instances using the Management Console
- [x] Configure networking (VPC, subnets, security groups)
- [x] Assign IAM roles to instances
- [x] Connect securely with EC2 Instance Connect
- [x] Automate deployments with AWS CLI
- [x] Use Systems Manager Parameter Store
- [x] Bootstrap instances with user data scripts
- [x] Query AWS resources programmatically
- [x] Troubleshoot common EC2 issues

---

## 🧹 Cleanup

When finished:
1. Click **End Lab**
2. Confirm **Yes**
3. Wait for resources to terminate
4. Close the lab window

> 💰 **Note:** Lab resources are automatically cleaned up. No manual deletion needed!

---

## 📄 License

This lab guide is based on AWS Training materials.

---

## 🤝 Contributing

Found an issue or have suggestions? Feel free to:
- Open an issue
- Submit a pull request
- Share your feedback

---

## 📞 Support

- **AWS Support:** [support.aws.amazon.com](https://support.aws.amazon.com)
- **Lab Issues:** Contact your instructor or AWS Training support

---

<div align="center">

**Made with ☁️ by AWS Training**

⭐ Star this repo if you found it helpful!

</div>