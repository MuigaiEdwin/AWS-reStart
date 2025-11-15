# Migrating to Amazon RDS - Lab Guide

![AWS](https://img.shields.io/badge/AWS-RDS-orange)
![Database](https://img.shields.io/badge/Database-MariaDB-blue)
![CLI](https://img.shields.io/badge/Tool-AWS_CLI-green)

## Overview

This lab demonstrates how to migrate a café web application from using a local database to a fully managed Amazon RDS (Relational Database Service) instance. The migration process involves building required infrastructure components, transferring data, and reconfiguring the application.

## Architecture

### Starting Architecture
![Lab Dashboard Screenshot](/screenshots/StartingArchitecture.png)
- **Application**: Café web application running on EC2 LAMP stack (Linux, Apache, MySQL, PHP)
- **Database**: Local MariaDB database on the same EC2 instance
- **Instance Type**: T3 small in a public subnet
- **Administration**: CLI Host instance for AWS CLI operations

### Final Architecture
![Lab Dashboard Screenshot](/screenshots/FinalArchitecture.png)
- **Application**: Same café web application on EC2
- **Database**: Amazon RDS MariaDB instance in private subnets
- **High Availability**: Multi-AZ deployment capability
- **Security**: Database isolated in private subnets with security groups

## Learning Objectives

By completing this lab, you will learn to:

1. Create an Amazon RDS MariaDB instance using AWS CLI
2. Migrate data from a local MariaDB database to Amazon RDS
3. Configure VPC networking for RDS (subnets, security groups)
4. Monitor RDS instances using Amazon CloudWatch metrics
5. Update application configuration to use RDS endpoints

## Prerequisites

- Basic knowledge of AWS services (EC2, VPC, RDS)
- Familiarity with Linux command line
- Understanding of MySQL/MariaDB databases
- Basic networking concepts (CIDR, subnets, security groups)

## Lab Duration

Approximately **60 minutes**

## Lab Tasks

### Task 1: Generate Order Data
- Access the café website
- Place multiple orders to populate the database
- Record order count for verification after migration

### Task 2: Create Amazon RDS Instance (AWS CLI)
#### 2.1 Connect to CLI Host
- Use EC2 Instance Connect to access CLI Host instance

#### 2.2 Configure AWS CLI
- Set up AWS credentials and region
- Configure JSON output format

#### 2.3 Create Prerequisite Components
- **Security Group**: `CafeDatabaseSG` (allows MySQL traffic from café instance)
- **Private Subnet 1**: `10.200.2.0/23` (same AZ as café instance)
- **Private Subnet 2**: `10.200.10.0/23` (different AZ)
- **DB Subnet Group**: `CafeDB Subnet Group`

#### 2.4 Create RDS Instance
- **Instance ID**: `CafeDBInstance`
- **Engine**: MariaDB 10.5.13
- **Instance Class**: db.t3.micro
- **Storage**: 20 GB
- **Credentials**: root / Re:Start!9
- **Network**: Private subnets with CafeDatabaseSG

### Task 3: Migrate Application Data
- Connect to CafeInstance via EC2 Instance Connect
- Create database backup using `mysqldump`
- Restore backup to Amazon RDS instance
- Verify data migration success

### Task 4: Configure Application
- Update database endpoint in AWS Systems Manager Parameter Store
- Change `/cafe/dbUrl` parameter to RDS endpoint
- Test website functionality
- Verify order history matches pre-migration data

### Task 5: Monitor RDS Database
- Explore CloudWatch metrics in RDS console
- Monitor key metrics:
  - CPU Utilization
  - Database Connections
  - Free Storage Space
  - Freeable Memory
  - Read/Write IOPS
- Test connection monitoring with interactive SQL session

## Key AWS CLI Commands

```bash
# Create security group
aws ec2 create-security-group \
  --group-name CafeDatabaseSG \
  --description "Security group for Cafe database" \
  --vpc-id <VPC_ID>

# Create private subnet
aws ec2 create-subnet \
  --vpc-id <VPC_ID> \
  --cidr-block 10.200.2.0/23 \
  --availability-zone <AZ>

# Create DB subnet group
aws rds create-db-subnet-group \
  --db-subnet-group-name "CafeDB Subnet Group" \
  --subnet-ids <SUBNET_1> <SUBNET_2>

# Create RDS instance
aws rds create-db-instance \
  --db-instance-identifier CafeDBInstance \
  --engine mariadb \
  --db-instance-class db.t3.micro \
  --allocated-storage 20
```

## Database Migration Commands

```bash
# Backup local database
mysqldump --user=root --password='Re:Start!9' \
  --databases cafe_db --add-drop-database > cafedb-backup.sql

# Restore to RDS
mysql --user=root --password='Re:Start!9' \
  --host=<RDS_ENDPOINT> < cafedb-backup.sql

# Verify migration
mysql --user=root --password='Re:Start!9' \
  --host=<RDS_ENDPOINT> cafe_db
```

## Network Configuration

### CIDR Blocks
- **VPC**: `10.200.0.0/20`
- **Public Subnet 1**: `10.200.0.0/24`
- **Private Subnet 1**: `10.200.2.0/23`
- **Private Subnet 2**: `10.200.10.0/23`

### Security Group Rules
- **CafeDatabaseSG**: Allow TCP 3306 from CafeSecurityGroup

## Best Practices Demonstrated

1. **Infrastructure as Code**: Using AWS CLI for reproducible infrastructure
2. **Security**: Database in private subnets, restricted security group rules
3. **Configuration Management**: Externalized database connection via Parameter Store
4. **High Availability**: Multi-AZ subnet group for RDS deployment
5. **Monitoring**: CloudWatch integration for database performance metrics
6. **Backup Strategy**: Automated daily backups with configurable retention

## CloudWatch Metrics Monitored

- **CPUUtilization**: CPU usage percentage
- **DatabaseConnections**: Active database connections
- **FreeStorageSpace**: Available storage capacity
- **FreeableMemory**: Available RAM
- **WriteIOPS**: Disk write operations per second
- **ReadIOPS**: Disk read operations per second

## Troubleshooting Tips

- Wait for RDS instance status to show `available` before migration
- Ensure security group rules allow MySQL traffic (port 3306)
- Verify RDS endpoint address is correctly updated in Parameter Store
- Check CloudWatch metrics refresh interval (1 minute) when monitoring

## Additional Resources

- [Amazon RDS Documentation](https://docs.aws.amazon.com/rds/)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/)
- [MariaDB Documentation](https://mariadb.org/documentation/)
- [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

## Cleanup

When finished with the lab, ensure you properly terminate resources to avoid unnecessary charges:
- Delete RDS instance
- Remove DB subnet group
- Delete security groups
- Terminate EC2 instances

## License

This lab guide is for educational purposes.

---

**Note**: This is a hands-on lab exercise. Actual implementation requires an AWS account and may incur costs.