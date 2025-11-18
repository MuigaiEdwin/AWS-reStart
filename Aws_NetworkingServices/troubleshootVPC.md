# VPC Troubleshooting Lab

A comprehensive hands-on lab for troubleshooting AWS Virtual Private Cloud (VPC) configurations and analyzing VPC Flow Logs.

## Overview

This lab provides practical experience in diagnosing and resolving common VPC networking issues. You'll work with a multi-VPC environment containing EC2 instances and various networking components while learning to capture and analyze network traffic data.

## Lab Architecture

The environment includes:
- Two VPCs with associated networking components
- Amazon EC2 instances (web server and CLI host)
- VPC Flow Logs integration with Amazon S3
- Network ACLs and Security Groups
- Internet Gateway and Route Tables

## Learning Objectives

By completing this lab, you will be able to:

- Create and configure VPC Flow Logs
- Troubleshoot VPC configuration issues systematically
- Analyze network traffic using flow log data
- Use AWS CLI for network diagnostics
- Resolve security group and network ACL misconfigurations
- Query and interpret VPC Flow Log files

## Prerequisites

- AWS account with appropriate permissions
- Basic understanding of VPC concepts
- Familiarity with AWS CLI
- Knowledge of networking fundamentals (TCP/IP, routing, firewalls)

## Lab Duration

Approximately **75 minutes**

## Key Tasks

### Task 1: Connect to CLI Host Instance
- Connect using EC2 Instance Connect
- Configure AWS CLI with appropriate credentials
- Set up terminal environment for troubleshooting

### Task 2: Create VPC Flow Logs
- Create S3 bucket for flow log storage
- Identify VPC resources using AWS CLI
- Configure flow logs to capture all IP traffic
- Verify flow log activation

### Task 3: Troubleshoot VPC Configuration Issues

#### Challenge #1: Web Server Access
**Problem:** Web server page fails to load

**Investigation areas:**
- Port connectivity using `nmap`
- Security group configurations
- Route table settings
- Internet Gateway attachment

**AWS CLI commands used:**
```bash
aws ec2 describe-instances
aws ec2 describe-security-groups
aws ec2 describe-route-tables
aws ec2 create-route
```

#### Challenge #2: SSH Access
**Problem:** EC2 Instance Connect fails

**Investigation areas:**
- Network ACL rules
- Inbound/outbound traffic permissions
- Port 22 accessibility

**AWS CLI commands used:**
```bash
aws ec2 describe-network-acls
aws ec2 delete-network-acl-entry
```

### Task 4: Analyze Flow Logs

**Activities:**
- Download flow logs from S3
- Extract compressed log files
- Query logs using `grep` commands
- Filter for REJECT actions
- Identify failed connection attempts
- Convert Unix timestamps to readable format

**Sample commands:**
```bash
# Download logs
aws s3 cp s3://flowlog######/ . --recursive

# Extract logs
gunzip *.gz

# Search for rejected traffic
grep -rn REJECT .

# Filter by port and IP
grep -rn 22 . | grep REJECT | grep <ip-address>

# Convert timestamp
date -d @<timestamp>
```

## Tools and Services Used

- **AWS CLI** - Primary troubleshooting interface
- **EC2 Instance Connect** - Secure instance access
- **VPC Flow Logs** - Network traffic capture
- **Amazon S3** - Flow log storage
- **nmap** - Port scanning utility
- **grep** - Log file analysis
- **Amazon Athena** - Advanced log querying (optional)

## Key Concepts Covered

### Networking Components
- Virtual Private Clouds (VPCs)
- Subnets (Public/Private)
- Internet Gateways
- Route Tables
- Security Groups
- Network ACLs

### Troubleshooting Techniques
- Systematic isolation of network issues
- Layer-by-layer debugging approach
- Log analysis and correlation
- CLI-based diagnostics

### Security Best Practices
- Principle of least privilege
- Proper security group configuration
- Network ACL rule management
- Flow log monitoring

## Common Issues and Solutions

| Issue | Symptoms | Resolution |
|-------|----------|------------|
| Missing route to IGW | Cannot reach internet | Add 0.0.0.0/0 route to Internet Gateway |
| Restrictive security group | Connection timeout | Add inbound rules for required ports |
| Network ACL blocking traffic | REJECT in flow logs | Remove or modify deny rules |
| Closed ports | nmap shows filtered ports | Update security group rules |

## Success Criteria

✅ Web server page loads successfully  
✅ SSH connection via EC2 Instance Connect works  
✅ Flow logs captured and downloadable  
✅ Log analysis reveals connection attempts  
✅ Understanding of VPC troubleshooting methodology

## Advanced Topics

For further exploration:
- Using Amazon Athena for SQL-based log queries
- Setting up CloudWatch metrics from flow logs
- Automating network diagnostics with Lambda
- VPC Traffic Mirroring for deep packet inspection

## Cleanup

After completing the lab:
1. Delete the S3 bucket containing flow logs
2. Remove flow log configurations
3. Terminate EC2 instances if manually created
4. Delete custom VPC resources if applicable

## Additional Resources

- [AWS VPC Documentation](https://docs.aws.amazon.com/vpc/)
- [VPC Flow Logs User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [Querying VPC Flow Logs with Athena](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs.html)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/)

## Repository Structure

```
.
├── README.md
├── lab-guide.md
├── scripts/
│   └── setup-cli.sh
└── examples/
    ├── flow-log-queries.txt
    └── troubleshooting-checklist.md
```

## Contributing

Contributions to improve this lab guide are welcome! Please submit pull requests or open issues for suggestions.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Note:** This lab is designed for educational purposes. Always follow AWS best practices and security guidelines in production environments.