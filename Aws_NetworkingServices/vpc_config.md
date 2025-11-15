# AWS VPC Configuration Lab

## Overview

This hands-on lab guides you through building a complete Amazon Virtual Private Cloud (VPC) infrastructure from scratch. You'll create a secure, isolated network environment within AWS where you can deploy resources like EC2 instances with full control over networking components.

## Architecture
![Lab Dashboard Screenshot](/screenshots/vpc-architecture.png)
By the end of this lab, you will have built the following architecture:

- **1 VPC** with CIDR block 10.0.0.0/16
- **2 Subnets** (Public and Private) in a single Availability Zone
- **1 Internet Gateway** for public internet access
- **1 NAT Gateway** for private subnet internet access
- **2 Route Tables** (Public and Private)
- **2 EC2 Instances** (Bastion server in public subnet, optional instance in private subnet)

## Learning Objectives

Upon completion of this lab, you will be able to:

- ✅ Create a VPC with custom IPv4 CIDR blocks
- ✅ Configure public and private subnets
- ✅ Set up an Internet Gateway for external connectivity
- ✅ Deploy a NAT Gateway for private subnet internet access
- ✅ Configure route tables for traffic management
- ✅ Launch and configure a bastion host (jump box)
- ✅ Access private instances securely through a bastion server

## Prerequisites

- AWS Account with appropriate permissions
- Basic understanding of networking concepts (IP addresses, CIDR notation, routing)
- Familiarity with the AWS Management Console

## Duration

⏱️ **Approximately 45 minutes**

## Lab Tasks

### Task 1: Creating a VPC
Create a new VPC with:
- Name: `Lab VPC`
- CIDR block: `10.0.0.0/16`
- Enable DNS hostnames

### Task 2: Creating Subnets

#### Public Subnet
- Name: `Public Subnet`
- CIDR: `10.0.0.0/24`
- Auto-assign public IPv4: Enabled

#### Private Subnet
- Name: `Private Subnet`
- CIDR: `10.0.2.0/23`
- Supports IP addresses from 10.0.2.x to 10.0.3.x

### Task 3: Creating an Internet Gateway
- Name: `Lab IGW`
- Attach to Lab VPC

### Task 4: Configuring Route Tables

#### Private Route Table
- Local VPC routing only

#### Public Route Table
- Local VPC routing
- Route to Internet Gateway (0.0.0.0/0 → IGW)
- Associated with Public Subnet

### Task 5: Launching a Bastion Server
Deploy an EC2 instance in the public subnet:
- Instance type: `t3.micro`
- AMI: `Amazon Linux 2023 AMI`
- Security Group: Allow SSH from anywhere
- Access method: EC2 Instance Connect

### Task 6: Creating a NAT Gateway
- Name: `Lab NAT gateway`
- Deploy in Public Subnet
- Allocate Elastic IP
- Configure Private Route Table to route internet traffic (0.0.0.0/0) to NAT Gateway

### Optional Challenge: Testing the Private Subnet

#### Launch Private Instance
- Deploy EC2 instance in Private Subnet
- Security Group: Allow SSH from VPC CIDR (10.0.0.0/16)
- Access via bastion server

#### Test Connectivity
1. Connect to Bastion Server using EC2 Instance Connect
2. SSH from Bastion to Private Instance using private IP
3. Ping external websites to verify NAT Gateway functionality

## Key Networking Concepts

### Public vs Private Subnets
- **Public Subnet**: Has a route to an Internet Gateway, resources can receive public IPs
- **Private Subnet**: No direct internet access, uses NAT Gateway for outbound traffic

### Bastion Host (Jump Box)
A secure EC2 instance in a public subnet that provides access to instances in private subnets. This follows security best practices by limiting direct access to private resources.

### NAT Gateway
Allows instances in private subnets to initiate outbound connections to the internet while preventing inbound connections from the internet.

## Security Best Practices Demonstrated

- ✔️ Separation of public and private resources
- ✔️ Use of bastion host for secure access
- ✔️ Private instances isolated from direct internet access
- ✔️ Security groups with appropriate access controls

## Troubleshooting Tips

| Issue | Solution |
|-------|----------|
| Can't connect to bastion | Verify security group allows SSH, check public IP is assigned |
| Can't reach private instance | Confirm bastion is in public subnet, check security group allows SSH from VPC CIDR |
| Private instance can't reach internet | Verify NAT Gateway is in public subnet and private route table points to it |
| DNS not resolving | Enable DNS hostnames in VPC settings |

## Cleanup (Important!)

To avoid ongoing charges, remember to delete resources in this order:
1. Terminate EC2 instances
2. Delete NAT Gateway (wait for deletion to complete)
3. Release Elastic IP addresses
4. Delete subnets
5. Detach and delete Internet Gateway
6. Delete VPC

## Additional Resources

- [AWS VPC Documentation](https://docs.aws.amazon.com/vpc/)
- [VPC Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)
- [NAT Gateway Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)

## License

This lab is provided for educational purposes.

## Contributing

Feel free to submit issues or pull requests to improve this lab guide.

---

**Lab Status**: ✅ Complete

**Last Updated**: November 2025