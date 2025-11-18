# AWS re/Start Challenge Lab - CloudFormation VPC and EC2 Instance

## Lab Overview

This challenge lab focuses on creating an AWS infrastructure using AWS CloudFormation. You'll build a complete VPC environment with an EC2 instance using Infrastructure as Code (IaC) principles.

## Objectives

Create a CloudFormation template that provisions:
- Amazon Virtual Private Cloud (VPC)
- Internet Gateway attached to the VPC
- Security Group configured to allow SSH access from anywhere
- Private Subnet within the VPC
- Amazon EC2 instance (T3.micro) within the private subnet

**Note:** SSH access to the EC2 instance is not required for successful completion.

## Prerequisites

- Access to AWS Management Console
- Basic understanding of AWS networking concepts
- Familiarity with YAML or JSON syntax

## Step-by-Step Guide

### Step 1: Access the Lab Environment

1. Click **Start Lab** at the top of the lab instructions
2. Wait for the status message "Lab status: in creation"
3. Click **AWS** to open the AWS Management Console in a new tab
4. Arrange windows side-by-side for easy reference

### Step 2: Navigate to CloudFormation

1. In the AWS Console, search for **CloudFormation** in the search bar
2. Click on **CloudFormation** to open the service
3. Ensure you're in the correct region (check top-right corner)

### Step 3: Create Your CloudFormation Template

Create a new file named `vpc-ec2-stack.yaml` with the following structure:

```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: VPC with EC2 instance for re/Start Challenge Lab

Parameters:
  LatestAmiId:
    Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
    Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2

Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
      Tags:
        - Key: Name
          Value: Lab-VPC

  MyInternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: Lab-IGW

  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref MyVPC
      InternetGatewayId: !Ref MyInternetGateway

  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select 
        - 0
        - !GetAZs ''
      Tags:
        - Key: Name
          Value: Lab-Private-Subnet

  EC2SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow SSH from anywhere
      VpcId: !Ref MyVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
      Tags:
        - Key: Name
          Value: Lab-SSH-SG

  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.micro
      ImageId: !Ref LatestAmiId
      SubnetId: !Ref PrivateSubnet
      SecurityGroupIds:
        - !Ref EC2SecurityGroup
      Tags:
        - Key: Name
          Value: Lab-EC2-Instance

Outputs:
  VPCId:
    Description: VPC ID
    Value: !Ref MyVPC
  
  EC2InstanceId:
    Description: EC2 Instance ID
    Value: !Ref MyEC2Instance
  
  SecurityGroupId:
    Description: Security Group ID
    Value: !Ref EC2SecurityGroup
```

**Alternative: If you need a specific region AMI, use this version instead:**

For **us-west-2** (Oregon):
```yaml
AWSTemplateFormatVersion: '2010-09-09'
Description: VPC with EC2 instance for re/Start Challenge Lab

Resources:
  MyVPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: 10.0.0.0/16
      EnableDnsHostnames: true
      EnableDnsSupport: true
      Tags:
        - Key: Name
          Value: Lab-VPC

  MyInternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: Lab-IGW

  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      VpcId: !Ref MyVPC
      InternetGatewayId: !Ref MyInternetGateway

  PrivateSubnet:
    Type: AWS::EC2::Subnet
    Properties:
      VpcId: !Ref MyVPC
      CidrBlock: 10.0.1.0/24
      AvailabilityZone: !Select 
        - 0
        - !GetAZs ''
      Tags:
        - Key: Name
          Value: Lab-Private-Subnet

  EC2SecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupDescription: Allow SSH from anywhere
      VpcId: !Ref MyVPC
      SecurityGroupIngress:
        - IpProtocol: tcp
          FromPort: 22
          ToPort: 22
          CidrIp: 0.0.0.0/0
      Tags:
        - Key: Name
          Value: Lab-SSH-SG

  MyEC2Instance:
    Type: AWS::EC2::Instance
    Properties:
      InstanceType: t3.micro
      ImageId: ami-05134c8ef96964280
      SubnetId: !Ref PrivateSubnet
      SecurityGroupIds:
        - !Ref EC2SecurityGroup
      Tags:
        - Key: Name
          Value: Lab-EC2-Instance

Outputs:
  VPCId:
    Description: VPC ID
    Value: !Ref MyVPC
  
  EC2InstanceId:
    Description: EC2 Instance ID
    Value: !Ref MyEC2Instance
  
  SecurityGroupId:
    Description: Security Group ID
    Value: !Ref EC2SecurityGroup
```

### Step 4: Deploy the CloudFormation Stack

#### Option A: Using AWS Console

1. In CloudFormation console, click **Create stack** → **With new resources**
2. Select **Upload a template file**
3. Click **Choose file** and select your `vpc-ec2-stack.yaml`
4. Click **Next**
5. Enter Stack name: `lab-vpc-ec2-stack`
6. Click **Next** through the configure options
7. Acknowledge any IAM capabilities if prompted
8. Click **Submit**

#### Option B: Using AWS CLI (Terminal)

```bash
# Create the stack
aws cloudformation create-stack \
  --stack-name lab-vpc-ec2-stack \
  --template-body file://vpc-ec2-stack.yaml \
  --region us-west-2

# Monitor stack creation
aws cloudformation describe-stacks \
  --stack-name lab-vpc-ec2-stack \
  --query 'Stacks[0].StackStatus'

# Watch events
aws cloudformation describe-stack-events \
  --stack-name lab-vpc-ec2-stack \
  --max-items 10
```

### Step 5: Verify Stack Creation

1. Monitor the **Events** tab for progress
2. Watch for the status to change to **CREATE_COMPLETE**
3. If errors occur, check the **Events** tab for specific error messages
4. Review the **Resources** tab to confirm all components were created

### Step 6: Troubleshooting Common Issues

#### Stack Creation Fails

- **Check the Events tab** for specific error messages
- **Verify CIDR blocks** don't overlap with existing resources
- **Confirm instance type availability** in your region
- **Review IAM permissions** if access denied errors occur

#### Template Validation Errors

```bash
# Validate your template before deployment
aws cloudformation validate-template \
  --template-body file://vpc-ec2-stack.yaml
```

### Step 7: Iterate and Improve

1. If the stack fails, delete it:
   ```bash
   aws cloudformation delete-stack --stack-name lab-vpc-ec2-stack
   ```
2. Review error messages and update your template
3. Redeploy and test again
4. Repeat until successful

### Step 8: Verify All Components

Once the stack is created successfully, verify:

- ✅ VPC exists with correct CIDR block
- ✅ Internet Gateway is attached to VPC
- ✅ Private Subnet is created within VPC
- ✅ Security Group allows SSH (port 22) from anywhere
- ✅ EC2 T3.micro instance is running in the private subnet

You can verify using AWS CLI:

```bash
# Check VPC
aws ec2 describe-vpcs --filters "Name=tag:Name,Values=Lab-VPC"

# Check EC2 instance
aws ec2 describe-instances --filters "Name=tag:Name,Values=Lab-EC2-Instance"

# Check Security Group
aws ec2 describe-security-groups --filters "Name=tag:Name,Values=Lab-SSH-SG"
```

### Step 9: Notify Instructor

Once your CloudFormation stack builds without errors:
1. Take a screenshot of the **CREATE_COMPLETE** status
2. Review the **Resources** tab to show all components
3. Notify your instructor for review

## Additional Resources

- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/)
- [CloudFormation Template Reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-reference.html)
- [VPC and Subnet Sizing](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html)

## Clean Up

To avoid charges, delete the stack when done:

```bash
aws cloudformation delete-stack --stack-name lab-vpc-ec2-stack
```

Or use the AWS Console:
1. Select your stack
2. Click **Delete**
3. Confirm deletion

## Lab Completion Checklist

- [ ] CloudFormation template created
- [ ] Stack deployed without errors
- [ ] All 5 required components present
- [ ] Stack status shows CREATE_COMPLETE
- [ ] Instructor notified for review

---

**Good luck with your lab!** 🚀