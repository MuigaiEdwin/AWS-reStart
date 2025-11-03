# Amazon Aurora RDS - Hands-On Lab

![AWS](https://img.shields.io/badge/AWS-RDS%20Aurora-orange?style=flat-square&logo=amazon-aws)
![MySQL](https://img.shields.io/badge/MySQL-Compatible-blue?style=flat-square&logo=mysql)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)

## 📋 Overview

This repository documents my hands-on learning experience with Amazon Aurora, a fully managed MySQL-compatible relational database service. The lab focused on creating, configuring, and querying an Aurora database cluster.

**Lab Duration:** ~40 minutes  
**Date Completed:** October 27, 2025

---

## 🎯 Learning Objectives

- [x] Create and configure an Aurora MySQL database cluster
- [x] Connect EC2 instance to Aurora database
- [x] Perform database operations using MySQL client
- [x] Understand Aurora endpoint types and their uses
- [x] Implement proper security configurations

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                    VPC                          │
│  ┌──────────────────┐      ┌─────────────────┐ │
│  │   EC2 Instance   │─────▶│  Aurora Cluster │ │
│  │  (Command Host)  │      │  (MySQL 8.0)    │ │
│  │                  │      │                 │ │
│  │  - MariaDB CLI   │      │  - Writer Node  │ │
│  │  - Session Mgr   │      │  - Port 3306    │ │
│  └──────────────────┘      └─────────────────┘ │
│         │                          │            │
│         │                          │            │
│  ┌──────▼──────────┐      ┌───────▼─────────┐  │
│  │ Security Group  │      │  DB Subnet Grp  │  │
│  │  (EC2 access)   │      │  (Private)      │  │
│  └─────────────────┘      └─────────────────┘  │
└─────────────────────────────────────────────────┘
```

---

## 🔧 Setup & Configuration

### 1. Aurora Database Creation

**Database Configuration:**
```yaml
Engine: Aurora MySQL 8.0
Instance Class: db.t3.medium
Cluster Identifier: aurora
Master Username: admin
Deployment: Single-AZ (Dev/Test)
```

**Network Configuration:**
```yaml
VPC: LabVPC
Subnet Group: dbsubnetgroup
Public Access: No
Security Group: DBSecurityGroup
```

**Additional Settings:**
```yaml
Initial Database: world
Enhanced Monitoring: Disabled
Encryption: Disabled (lab only)
Auto Minor Version Upgrade: Disabled
```

### 2. EC2 Instance Setup

**Install MariaDB Client:**
```bash
sudo yum install mariadb -y
```

**Connect to Aurora:**
```bash
# Replace <endpoint> with your Aurora cluster endpoint
mysql -u admin --password='admin123' -h <endpoint>
```

**Example endpoint format:**
```
aurora.cluster-cabcdefghijklm.us-west-2.rds.amazonaws.com
```

---

## 💾 Database Operations

### Connect to Database
```sql
-- Show available databases
SHOW DATABASES;

-- Switch to world database
USE world;
```

### Create Table
```sql
CREATE TABLE `country` (
  `Code` CHAR(3) NOT NULL DEFAULT '',
  `Name` CHAR(52) NOT NULL DEFAULT '',
  `Continent` ENUM('Asia','Europe','North America','Africa','Oceania','Antarctica','South America') NOT NULL DEFAULT 'Asia',
  `Region` CHAR(26) NOT NULL DEFAULT '',
  `SurfaceArea` FLOAT(10,2) NOT NULL DEFAULT '0.00',
  `IndepYear` SMALLINT(6) DEFAULT NULL,
  `Population` INT(11) NOT NULL DEFAULT '0',
  `LifeExpectancy` FLOAT(3,1) DEFAULT NULL,
  `GNP` FLOAT(10,2) DEFAULT NULL,
  `GNPOld` FLOAT(10,2) DEFAULT NULL,
  `LocalName` CHAR(45) NOT NULL DEFAULT '',
  `GovernmentForm` CHAR(45) NOT NULL DEFAULT '',
  `Capital` INT(11) DEFAULT NULL,
  `Code2` CHAR(2) NOT NULL DEFAULT '',
  PRIMARY KEY (`Code`)
);
```

### Insert Sample Data
```sql
INSERT INTO `country` VALUES 
('GAB','Gabon','Africa','Central Africa',267668.00,1960,1226000,50.1,5493.00,5279.00,'Le Gabon','Republic',902,'GA');

INSERT INTO `country` VALUES 
('IRL','Ireland','Europe','British Islands',70273.00,1921,3775100,76.8,75921.00,73132.00,'Ireland/Éire','Republic',1447,'IE');

INSERT INTO `country` VALUES 
('THA','Thailand','Asia','Southeast Asia',513115.00,1350,61399000,68.6,116416.00,153907.00,'Prathet Thai','Constitutional Monarchy',3320,'TH');

INSERT INTO `country` VALUES 
('CRI','Costa Rica','North America','Central America',51100.00,1821,4023000,75.8,10226.00,9757.00,'Costa Rica','Republic',584,'CR');

INSERT INTO `country` VALUES 
('AUS','Australia','Oceania','Australia and New Zealand',7741220.00,1901,18886000,79.8,351182.00,392911.00,'Australia','Constitutional Monarchy, Federation',135,'AU');
```

### Query Data
```sql
-- Find countries with GNP > 35000 and Population > 10 million
SELECT * FROM country 
WHERE GNP > 35000 AND Population > 10000000;
```

**Expected Results:**
| Code | Name      | Continent | Population | GNP       |
|------|-----------|-----------|------------|-----------|
| AUS  | Australia | Oceania   | 18886000   | 351182.00 |
| THA  | Thailand  | Asia      | 61399000   | 116416.00 |

---

## 📚 Key Concepts Learned

### Aurora Endpoint Types

#### 🔵 Cluster Endpoint (Writer)
- **Purpose:** All write operations (INSERT, UPDATE, DELETE, DDL)
- **Target:** Primary DB instance
- **Failover:** Automatic failover to new primary
- **Format:** `cluster-name.cluster-xxxxx.region.rds.amazonaws.com:3306`

#### 🔵 Reader Endpoint
- **Purpose:** Read-only operations (SELECT queries)
- **Target:** Load-balanced across Aurora replicas
- **Failover:** Automatically routes to available replicas
- **Format:** `cluster-name.cluster-ro-xxxxx.region.rds.amazonaws.com:3306`

### MySQL Client Connection Switches

```bash
mysql [OPTIONS]

-u, --user          MySQL username
-p, --password      MySQL password (use quotes for special chars)
-h, --host          Database host endpoint
-P, --port          Port number (default: 3306)
-D, --database      Database name to use
```

### Security Best Practices

✅ **Implemented:**
- Private subnet placement (no public access)
- Security groups restricting access
- Separate DB subnet group
- VPC isolation

⚠️ **For Production:**
- Enable encryption at rest
- Enable enhanced monitoring
- Use Multi-AZ deployment
- Enable automated backups
- Use IAM database authentication
- Implement least privilege access

---

## 🛠️ Technologies Used

| Service/Tool | Purpose |
|--------------|---------|
| **Amazon RDS Aurora** | Managed MySQL-compatible database |
| **Amazon EC2** | Command host for database access |
| **AWS Systems Manager** | Session Manager for secure SSH |
| **MariaDB Client** | MySQL command-line interface |
| **Amazon VPC** | Network isolation and security |
| **AWS CloudFormation** | Infrastructure provisioning |

---

## 📊 Skills Demonstrated

### AWS Services
- ✅ RDS Aurora cluster provisioning
- ✅ VPC and subnet configuration
- ✅ Security group management
- ✅ EC2 instance connectivity
- ✅ Session Manager usage

### Database Skills
- ✅ MySQL database administration
- ✅ DDL (Data Definition Language)
- ✅ DML (Data Manipulation Language)
- ✅ SQL query writing
- ✅ Database connectivity troubleshooting

### DevOps Practices
- ✅ Infrastructure as Code understanding
- ✅ Security best practices
- ✅ Documentation skills
- ✅ Command-line proficiency

---

## 🚀 Next Steps

- [ ] Practice Multi-AZ deployments
- [ ] Implement Aurora read replicas
- [ ] Explore Aurora Serverless v2
- [ ] Test automated backup and restore
- [ ] Learn Aurora performance optimization
- [ ] Practice Aurora Global Database
- [ ] Implement monitoring with CloudWatch
- [ ] Try Aurora MySQL parallel query

---

## 📖 Resources

- [Amazon Aurora Documentation](https://docs.aws.amazon.com/aurora/)
- [RDS Best Practices](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.BestPractices.html)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [AWS VPC Guide](https://docs.aws.amazon.com/vpc/)

---

## 📝 Notes

**Lab Environment Specifics:**
- Single-AZ deployment (not for production)
- Encryption disabled (enable for production)
- Enhanced monitoring disabled (enable for production)
- Auto minor version upgrade disabled

**Important:** This was a hands-on learning lab. Production environments should implement additional security, high availability, and monitoring features.

---

## 👨‍💻 About

This lab is part of my AWS learning journey through the **AWS re/Start Program**. I'm building practical cloud skills with hands-on experience in AWS services.

**Connect with me:**
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)](https://github.com/MuigaiEdwin)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/muigaiedwin/)
[![X (Twitter)](https://img.shields.io/badge/X-Follow-000000?style=for-the-badge&logo=x)](https://x.com/MuigaiEd)


---

**⭐ If you find this helpful, please star this repo!**

---

*Last Updated: October 27, 2025*