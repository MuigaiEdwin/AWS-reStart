# AWS Auto Scaling Lab - Complete Guide

A comprehensive hands-on lab demonstrating how to implement auto scaling infrastructure on AWS using EC2, Application Load Balancer, and Auto Scaling Groups.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Lab Objectives](#lab-objectives)
- [Setup Instructions](#setup-instructions)
- [Tasks](#tasks)
- [Testing](#testing)
- [Cleanup](#cleanup)
- [Troubleshooting](#troubleshooting)
- [Key Concepts](#key-concepts)

## 🎯 Overview

This lab guides you through creating a dynamically scalable web application infrastructure on AWS. You'll use the AWS CLI and Management Console to build an auto-scaling environment that automatically adjusts capacity based on CPU utilization.

**Duration:** Approximately 45 minutes

## 🏗️ Architecture

### Starting Architecture
- Command Host instance in a public subnet for AWS CLI operations

### Final Architecture
- Application Load Balancer distributing traffic
- Auto Scaling Group managing EC2 instances
- Instances deployed across multiple Availability Zones in private subnets
- CloudWatch alarms monitoring CPU utilization
- Target tracking scaling policy maintaining 50% average CPU

## ✅ Prerequisites

- AWS Account with appropriate permissions
- Basic understanding of:
  - Amazon EC2
  - AWS CLI
  - Load balancers
  - Auto Scaling concepts
- Lab environment provisioned (includes Command Host instance)

## 🎓 Lab Objectives

By completing this lab, you will learn to:

1. Create EC2 instances using AWS CLI commands
2. Generate custom AMIs from running instances
3. Create EC2 launch templates
4. Configure Application Load Balancers
5. Set up Auto Scaling groups with scaling policies
6. Implement dynamic scaling based on CPU metrics

## 🚀 Setup Instructions

### 1. Access the Lab Environment

1. Launch the lab and wait for "Lab status: ready"
2. Open the AWS Management Console
3. Ensure you're in the correct region (us-west-2)

### 2. Connect to Command Host

```bash
# Use EC2 Instance Connect to connect to the Command Host instance
# Navigate to EC2 > Instances > Command Host > Connect
```

### 3. Configure AWS CLI

```bash
# Verify region
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region

# Configure AWS CLI
aws configure
# Press Enter for Access Key ID
# Press Enter for Secret Access Key
# Enter your region (e.g., us-west-2)
# Enter 'json' for output format

# Navigate to scripts directory
cd /home/ec2-user/
```

## 📝 Tasks

### Task 1: Creating a Custom AMI

#### 1.1 Review UserData Script

```bash
more UserData.txt
```

This script installs and configures a PHP web application for CPU load testing.

#### 1.2 Launch Web Server Instance

Replace placeholders with your actual values from the lab Details panel:

```bash
aws ec2 run-instances \
  --key-name <KEYNAME> \
  --instance-type t3.micro \
  --image-id <AMIID> \
  --user-data file:///home/ec2-user/UserData.txt \
  --security-group-ids <HTTPACCESS> \
  --subnet-id <SUBNETID> \
  --associate-public-ip-address \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer}]' \
  --output text \
  --query 'Instances[*].InstanceId'
```

Save the returned Instance ID for later use.

#### 1.3 Wait for Instance to Start

```bash
aws ec2 wait instance-running --instance-ids <NEW-INSTANCE-ID>
```

#### 1.4 Get Public DNS Name

```bash
aws ec2 describe-instances \
  --instance-id <NEW-INSTANCE-ID> \
  --query 'Reservations[0].Instances[0].NetworkInterfaces[0].Association.PublicDnsName'
```

Test the web server by visiting: `http://<PUBLIC-DNS-ADDRESS>/index.php`

Wait 5 minutes for the web server to fully initialize.

#### 1.5 Create AMI

```bash
aws ec2 create-image \
  --name WebServerAMI \
  --instance-id <NEW-INSTANCE-ID>
```

### Task 2: Creating Auto Scaling Environment

#### 2.1 Create Application Load Balancer

1. Navigate to EC2 > Load Balancers > Create load balancer
2. Select Application Load Balancer
3. Configure:
   - **Name:** WebServerELB
   - **VPC:** Lab VPC
   - **Subnets:** Public Subnet 1 and Public Subnet 2
   - **Security Group:** HTTPAccess
4. Create target group:
   - **Name:** webserver-app
   - **Target type:** Instances
   - **Health check path:** /index.php
5. Complete load balancer creation
6. Save the DNS name for later testing

#### 2.2 Create Launch Template

1. Navigate to EC2 > Launch Templates > Create launch template
2. Configure:
   - **Name:** web-app-launch-template
   - **AMI:** WebServerAMI (under My AMIs tab)
   - **Instance type:** t3.micro
   - **Key pair:** Don't include in launch template
   - **Security group:** HTTPAccess
   - Enable Auto Scaling guidance
3. Create template

#### 2.3 Create Auto Scaling Group

1. From launch template, select Actions > Create Auto Scaling group
2. Configure:
   - **Name:** Web App Auto Scaling Group
   - **VPC:** Lab VPC
   - **Subnets:** Private Subnet 1 and Private Subnet 2
3. Load balancing:
   - Attach to existing load balancer
   - Target group: webserver-app | HTTP
   - Enable ELB health checks
4. Group size:
   - **Desired capacity:** 2
   - **Minimum capacity:** 2
   - **Maximum capacity:** 4
5. Scaling policy:
   - **Type:** Target tracking scaling policy
   - **Metric:** Average CPU utilization
   - **Target value:** 50%
6. Add tag:
   - **Key:** Name
   - **Value:** WebApp
7. Create Auto Scaling group

## 🧪 Testing

### Verify Auto Scaling Configuration

1. Wait for instances to reach "2/2 checks passed" status
2. Check target group health (Target Groups > webserver-app > Targets tab)
3. Verify both instances show "healthy" status

### Test Scale-Out Behavior

1. Access load balancer DNS name in browser
2. Click "Start Stress" button to simulate CPU load
3. Monitor Auto Scaling Groups > Activity tab
4. Observe new instance launch after ~3-5 minutes when CPU exceeds 50%

## 🧹 Cleanup

To avoid charges, delete resources in this order:

1. Auto Scaling Group
2. Launch Template
3. Load Balancer
4. Target Group
5. EC2 Instances
6. Custom AMI
7. Associated snapshots

## 🔧 Troubleshooting

### Common Issues

**Instance ID Error**
```
Error: Invalid id: "d0eb945b9c782ab7"
```
- Ensure instance ID includes `i-` prefix (e.g., `i-d0eb945b9c782ab7`)

**Command Not Found Errors**
- Write AWS CLI commands on a single line or use backslash (`\`) for line continuation
- Ensure no spaces after backslashes

**Web Server Not Loading**
- Wait at least 5 minutes after instance launch
- Verify security group allows HTTP traffic (port 80)
- Check instance status is "2/2 checks passed"

**t3.micro Not Available**
- Try t2.micro instance type instead

## 💡 Key Concepts

### Auto Scaling Benefits
- **High availability:** Distributes instances across multiple AZs
- **Fault tolerance:** Automatically replaces unhealthy instances
- **Cost optimization:** Scales in during low demand
- **Performance:** Scales out during high demand

### Scaling Policies
- **Target Tracking:** Maintains specific metric value (used in this lab)
- **Step Scaling:** Adds/removes capacity based on metric thresholds
- **Simple Scaling:** Single scaling adjustment based on alarm

### Health Checks
- **EC2 Status Checks:** Instance and system reachability
- **ELB Health Checks:** Application-level health verification

## 📚 Additional Resources

- [AWS Auto Scaling Documentation](https://docs.aws.amazon.com/autoscaling/)
- [Application Load Balancer Guide](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/)
- [EC2 Launch Templates](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html)

## 📄 License

This lab guide is for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Note:** This lab uses AWS resources that may incur charges. Always clean up resources after completion.