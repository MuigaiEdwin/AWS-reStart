# AWS Café Instance Optimization Lab

## Overview

This lab demonstrates how to optimize AWS resources to reduce costs by decommissioning a local database and downsizing an EC2 instance. The activity simulates a real-world scenario where the Café web application has migrated its database to Amazon RDS, creating opportunities for cost optimization.

## Lab Objectives

After completing this lab, you will be able to:

- Optimize an Amazon EC2 instance to reduce operational costs
- Use the AWS CLI to manage EC2 instances
- Use the AWS Pricing Calculator to estimate AWS service costs
- Calculate projected cost savings from resource optimization

## Architecture

![Lab Dashboard Screenshot](/screenshots/optimize-resources-architecture.png)
### Before Optimization
- **EC2 Instance**: t3.small with 40GB storage
- Local MariaDB database (decommissioned but still consuming resources)
- Amazon RDS MariaDB instance (20GB)

### After Optimization
- **EC2 Instance**: t3.micro with 20GB storage
- Local database removed
- Amazon RDS MariaDB instance (20GB)

## Prerequisites

- AWS account with appropriate permissions
- Basic understanding of AWS EC2 and RDS services
- Familiarity with SSH and command-line interfaces
- PuTTY (for Windows users) or Terminal (for macOS/Linux users)

## Lab Duration

Approximately 50 minutes

## Tasks

### Task 1: Optimize the Website to Reduce Costs

#### 1.1 Connect to the Café Instance via SSH

**Windows Users:**
1. Download the PPK file from the lab credentials
2. Use PuTTY to connect to the instance
3. Configure PuTTY session with the Public IP address

**macOS/Linux Users:**
1. Download the PEM file from the lab credentials
2. Set appropriate permissions: `chmod 400 labsuser.pem`
3. Connect via SSH: `ssh -i labsuser.pem ec2-user@<public-ip>`

#### 1.2 Configure AWS CLI

```bash
# Discover the region
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region

# Configure AWS CLI
aws configure
```

Enter your AWS credentials when prompted:
- AWS Access Key ID
- AWS Secret Access Key
- Default region name
- Default output format: json

#### 1.3 Uninstall MariaDB and Resize Instance

```bash
# Stop and remove MariaDB
sudo systemctl stop mariadb
sudo yum -y remove mariadb-server

# Get Instance ID
aws ec2 describe-instances \
--filters "Name=tag:Name,Values= CafeInstance" \
--query "Reservations[*].Instances[*].InstanceId"

# Stop the instance
aws ec2 stop-instances --instance-ids <CafeInstance-Instance-ID>

# Modify instance type to t3.micro
aws ec2 modify-instance-attribute \
--instance-id <CafeInstance-Instance-ID> \
--instance-type "{\"Value\": \"t3.micro\"}"

# Start the instance
aws ec2 start-instances --instance-ids <CafeInstance-Instance-ID>

# Check instance status
aws ec2 describe-instances \
--instance-ids <CafeInstance-Instance-ID> \
--query "Reservations[*].Instances[*].[InstanceType,PublicDnsName,PublicIpAddress,State.Name]"
```

### Task 2: Use AWS Pricing Calculator

#### 2.1 Calculate Costs Before Optimization

Visit the [AWS Pricing Calculator](https://calculator.aws) and configure:

**Amazon EC2:**
- Instance type: t3.small
- Operating system: Linux
- Utilization: 100% per month
- EBS: General Purpose SSD (gp2), 40 GB

**Amazon RDS:**
- Instance class: db.t3.micro
- Engine: MariaDB
- Storage: 20 GB

#### 2.2 Calculate Costs After Optimization

Modify the calculator with optimized values:

**Amazon EC2:**
- Instance type: t3.micro
- EBS: General Purpose SSD (gp2), 20 GB

#### 2.3 Cost Savings Analysis

Example calculations (pricing as of April 2020):

```
Before Optimization:
- Amazon EC2: $20.89
- Amazon RDS: $14.71
Total: $35.60/month

After Optimization:
- Amazon EC2: $10.47
- Amazon RDS: $14.71
Total: $25.18/month

Monthly Savings: $10.42 (29% reduction)
```

## Key Learnings

1. **Resource Optimization**: Removing unused services and downsizing instances can significantly reduce costs
2. **AWS CLI Proficiency**: Managing EC2 instances programmatically using AWS CLI
3. **Cost Estimation**: Using AWS Pricing Calculator for financial planning
4. **Database Migration Benefits**: Separating database workloads enables optimization opportunities

## Business Impact

This optimization demonstrates how identifying and eliminating waste in cloud infrastructure can lead to meaningful cost savings. Even small monthly savings compound over time and contribute to business sustainability.

## Security Notes

- Always secure your SSH keys (PEM/PPK files)
- Use IAM roles and least privilege access
- Regularly audit and optimize resource usage
- Never commit credentials to version control

## Troubleshooting

### Instance Won't Start
- Verify instance ID is correct
- Check service limits in your AWS account
- Review CloudWatch logs for errors

### SSH Connection Issues
- Verify security group allows SSH (port 22)
- Confirm public IP address is correct
- Check key file permissions (400 for PEM files)

### Website Not Accessible
- Wait for instance to fully initialize
- Verify security group allows HTTP (port 80)
- Check that the web service started properly

## Additional Resources

- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/)
- [AWS Pricing Calculator](https://calculator.aws/)
- [AWS Cost Optimization Best Practices](https://aws.amazon.com/pricing/cost-optimization/)

## License

This lab is provided for educational purposes. Please refer to AWS documentation for current pricing and service information.

## Acknowledgments

Lab scenario based on the Café web application migration project, demonstrating real-world cloud optimization practices.

---

**Note**: Pricing examples are for demonstration purposes only. Always refer to the official AWS website for current pricing information.