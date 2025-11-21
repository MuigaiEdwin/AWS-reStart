# Introduction to Amazon EC2 Lab

## Overview

This lab provides a hands-on introduction to Amazon Elastic Compute Cloud (Amazon EC2), covering the fundamental operations of launching, managing, resizing, and monitoring cloud instances.

Amazon EC2 is a web service that provides resizable compute capacity in the cloud, designed to make web-scale cloud computing accessible to developers. With EC2, you can obtain and configure computing capacity in minutes, scale resources on-demand, and pay only for what you use.

## Learning Objectives

By completing this lab, you will be able to:

- Launch an EC2 web server with termination protection enabled
- Monitor EC2 instance health and performance
- Configure security groups to control network access
- Resize EC2 instances and storage volumes
- Test and utilize termination protection
- Properly terminate EC2 instances

## Lab Duration

Approximately 45 minutes

## Prerequisites

- AWS account access
- Familiarity with AWS Management Console basics
- Web browser with pop-up windows enabled

## Lab Architecture

This lab uses the following AWS resources:
![Lab Dashboard Screenshot](/screenshots/intro-ec2.jpeg)
- **Amazon EC2 Instance**: A t3.micro instance (later resized to t3.small) running Amazon Linux 2023
- **Amazon EBS Volume**: 8 GiB root volume (later resized to 10 GiB)
- **Security Group**: Custom security group with configurable inbound rules
- **Lab VPC**: Isolated virtual private cloud environment

## Tasks Overview

### Task 1: Launch Your EC2 Instance

Configure and launch a web server instance with the following specifications:

- **Instance Name**: Web Server
- **AMI**: Amazon Linux 2023
- **Instance Type**: t3.micro (2 vCPU, 1 GiB memory)
- **Termination Protection**: Enabled
- **Key Pair**: None (SSH access not required)
- **Security Group**: Web Server security group (no inbound rules initially)
- **Storage**: 8 GiB root volume
- **User Data Script**: Installs and configures Apache web server

The provided user data script performs the following:
```bash
#!/bin/bash
yum -y install httpd
systemctl enable httpd
systemctl start httpd
echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
```

### Task 2: Monitor Your Instance

Explore EC2 monitoring capabilities:

- Verify instance status checks (System reachability and Instance reachability)
- Review CloudWatch metrics in the Monitoring tab
- Capture instance screenshots for troubleshooting
- Understand basic (5-minute) and detailed (1-minute) monitoring options

### Task 3: Update Security Group and Access Web Server

- Retrieve the instance's public IPv4 address
- Attempt to access the web server (initial access will fail)
- Update security group with HTTP inbound rule (Port 80, Source: Anywhere-IPv4)
- Successfully access the web server and verify the "Hello From Your Web Server!" message

### Task 4: Resize Your Instance

Modify instance resources without data loss:

- **Stop the instance** (no charges apply while stopped; storage charges continue)
- **Change instance type** from t3.micro to t3.small (doubles available memory)
- **Resize EBS volume** from 8 GiB to 10 GiB
- **Start the instance** with new configuration

### Task 5: Test Termination Protection

Understand and demonstrate termination protection:

- Attempt to terminate instance (operation fails due to protection)
- Disable termination protection via Instance Settings
- Successfully terminate the instance
- Verify instance termination

## Key Concepts Covered

### Amazon Machine Images (AMI)
Provides the template for launching instances, including OS, applications, and launch permissions.

### Instance Types
EC2 offers various instance types optimized for different workloads. This lab uses t3 instances, which are general-purpose and cost-effective.

### Security Groups
Virtual firewalls that control inbound and outbound traffic. Rules can be modified at any time and automatically apply to associated instances.

### Amazon EBS Volumes
Network-attached virtual storage for EC2 instances. Volumes can be resized without stopping the instance (for certain configurations).

### Termination Protection
Prevents accidental instance deletion by requiring explicit disabling before termination is allowed.

### User Data
Custom scripts executed during instance launch, enabling automated configuration and software installation.

## Troubleshooting Tips

- **Access Denied Error**: Close error box and retry "Start Lab"
- **Lab Status Indicators**: 
  - Red circle = Lab not started
  - Yellow circle = Lab starting
  - Green circle = Lab ready
- **Pop-up Windows Blocked**: Enable pop-ups in browser settings
- **Cannot Access Web Server**: Verify security group rules allow HTTP (port 80)
- **Instance Not Responding**: Check instance status checks and CloudWatch metrics

## Important Notes

- Do not change the lab region unless instructed
- Resources take a few minutes to provision after lab starts
- When stopping instances, EBS volume charges continue (only compute charges stop)
- This lab uses restricted instance types to manage costs

## AWS Services Used

- Amazon EC2 (Elastic Compute Cloud)
- Amazon EBS (Elastic Block Store)
- Amazon VPC (Virtual Private Cloud)
- Amazon CloudWatch
- AWS Management Console

## Next Steps

After completing this lab, explore:

- Advanced EC2 features (Elastic IPs, Auto Scaling, Load Balancing)
- Security best practices (IAM roles, security group refinement)
- Cost optimization strategies
- High availability and disaster recovery patterns
- Infrastructure as Code (CloudFormation, Terraform)

## Resources

- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Security Groups Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
- [EBS Volumes Documentation](https://docs.aws.amazon.com/ebs/)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025