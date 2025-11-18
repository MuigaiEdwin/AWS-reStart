# AWS CloudFormation Troubleshooting Lab

A comprehensive hands-on activity for learning AWS CloudFormation deployment, troubleshooting, and best practices through practical scenarios.

## 📋 Overview

This lab provides practical experience with AWS CloudFormation by working through real-world troubleshooting scenarios. You'll learn to identify and resolve common deployment issues, detect configuration drift, and manage stack lifecycle operations using the AWS CLI.

## 🎯 Learning Objectives

After completing this lab, you will be able to:

- Query JSON-formatted documents using JMESPath
- Troubleshoot CloudFormation stack deployments via AWS CLI
- Analyze EC2 instance logs to diagnose deployment failures
- Detect and identify configuration drift in CloudFormation-managed resources
- Resolve failed stack deletion scenarios
- Implement Infrastructure as Code (IaC) best practices

## 🏗️ Architecture

The lab deploys the following AWS resources:

![Lab Architecture](/screenshots/troubleshoot-cloudfront.png)

- **VPC2** - Custom Virtual Private Cloud
- **Public Subnet** - Network segment for internet-accessible resources
- **CLI Host** - EC2 instance for executing AWS CLI commands
- **Web Server** - EC2 instance running Apache httpd
- **S3 Bucket** - Object storage created by CloudFormation
- **Security Groups** - Network access controls
- **WaitCondition** - Ensures userdata script completion

## ⏱️ Duration

Approximately **75 minutes** to complete all tasks

## 📚 Lab Structure

### Task 1: JMESPath Query Practice
Learn to query JSON documents using JMESPath expressions for filtering AWS CLI output.

**Key Skills:**
- Array indexing and filtering
- Attribute selection
- Complex query expressions

### Task 2: Troubleshooting Stack Deployment
Deploy a CloudFormation stack with intentional errors and learn systematic troubleshooting.

**Scenarios Covered:**
- Stack creation failure analysis
- Rollback prevention for debugging
- Log file analysis on EC2 instances
- Template error correction

**Key Commands:**
```bash
# Create stack
aws cloudformation create-stack \
  --stack-name myStack \
  --template-body file://template1.yaml \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameters ParameterKey=KeyName,ParameterValue=vockey

# Monitor stack resources
aws cloudformation describe-stack-resources \
  --stack-name myStack

# Analyze failed events
aws cloudformation describe-stack-events \
  --stack-name myStack \
  --query "StackEvents[?ResourceStatus == 'CREATE_FAILED']"
```

![Lab Dashboard Screenshot](/screenshots/troubleshootcloudfront.png)

### Task 3: Configuration Drift Detection
Manually modify resources and use CloudFormation drift detection to identify changes.

**Activities:**
- Manual security group modification
- S3 bucket object addition
- Drift detection and analysis

**Key Commands:**
```bash
# Detect drift
aws cloudformation detect-stack-drift --stack-name myStack

# Review drift status
aws cloudformation describe-stack-resource-drifts \
  --stack-name myStack \
  --stack-resource-drift-status-filters MODIFIED
```

### Task 4: Stack Deletion Challenge
Resolve a failed stack deletion while preserving S3 bucket contents.

**Challenge Goal:** Delete the CloudFormation stack while retaining the S3 bucket and its objects.

## 🔧 Prerequisites

- AWS Account with appropriate permissions
- Basic knowledge of:
  - Linux command line
  - SSH connections
  - AWS CLI basics
  - JSON format

## 🚀 Getting Started

### Windows Users
1. Download the `.ppk` file from lab credentials
2. Use PuTTY to connect to CLI Host
3. Follow [AWS PuTTY connection guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)

### macOS/Linux Users
```bash
# Download .pem file and set permissions
chmod 400 labsuser.pem

# Connect to CLI Host
ssh -i labsuser.pem ec2-user@<PublicIP>
```

### Configure AWS CLI
```bash
# Discover region
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region

# Configure credentials
aws configure
```

## 🐛 Common Issues & Solutions

### Issue: WaitCondition Timeout
**Symptom:** Stack creation fails with wait condition timeout

**Root Cause:** Error in userdata script prevents completion signal

**Solution:** 
1. Use `--on-failure DO_NOTHING` to prevent rollback
2. SSH to EC2 instance
3. Check `/var/log/cloud-init-output.log`
4. Fix template errors and redeploy

### Issue: Stack Deletion Fails
**Symptom:** S3 bucket fails to delete

**Root Cause:** Bucket contains objects

**Solution:** Use `--retain-resources` parameter to preserve specific resources

## 📖 Key CloudFormation Concepts

### Stack Statuses
- `CREATE_IN_PROGRESS` - Resources being created
- `CREATE_COMPLETE` - All resources successfully created
- `CREATE_FAILED` - Stack creation failed
- `ROLLBACK_IN_PROGRESS` - Reverting changes after failure
- `ROLLBACK_COMPLETE` - All changes reverted
- `DELETE_IN_PROGRESS` - Resources being deleted
- `DELETE_FAILED` - Stack deletion failed

### Drift Detection
CloudFormation can detect when resources are modified outside of stack operations:
- `IN_SYNC` - Resource matches template
- `MODIFIED` - Resource has been changed manually
- `DELETED` - Resource no longer exists
- `NOT_CHECKED` - Resource type doesn't support drift detection

## 💡 Best Practices

1. **Always use version control** for CloudFormation templates
2. **Test templates** in non-production environments first
3. **Use WaitConditions** to validate userdata script execution
4. **Enable termination protection** for production stacks
5. **Never manually modify** CloudFormation-managed resources
6. **Use drift detection** regularly to maintain consistency
7. **Tag all resources** for better organization and cost tracking

## 🔍 Useful Commands Reference

```bash
# List all stacks
aws cloudformation list-stacks

# Get stack outputs
aws cloudformation describe-stacks \
  --stack-name myStack \
  --query 'Stacks[0].Outputs'

# Validate template syntax
aws cloudformation validate-template \
  --template-body file://template1.yaml

# Update existing stack
aws cloudformation update-stack \
  --stack-name myStack \
  --template-body file://template1.yaml

# Delete stack with retained resources
aws cloudformation delete-stack \
  --stack-name myStack \
  --retain-resources <LogicalResourceId>
```

## 📝 Lab Files

- `template1.yaml` - CloudFormation template for web server deployment
- `labsuser.pem/ppk` - SSH key pair for EC2 access

## 🎓 Skills Developed

- Infrastructure as Code (IaC) implementation
- AWS CLI proficiency
- Log analysis and debugging
- JSON query operations with JMESPath
- CloudFormation stack lifecycle management
- Drift detection and remediation

## 📚 Additional Resources

- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/cloudformation/)
- [JMESPath Tutorial](https://jmespath.org/tutorial.html)
- [CloudFormation Best Practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)

## 🤝 Business Context

This lab simulates a real-world scenario where Sofía, from a café business, learns to implement Infrastructure as Code to:
- Reliably create matching development and production environments
- Enable efficient feature development workflows
- Leverage drift detection for maintaining infrastructure consistency
- Manage complex multi-service cloud deployments

## ⚠️ Important Notes

- Lab resources incur AWS charges - remember to clean up after completion
- The lab uses specific AMI IDs that may vary by region
- WaitCondition has a 60-second timeout - ensure userdata scripts complete quickly
- S3 buckets must be empty before CloudFormation can delete them

## 🏆 Success Criteria

You've successfully completed the lab when you can:
1. ✅ Deploy a CloudFormation stack without errors
2. ✅ Identify and fix template issues using log analysis
3. ✅ Detect configuration drift
4. ✅ Delete a stack while retaining specific resources

---

**Last Updated:** November 2025  
**Lab Version:** 1.0  
**Difficulty Level:** Intermediate