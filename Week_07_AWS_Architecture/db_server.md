# AWS RDS Lab - Complete Implementation Guide

## Lab Overview
This lab demonstrates creating and managing an Amazon RDS database instance, connecting from an EC2 instance, and performing SQL operations.

## Prerequisites
- AWS Account with lab access
- SSH client (Terminal for macOS/Linux, PuTTY for Windows)
- Downloaded PEM/PPK key file

---

## Part 1: Create RDS Instance

### Step 1: Navigate to RDS Service
1. Open AWS Management Console
2. Search for "RDS" in the services search bar
3. Click on "RDS" to open the RDS Dashboard

### Step 2: Create Database
1. Click **Create database**
2. Configure the following settings:

**Engine Options:**
- Choose: **MySQL** (or Amazon Aurora Provisioned)
- Version: Latest stable version

**Templates:**
- Select: **Free tier** (or Dev/Test)

**Settings:**
- DB instance identifier: `lab-database` (or your choice)
- Master username: `admin`
- Master password: `YourPassword123!` (choose a strong password)
- Confirm password

**DB Instance Configuration:**
- DB instance class: **Burstable classes (db.t3.micro)**

**Storage:**
- Storage type: **General Purpose SSD (gp2)**
- Allocated storage: **20 GB** (max 100 GB allowed)
- Uncheck "Enable storage autoscaling"

**Connectivity:**
- Virtual private cloud (VPC): **Lab VPC**
- Public access: **Yes** (to allow connection)
- VPC security group: **Create new** or select existing that allows port 3306
  - Security group name: `rds-mysql-sg`
  - Ensure inbound rule: Type: MySQL/Aurora, Port: 3306, Source: Security group of LinuxServer

**Additional Configuration:**
- Initial database name: `labdb`
- Backup retention: 1 day
- Enhanced monitoring: **Disable** (for MySQL)
- Delete protection: Uncheck

3. Click **Create database**
4. Wait 5-10 minutes for the database to be available

**Note down:**
- Endpoint: `lab-database.xxxxxxxxxx.us-east-1.rds.amazonaws.com`
- Port: `3306`
- Master username: `admin`
- Password: (what you set)

---

## Part 2: Connect to Linux Server

### Step 1: Get Connection Details
1. Click **Details** → **Show** in lab interface
2. Download PEM key (Linux/macOS) or PPK key (Windows)
3. Note the **LinuxServer** public IP address

### Step 2: SSH Connection

**For Linux/macOS:**
```bash
# Set correct permissions for PEM file
chmod 400 labsuser.pem

# Connect to the instance
ssh -i labsuser.pem ec2-user@<LinuxServer-IP>
```

**For Windows (using PuTTY):**
1. Open PuTTY
2. Host Name: `ec2-user@<LinuxServer-IP>`
3. Connection → SSH → Auth → Browse for PPK file
4. Click Open

---

## Part 3: Install MySQL Client and Connect

### Step 1: Install MySQL Client
```bash
# Update package manager
sudo yum update -y

# Install MySQL client
sudo yum install mysql -y

# Verify installation
mysql --version
```

### Step 2: Connect to RDS Instance
```bash
# Connect to your RDS database
mysql -h <your-rds-endpoint> -P 3306 -u admin -p

# When prompted, enter your master password
# You should see: mysql>
```

**Example:**
```bash
mysql -h lab-database.xxxxxxxxxx.us-east-1.rds.amazonaws.com -P 3306 -u admin -p
```

---

## Part 4: Create and Populate Tables

### Step 1: Create RESTART Table
```sql
-- Create the RESTART table
CREATE TABLE RESTART (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    RestartCity VARCHAR(50) NOT NULL,
    GraduationDate DATETIME NOT NULL
);

-- Verify table creation
DESCRIBE RESTART;
```

**📸 SCREENSHOT 1: Capture the DESCRIBE RESTART output**

### Step 2: Insert 10 Rows into RESTART
```sql
-- Insert 10 sample rows
INSERT INTO RESTART (StudentID, StudentName, RestartCity, GraduationDate) VALUES
(1, 'John Smith', 'New York', '2024-12-15 10:00:00'),
(2, 'Sarah Johnson', 'San Francisco', '2024-11-20 14:30:00'),
(3, 'Michael Brown', 'Chicago', '2025-01-10 09:00:00'),
(4, 'Emily Davis', 'Seattle', '2024-12-05 11:00:00'),
(5, 'David Wilson', 'Boston', '2025-02-14 13:00:00'),
(6, 'Jessica Martinez', 'Austin', '2024-11-30 15:30:00'),
(7, 'Daniel Anderson', 'Denver', '2025-01-20 10:30:00'),
(8, 'Ashley Taylor', 'Miami', '2024-12-28 12:00:00'),
(9, 'Christopher Thomas', 'Portland', '2025-03-05 14:00:00'),
(10, 'Amanda White', 'Atlanta', '2025-01-15 09:30:00');
```

**📸 SCREENSHOT 2: Capture the INSERT confirmation**

### Step 3: Select All Rows from RESTART
```sql
-- Select all rows
SELECT * FROM RESTART;
```

**📸 SCREENSHOT 3: Capture the SELECT output showing all 10 rows**

### Step 4: Create CLOUD_PRACTITIONER Table
```sql
-- Create the CLOUD_PRACTITIONER table
CREATE TABLE CLOUD_PRACTITIONER (
    StudentID INT PRIMARY KEY,
    CertificationDate DATETIME NOT NULL,
    FOREIGN KEY (StudentID) REFERENCES RESTART(StudentID)
);

-- Verify table creation
DESCRIBE CLOUD_PRACTITIONER;
```

**📸 SCREENSHOT 4: Capture the DESCRIBE CLOUD_PRACTITIONER output**

### Step 5: Insert 5 Rows into CLOUD_PRACTITIONER
```sql
-- Insert 5 sample rows (using existing StudentIDs from RESTART table)
INSERT INTO CLOUD_PRACTITIONER (StudentID, CertificationDate) VALUES
(1, '2024-10-15 10:00:00'),
(3, '2024-09-22 14:00:00'),
(5, '2024-11-10 11:30:00'),
(7, '2024-10-30 09:00:00'),
(9, '2024-11-25 13:00:00');
```

**📸 SCREENSHOT 5: Capture the INSERT confirmation**

### Step 6: Select All Rows from CLOUD_PRACTITIONER
```sql
-- Select all rows
SELECT * FROM CLOUD_PRACTITIONER;
```

**📸 SCREENSHOT 6: Capture the SELECT output showing all 5 rows**

### Step 7: Perform INNER JOIN
```sql
-- Inner join between RESTART and CLOUD_PRACTITIONER tables
SELECT 
    r.StudentID,
    r.StudentName,
    cp.CertificationDate
FROM 
    RESTART r
INNER JOIN 
    CLOUD_PRACTITIONER cp ON r.StudentID = cp.StudentID
ORDER BY 
    r.StudentID;
```

**📸 SCREENSHOT 7: Capture the INNER JOIN results**

---

## Part 5: Additional Verification Queries

```sql
-- Count total students in RESTART
SELECT COUNT(*) AS TotalStudents FROM RESTART;

-- Count certified students
SELECT COUNT(*) AS CertifiedStudents FROM CLOUD_PRACTITIONER;

-- Find students not yet certified
SELECT StudentID, StudentName 
FROM RESTART 
WHERE StudentID NOT IN (SELECT StudentID FROM CLOUD_PRACTITIONER);
```

---

## Part 6: Cleanup (Optional)

```sql
-- Exit MySQL
EXIT;
```

```bash
# Exit SSH session
exit
```

**In AWS Console:**
1. Navigate to RDS Dashboard
2. Select your database instance
3. Actions → Delete
4. Uncheck "Create final snapshot"
5. Check "I acknowledge..."
6. Type "delete me"
7. Click Delete

---

## GitHub Submission Structure

Create a repository with the following structure:

```
aws-rds-lab/
├── README.md
├── screenshots/
│   ├── 01-restart-table-creation.png
│   ├── 02-restart-insert.png
│   ├── 03-restart-select.png
│   ├── 04-cloud-practitioner-creation.png
│   ├── 05-cloud-practitioner-insert.png
│   ├── 06-cloud-practitioner-select.png
│   └── 07-inner-join.png
├── sql-scripts/
│   ├── 01-create-restart-table.sql
│   ├── 02-insert-restart-data.sql
│   ├── 03-create-cloud-practitioner-table.sql
│   ├── 04-insert-cloud-practitioner-data.sql
│   └── 05-inner-join-query.sql
└── documentation/
    └── lab-notes.md
```

---


## Key Learning Outcomes

✅ Created an Amazon RDS MySQL instance  
✅ Configured VPC and security groups for database access  
✅ Connected to RDS from EC2 instance using MySQL client  
✅ Created relational database tables with proper schemas  
✅ Inserted and queried data using SQL  
✅ Performed INNER JOIN operations across related tables  
✅ Demonstrated understanding of primary and foreign key relationships  

---

## Lab Configuration Summary

| Component | Configuration |
|-----------|--------------|
| **Database Engine** | MySQL 8.0 (or Aurora) |
| **Instance Class** | db.t3.micro |
| **Storage** | 20 GB gp2 |
| **VPC** | Lab VPC |
| **Multi-AZ** | Disabled |
| **Public Access** | Enabled |
| **Port** | 3306 |

---

## Troubleshooting

**Cannot connect to RDS:**
- Verify security group allows inbound traffic on port 3306
- Check RDS endpoint is correct
- Ensure RDS status is "Available"
- Verify VPC settings

**Foreign key constraint fails:**
- Ensure StudentID exists in RESTART table before inserting into CLOUD_PRACTITIONER
- Use StudentIDs 1-10 from the RESTART table

**MySQL client not found:**
```bash
# For Amazon Linux 2
sudo yum install mysql -y

# For Ubuntu
sudo apt-get update
sudo apt-get install mysql-client -y
```

---

## Resources

- [AWS RDS Documentation](https://docs.aws.amazon.com/rds/)
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [SQL JOIN Operations](https://www.w3schools.com/sql/sql_join.asp)

---

## Author
Your Name  
Date: October 29, 2025  
Course: Cloud Computing / AWS Database Management