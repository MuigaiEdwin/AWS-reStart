# AWS CloudTrail Security Investigation Lab

## Overview

This lab demonstrates how to use AWS CloudTrail for security auditing and incident response. You'll investigate a simulated website hack, analyze CloudTrail logs using multiple methods, and implement security remediation measures.

## Scenario

The Café website has been compromised. As Sofîa, the AWS administrator, you must identify the attacker, determine how they gained access, and secure the environment to prevent future incidents.

## Architecture

![Lab Architecture](/screenshots/cloudtrail.png)

- **Amazon EC2**: Café Web Server hosting the website
- **AWS CloudTrail**: Audit logging and trail creation
- **Amazon S3**: CloudTrail log storage
- **Amazon Athena**: SQL-based log analysis
- **AWS CLI**: Command-line log investigation

## Duration

**Approximately 75 minutes**

## Learning Objectives

By completing this lab, you will be able to:

- Configure and create a CloudTrail trail
- Analyze CloudTrail logs using multiple methods:
  - Linux `grep` utility
  - AWS CLI CloudTrail commands
  - Amazon Athena SQL queries
- Import CloudTrail log data into Athena
- Run SQL queries to filter and analyze log entries
- Identify security breaches and unauthorized access
- Resolve security concerns in AWS accounts and EC2 instances

## Lab Tasks

### Task 1: Initial Setup and Observation
- Modify security group settings
- Observe the normal Café website

### Task 2: Create CloudTrail and Discover the Hack
- Configure CloudTrail with S3 bucket storage
- Enable AWS KMS encryption
- Observe the hacked website (altered images)
- Notice unauthorized security group modifications

### Task 3: Log Analysis with grep and AWS CLI
- Connect to EC2 instance via SSH
- Download CloudTrail logs from S3
- Extract and analyze JSON log files using `grep`
- Filter logs by IP address and event name
- Use AWS CLI `lookup-events` command
- Search for security group modifications

### Task 4: Advanced Analysis with Amazon Athena
- Create Athena table from CloudTrail logs
- Run SQL queries to filter log data
- Identify suspicious security-related events
- **Challenge**: Discover the hacker's identity

### Task 5: Security Remediation
- Remove unauthorized OS users
- Update SSH security configuration
- Delete malicious inbound security group rules
- Restore the website to original state
- Delete compromised IAM users

## Investigation Results

During this lab, you will identify:

- ✅ The AWS IAM user who created the security vulnerability
- ✅ The exact timestamp of the security breach
- ✅ The source IP address of the attack
- ✅ The access method used (console vs programmatic)
- ✅ Evidence of OS-level compromise

## Key Security Findings

The investigation reveals multiple security issues:

1. **Security Group Misconfiguration**: SSH (port 22) opened to `0.0.0.0/0`
2. **Unauthorized IAM User**: The `chaos` user performed malicious actions
3. **OS User Compromise**: Unauthorized `chaos-user` OS account created
4. **SSH Configuration Weakness**: Password authentication enabled
5. **Website Defacement**: Images replaced with inappropriate content

## Technologies Used

- **AWS CloudTrail**: Activity logging and auditing
- **Amazon EC2**: Web server hosting
- **Amazon S3**: Log file storage
- **Amazon Athena**: Interactive query service
- **AWS CLI**: Command-line interface
- **AWS IAM**: Identity and access management
- **Linux Commands**: `grep`, `cat`, `gunzip`, `aureport`, `vi`
- **SSH**: Secure remote access

## Prerequisites

- Basic understanding of AWS services
- Familiarity with Linux command line
- Basic SQL knowledge for Athena queries
- Understanding of JSON format
- SSH client (PuTTY for Windows or terminal for macOS/Linux)

## Key Commands

### Download CloudTrail Logs
```bash
aws s3 cp s3://<monitoring-bucket>/ . --recursive
gunzip *.gz
```

### Analyze Logs with grep
```bash
# Filter by source IP
for i in $(ls); do echo $i && cat $i | python -m json.tool | grep sourceIPAddress ; done

# Filter by event name
for i in $(ls); do echo $i && cat $i | python -m json.tool | grep eventName ; done
```

### AWS CLI CloudTrail Commands
```bash
# Lookup security group events
aws cloudtrail lookup-events --lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::EC2::SecurityGroup --output text
```

### Athena SQL Queries
```sql
-- Basic query
SELECT useridentity.userName, eventtime, eventsource, eventname, requestparameters
FROM cloudtrail_logs_monitoring####
LIMIT 30;

-- Filter security-related events
SELECT DISTINCT useridentity.userName, eventName, eventSource 
FROM cloudtrail_logs_monitoring#### 
WHERE from_iso8601_timestamp(eventtime) > date_add('day', -1, now()) 
ORDER BY eventSource;
```

### Security Remediation Commands
```bash
# Check authentication logs
sudo aureport --auth

# Remove unauthorized user
sudo userdel -r chaos-user

# Edit SSH configuration
sudo vi /etc/ssh/sshd_config

# Restart SSH service
sudo service sshd restart

# Restore website files
sudo mv Coffee-and-Pastries.backup Coffee-and-Pastries.jpg
```

## Security Best Practices Demonstrated

1. **Enable CloudTrail**: Always maintain audit logging
2. **Restrict SSH Access**: Limit to specific IP addresses
3. **Disable Password Authentication**: Use key-based SSH only
4. **Regular Security Audits**: Review CloudTrail logs periodically
5. **Principle of Least Privilege**: Remove unnecessary IAM users
6. **Security Group Hygiene**: Regularly review inbound rules
7. **Incident Response**: Document and follow remediation procedures

## Important Notes

- CloudTrail logs are delivered to S3 every 5 minutes
- Browser caching may require hard refresh (Shift + Refresh) to see changes
- The trail name must be exactly "monitor" for the lab to work
- Always use `Shift + Refresh` to bypass browser cache when checking the website

## Files and Resources

- **S3 Bucket**: `monitoring####` (CloudTrail logs storage)
- **KMS Key**: Custom encryption key for log files
- **Log Format**: JSON with standard CloudTrail structure
- **EC2 Instance**: Café Web Server with security group
- **SSH Key**: `labsuser.pem` (macOS/Linux) or `labsuser.ppk` (Windows)

## Troubleshooting

**Issue**: No logs downloaded from S3
- **Solution**: Wait at least 5 minutes after creating the trail

**Issue**: Website shows old cached images
- **Solution**: Use Shift + Refresh to bypass browser cache

**Issue**: SSH connection fails
- **Solution**: Verify security group allows SSH from your IP address

**Issue**: Athena query fails
- **Solution**: Ensure query results location is configured in S3

## Business Value

This lab demonstrates how CloudTrail provides:

- **Accountability**: Track who did what and when
- **Security Compliance**: Meet audit and regulatory requirements
- **Incident Response**: Investigate security breaches effectively
- **Change Management**: Monitor infrastructure modifications
- **Forensic Analysis**: Detailed activity logs for investigation

## Outcome

By completing this lab, you will have:

- ✅ Successfully identified the security breach perpetrator
- ✅ Removed unauthorized access at both AWS and OS levels
- ✅ Restored the website to its original state
- ✅ Implemented security hardening measures
- ✅ Gained hands-on experience with CloudTrail log analysis

## Additional Resources

- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/cloudtrail/)
- [CloudTrail Event Reference](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference.html)
- [Athena for CloudTrail](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html)
- [AWS CloudTrail Partners](https://aws.amazon.com/cloudtrail/partners/)

## License

This lab is provided for educational purposes as part of AWS training curriculum.

---

**Note**: This is a simulated security incident in a controlled lab environment. Always follow proper incident response procedures in production environments.