# AWS Lab: Managing Resources with Tagging

A hands-on lab demonstrating how to use AWS CLI and SDK to manage EC2 instances through resource tagging strategies.

## Overview

This lab teaches essential AWS resource management techniques using tags to organize, control, and automate EC2 instance operations. You'll learn to query resources by tags, batch update tag values, and implement automated stop/start and termination policies based on tagging compliance.

## Learning Objectives

- Apply tags to existing AWS resources
- Find and filter resources based on tags using AWS CLI
- Use AWS CLI and AWS SDK for PHP to stop and terminate EC2 instances based on resource attributes
- Implement tag-based automation for resource management
- Build tag compliance policies ("tag-or-terminate")

## Duration

Approximately 45 minutes

## Lab Architecture

![Lab Dashboard Screenshot](/screenshots/Tagging.png)
The lab environment includes:

- **VPC**: Lab VPC with public and private subnets
- **Command Host**: Amazon Linux EC2 instance with pre-configured AWS CLI
- **8 EC2 Instances**: Tagged with custom metadata

### Tag Structure

All private instances use three custom tags:

| Tag Name | Description | Values |
|----------|-------------|--------|
| `Project` | Project assignment | `ERPSystem`, `Experiment1` |
| `Version` | Project version | `1.0` (initially) |
| `Environment` | Deployment stage | `development`, `staging`, `production` |

## Prerequisites

- AWS account access
- Basic familiarity with:
  - AWS EC2
  - Linux command line
  - SSH connections

## Lab Tasks

### Task 1: Using Tags to Manage Resources

Learn to query and filter EC2 instances using AWS CLI:

- Connect to the Command Host via SSH
- Use `aws ec2 describe-instances` with tag filters
- Master JMESPath query syntax for formatted output
- Batch update tags using shell scripts

**Key Skills**: AWS CLI filtering, JMESPath queries, tag management

### Task 2: Stop and Start Resources by Tag

Automate instance lifecycle management:

- Use the `stopinator.php` script to control instances
- Stop all development environment instances
- Restart instances based on tag criteria
- Verify operations in EC2 console

**Key Skills**: Automation scripting, AWS SDK for PHP, resource scheduling

### Task 3: Challenge - Terminate Non-Compliant Instances

Implement a "tag-or-terminate" security policy:

- Identify instances missing required tags
- Automatically terminate non-compliant resources
- Use the `terminate-instances.php` script
- Build enforcement automation

**Key Skills**: Compliance automation, security policies, AWS SDK

## Key Commands

### Query instances by project tag
```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem"
```

### Query with formatted output
```bash
aws ec2 describe-instances \
  --filter "Name=tag:Project,Values=ERPSystem" \
  --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}'
```

### Filter by multiple tags
```bash
aws ec2 describe-instances \
  --filter "Name=tag:Project,Values=ERPSystem" \
           "Name=tag:Environment,Values=development" \
  --query 'Reservations[*].Instances[*].{ID:InstanceId,Environment:Tags[?Key==`Environment`]|[0].Value}'
```

### Stop instances by tag
```bash
./stopinator.php -t"Project=ERPSystem;Environment=development"
```

### Start instances by tag
```bash
./stopinator.php -t"Project=ERPSystem;Environment=development" -s
```

### Terminate non-compliant instances
```bash
./terminate-instances.php -region <region> -subnetid <subnet-id>
```

## Scripts Included

### `change-resource-tags.sh`
Batch updates version tags for development instances in the ERPSystem project.

### `stopinator.php`
Stops or starts EC2 instances based on tag criteria across all AWS regions.

**Arguments:**
- `-t`: Tags in format `name=value;name=value`
- `-s`: Start instances (without this flag, instances are stopped)

### `terminate-instances.php`
Identifies and terminates instances missing required tags within a specified subnet.

**Arguments:**
- `-region`: AWS region
- `-subnetid`: Subnet ID to check for compliance

## JMESPath Query Examples

### Extract specific tag value
```
Tags[?Key==`Project`] | [0].Value
```

### Multiple properties with aliases
```
{ID:InstanceId, AZ:Placement.AvailabilityZone, Project:Tags[?Key==`Project`]|[0].Value}
```

## Best Practices Demonstrated

1. **Consistent Tagging Strategy**: Use standardized tag names across resources
2. **Automation**: Leverage scripts for repetitive tagging operations
3. **Compliance Enforcement**: Implement automated checks for tagging policies
4. **Cost Management**: Use tags to control resource lifecycles (stop/start schedules)
5. **Query Optimization**: Use filters and queries to efficiently find resources

## Use Cases

- **Development Environment Management**: Automatically stop dev instances after hours
- **Cost Optimization**: Schedule instance shutdowns based on environment tags
- **Security Compliance**: Enforce tagging requirements for visibility and governance
- **Resource Organization**: Group and manage resources by project, team, or purpose
- **Automated Cleanup**: Remove non-compliant or untagged resources

## Security Considerations

- The lab implements a "tag-or-terminate" policy for compliance
- Missing required tags triggers automatic instance termination
- Always verify tag values before running termination scripts in production
- Use IAM policies to control who can modify or remove tags

## Troubleshooting

**Issue**: Cannot connect to Command Host
- Verify security group allows SSH (port 22)
- Check that you're using the correct key pair
- Confirm the instance is in a running state

**Issue**: AWS CLI commands fail
- Ensure IAM role is attached to Command Host
- Verify you're in the correct AWS region
- Check command syntax and filter formatting

**Issue**: Scripts don't affect instances
- Verify tag names match exactly (case-sensitive)
- Check that instances are in the expected state
- Confirm you have necessary permissions

## Additional Resources

- [AWS Tagging Best Practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/)
- [JMESPath Tutorial](https://jmespath.org/tutorial.html)
- [AWS SDK for PHP Documentation](https://docs.aws.amazon.com/sdk-for-php/)

## License

This lab is provided for educational purposes.

## Support

For questions or issues with this lab, please consult the AWS documentation or contact your lab administrator.