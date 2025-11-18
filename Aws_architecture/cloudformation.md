# AWS CloudFormation Automation Lab

## Overview

This lab provides hands-on experience with AWS CloudFormation by deploying and managing infrastructure as code. You'll learn how to define, deploy, and modify cloud resources using CloudFormation templates, demonstrating the power of automated infrastructure deployment.

## Learning Objectives

By completing this lab, you will:

- Deploy an AWS CloudFormation stack with a VPC and Security Group
- Configure CloudFormation templates with additional resources (S3, EC2)
- Update existing stacks with modified templates
- Understand the structure and syntax of CloudFormation YAML templates
- Terminate CloudFormation stacks and their associated resources

## Duration

Approximately 45 minutes

## Lab Architecture

![Lab Dashboard Screenshot](/screenshots/initial-cloudfront.png)
The lab progressively builds infrastructure across four tasks:

1. **Task 1**: VPC with Security Group
2. **Task 2**: VPC + Security Group + S3 Bucket
3. **Task 3**: VPC + Security Group + S3 Bucket + EC2 Instance
4. **Task 4**: Clean up (delete all resources)

## Prerequisites

- AWS Account with appropriate permissions
- Basic understanding of AWS services (VPC, EC2, S3)
- Text editor for editing YAML files
- Web browser for AWS Console access

## Template Files

This repository contains the following CloudFormation templates:

- `task1.yaml` - Base template with VPC and Security Group
- `task2.yaml` - Adds Amazon S3 bucket to the stack
- `task3.yaml` - Adds Amazon EC2 instance to the stack

## Lab Tasks

### Task 1: Deploy a CloudFormation Stack

Deploy the initial stack that creates:
- Virtual Private Cloud (VPC)
- Security Group
- Public Subnet and Route Table

**Key Concepts:**
- Parameters section for user inputs
- Resources section for infrastructure definition
- Outputs section for displaying resource information

### Task 2: Add an Amazon S3 Bucket

Modify the template to include an S3 bucket and update the existing stack.

**Learning Points:**
- Editing CloudFormation templates
- Updating stacks without redeploying all resources
- Using AWS S3 Template Snippets documentation

### Task 3: Add an Amazon EC2 Instance

Add an EC2 instance with proper configuration including:
- Amazon Linux 2 AMI (via SSM Parameter Store)
- t3.micro instance type
- Security group association
- Subnet placement
- Resource tagging

**Key Concepts:**
- Using `!Ref` to reference other resources
- AWS Systems Manager Parameter Store for AMI IDs
- Complex resource dependencies

### Task 4: Delete the Stack

Clean up all resources by deleting the CloudFormation stack, demonstrating automatic resource cleanup.

## Template Structure

### Parameters Section
```yaml
Parameters:
  # Used to prompt for inputs like CIDR ranges
```

### Resources Section
```yaml
Resources:
  # Defines infrastructure components
```

### Outputs Section
```yaml
Outputs:
  # Provides information about created resources
```

## Important Notes

- YAML formatting is crucial (indentation uses 2 spaces)
- CloudFormation automatically determines optimal resource creation order
- Stack updates only modify changed resources
- Deleting a stack automatically removes all associated resources
- Use `!Ref` to reference other resources within the template

## Best Practices Demonstrated

1. **Infrastructure as Code**: All infrastructure defined in version-controlled templates
2. **Parameterization**: Using parameters for flexible, reusable templates
3. **Resource References**: Linking resources using `!Ref` for dependencies
4. **Automatic AMI Selection**: Using SSM Parameter Store for region-agnostic AMI selection
5. **Stack Updates**: Incremental changes without full redeployment

## Troubleshooting

- If stack creation fails, check the **Events** tab for error messages
- Verify YAML indentation (use 2 spaces, not tabs)
- Ensure all `!Ref` references point to valid resource names
- Check that custom names don't conflict with existing resources

## Additional Resources

- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
- [Amazon S3 Template Snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-s3.html)
- [AWS::EC2::Instance Documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)
- [AWS Systems Manager Parameter Store](https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/)

## Clean Up

Always remember to delete your CloudFormation stack after completing the lab to avoid unnecessary AWS charges:

```bash
aws cloudformation delete-stack --stack-name Lab
```

Or use the AWS Console to delete the stack as shown in Task 4.

## License

This lab is provided for educational purposes.

## Contributing

If you find issues or have suggestions for improvements, please open an issue or submit a pull request.

---

**Note**: This lab is designed for learning purposes in a controlled environment. Always follow your organization's security and compliance policies when working with AWS resources in production.