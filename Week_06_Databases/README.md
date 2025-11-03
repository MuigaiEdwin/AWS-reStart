# 🗄️ Week 6: Database Operations & AWS RDS

> **Comprehensive Database Management with MySQL and Amazon RDS**

[![AWS](https://img.shields.io/badge/AWS-RDS-FF9900?style=flat&logo=amazon-aws&logoColor=white)](https://aws.amazon.com/rds/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)](https://github.com)

**AWS re/Start Program** | Database Fundamentals & Cloud Architecture  
**Student:** Edwin Muigai  
**Completion Date:** October 2025

---

## 📚 Repository Overview

This repository contains hands-on lab exercises covering **SQL fundamentals** and **AWS RDS deployment**. The labs progress from basic database operations to advanced querying techniques and cloud infrastructure implementation.

### Learning Path

```
Foundation              Intermediate           Advanced              Cloud
    ↓                       ↓                     ↓                    ↓
  DDL Ops    →    DML Ops    →    SELECT    →    Functions    →    RDS Deploy
(Lab 1)          (Lab 2)         (Lab 3-4)       (Lab 5-6)         (Lab 7)
```

---

## 📂 Lab Files

| Lab # | File Name | Topic | Difficulty | Key Concepts |
|-------|-----------|-------|------------|--------------|
| **1** | `database_operations.sql` | DDL Operations | ⭐ Beginner | CREATE, DROP, ALTER, SHOW |
| **2** | `insert_update_delete.sql` | DML Operations | ⭐ Beginner | INSERT, UPDATE, DELETE |
| **3** | `selecting_data.sql` | SELECT Queries | ⭐⭐ Intermediate | SELECT, WHERE, ORDER BY |
| **4** | `conditional_search.sql` | Conditional Logic | ⭐⭐ Intermediate | BETWEEN, LIKE, Wildcards |
| **5** | `working_with_functions.sql` | SQL Functions | ⭐⭐⭐ Advanced | Aggregate, String Functions |
| **6** | `organizing_data.sql` | Data Organization | ⭐⭐⭐ Advanced | GROUP BY, Window Functions |
| **7** | `rds_database_setup.md` | AWS RDS Deployment | ⭐⭐⭐ Advanced | Multi-AZ, High Availability |

---

## 🎯 Skills Demonstrated

### SQL Proficiency

<table>
<tr>
<td width="50%">

**Data Definition Language (DDL)**
- ✅ CREATE databases and tables
- ✅ ALTER table structures
- ✅ DROP databases and tables
- ✅ SHOW database objects
- ✅ Schema design and modification

</td>
<td width="50%">

**Data Manipulation Language (DML)**
- ✅ INSERT records into tables
- ✅ UPDATE existing data
- ✅ DELETE records safely
- ✅ Import data from SQL files
- ✅ Transaction management

</td>
</tr>
<tr>
<td width="50%">

**Data Query Language (DQL)**
- ✅ SELECT with multiple columns
- ✅ WHERE clause filtering
- ✅ ORDER BY sorting (ASC/DESC)
- ✅ Comparison operators (<, >, =)
- ✅ Logical operators (AND, OR)
- ✅ BETWEEN range queries
- ✅ LIKE pattern matching
- ✅ Wildcard characters (%, _)

</td>
<td width="50%">

**Advanced Functions**
- ✅ Aggregate functions (SUM, AVG, COUNT, MIN, MAX)
- ✅ String functions (SUBSTRING_INDEX, LENGTH, TRIM)
- ✅ Window functions (RANK, DENSE_RANK, ROW_NUMBER)
- ✅ GROUP BY aggregation
- ✅ OVER clause with PARTITION BY
- ✅ Running totals and cumulative calculations

</td>
</tr>
</table>

### AWS Cloud Architecture
- ✅ Amazon RDS deployment and configuration
- ✅ Multi-AZ high availability setup
- ✅ VPC networking and security groups
- ✅ Database security best practices
- ✅ Application-database integration

---

## 🚀 Quick Start Guide

### Prerequisites

```bash
# MySQL Server (for local practice)
sudo apt update
sudo apt install mysql-server

# MySQL Client
mysql --version

# AWS CLI (for RDS labs)
aws --version
```

### Running the SQL Labs

#### Option 1: MySQL Command Line

```bash
# Connect to MySQL
mysql -u root -p

# Run individual labs
mysql -u root -p < database_operations.sql
mysql -u root -p < insert_update_delete.sql
mysql -u root -p < selecting_data.sql
# ... and so on
```

#### Option 2: MySQL Workbench

1. Open MySQL Workbench
2. Create connection to your local MySQL server
3. Open any `.sql` file
4. Execute queries (⚡ lightning bolt icon)

#### Option 3: VS Code with MySQL Extension

```bash
# Install MySQL extension
# Connect to your database
# Open .sql files and run queries
```

---

## 📖 Detailed Lab Descriptions

### Lab 1: Database Operations (`database_operations.sql`)
**Foundation of database structure management**

Learn to create and manage database schemas with DDL commands.

```sql
-- Key Operations
CREATE DATABASE world;
CREATE TABLE country (...);
ALTER TABLE country RENAME COLUMN ...;
DROP TABLE city;
SHOW DATABASES;
```

**What You'll Learn:**
- Database and table creation
- Schema modification with ALTER
- Safe deletion practices
- Viewing database objects

---

### Lab 2: Insert, Update, Delete (`insert_update_delete.sql`)
**Data manipulation fundamentals**

Master CRUD operations for managing data within tables.

```sql
-- Key Operations
INSERT INTO country VALUES (...);
UPDATE country SET Population = 0;
DELETE FROM country WHERE ...;
```

**What You'll Learn:**
- Adding records to tables
- Modifying existing data
- Safely removing records
- Bulk data import from SQL files
- Understanding WHERE clauses importance

---

### Lab 3: Selecting Data (`selecting_data.sql`)
**Querying and retrieving information**

Extract meaningful data from databases using SELECT statements.

```sql
-- Key Operations
SELECT Name, Population FROM country;
SELECT * FROM country WHERE Population > 50000000;
SELECT COUNT(*) FROM country;
ORDER BY Population DESC;
```

**What You'll Learn:**
- Basic SELECT queries
- Filtering with WHERE
- Sorting results with ORDER BY
- Counting records
- Column aliases with AS

---

### Lab 4: Conditional Search (`conditional_search.sql`)
**Advanced filtering techniques**

Build complex queries using operators and pattern matching.

```sql
-- Key Operations
WHERE Population BETWEEN 50000000 AND 100000000;
WHERE Region LIKE "%Europe%";
WHERE LOWER(Region) LIKE "%central%";
```

**What You'll Learn:**
- BETWEEN operator for ranges
- LIKE operator with wildcards
- Case-insensitive searching
- Combining multiple conditions

---

### Lab 5: Working with Functions (`working_with_functions.sql`)
**Data transformation and analysis**

Use built-in SQL functions for calculations and string manipulation.

```sql
-- Key Operations
SELECT SUM(Population), AVG(Population) FROM country;
SELECT SUBSTRING_INDEX(Region, " ", 1) FROM country;
SELECT DISTINCT(Region) FROM country;
```

**What You'll Learn:**
- Aggregate functions for statistics
- String manipulation functions
- Removing duplicates with DISTINCT
- Functions in WHERE clauses

---

### Lab 6: Organizing Data (`organizing_data.sql`)
**Advanced data aggregation**

Group and rank data for analytical insights.

```sql
-- Key Operations
SELECT Region, SUM(Population) FROM country GROUP BY Region;
SELECT Name, RANK() OVER(PARTITION BY Region ORDER BY Population DESC);
```

**What You'll Learn:**
- GROUP BY for aggregation
- Window functions (RANK, DENSE_RANK, ROW_NUMBER)
- PARTITION BY for grouped calculations
- Running totals and cumulative sums

---

### Lab 7: AWS RDS Setup (`rds_database_setup.md`)
**Cloud database deployment**

Deploy a production-ready, highly available MySQL database on AWS.

**Architecture Components:**
- Multi-AZ RDS MySQL instance
- VPC with public and private subnets
- Security groups for access control
- Web server integration

**What You'll Learn:**
- Amazon RDS configuration
- High availability with Multi-AZ
- Network security best practices
- Database endpoint management
- Application integration

---

## 💡 Key Concepts Reference

### SQL Command Categories

```
┌─────────────────────────────────────────────────────────┐
│                    SQL Commands                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  DDL (Data Definition)          DML (Data Manipulation) │
│  ├── CREATE                     ├── INSERT              │
│  ├── ALTER                      ├── UPDATE              │
│  ├── DROP                       └── DELETE              │
│  └── TRUNCATE                                           │
│                                                         │
│  DQL (Data Query)               DCL (Data Control)      │
│  ├── SELECT                     ├── GRANT               │
│  ├── WHERE                      └── REVOKE              │
│  ├── ORDER BY                                           │
│  ├── GROUP BY                   TCL (Transaction)       │
│  └── HAVING                     ├── COMMIT              │
│                                 ├── ROLLBACK            │
│                                 └── SAVEPOINT           │
└─────────────────────────────────────────────────────────┘
```

### Common SQL Functions

| Category | Functions | Use Case |
|----------|-----------|----------|
| **Aggregate** | SUM(), AVG(), COUNT(), MIN(), MAX() | Statistical analysis |
| **String** | SUBSTRING(), LENGTH(), TRIM(), CONCAT() | Text manipulation |
| **Window** | RANK(), ROW_NUMBER(), DENSE_RANK() | Ranking and ordering |
| **Date** | NOW(), DATE(), YEAR(), MONTH() | Date operations |
| **Conditional** | IF(), CASE, COALESCE() | Logic operations |

---

## 🎓 Learning Outcomes

By completing these labs, you will:

### Technical Skills
- [x] Write efficient SQL queries for data retrieval
- [x] Design and modify database schemas
- [x] Perform CRUD operations confidently
- [x] Use aggregate and window functions for analysis
- [x] Deploy and manage cloud databases on AWS
- [x] Implement database security best practices

### Professional Competencies
- [x] Database administration fundamentals
- [x] Cloud infrastructure deployment
- [x] Security-first architecture design
- [x] Production-ready configuration
- [x] Documentation and communication
- [x] Problem-solving and troubleshooting

---

## 🔧 Troubleshooting Guide

### Common Issues and Solutions

<details>
<summary><b>MySQL Connection Refused</b></summary>

```bash
# Check if MySQL is running
sudo systemctl status mysql

# Start MySQL service
sudo systemctl start mysql

# Enable on boot
sudo systemctl enable mysql
```
</details>

<details>
<summary><b>Access Denied Error</b></summary>

```bash
# Reset root password
sudo mysql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_password';
FLUSH PRIVILEGES;
EXIT;
```
</details>

<details>
<summary><b>Database Doesn't Exist</b></summary>

```sql
-- Check available databases
SHOW DATABASES;

-- Create the world database
CREATE DATABASE world;
USE world;
```
</details>

<details>
<summary><b>Syntax Errors</b></summary>

- Check for missing semicolons (;)
- Verify column names match exactly
- Ensure proper quote usage (' for strings)
- Check for reserved keyword conflicts
</details>

---

## 📊 Database Schema

### World Database Structure

```sql
world
├── country
│   ├── Code (PK)
│   ├── Name
│   ├── Continent
│   ├── Region
│   ├── SurfaceArea
│   ├── IndepYear
│   ├── Population
│   ├── LifeExpectancy
│   ├── GNP
│   ├── LocalName
│   ├── GovernmentForm
│   ├── HeadOfState
│   └── Capital
├── city
│   ├── ID (PK)
│   ├── Name
│   ├── CountryCode (FK)
│   ├── District
│   └── Population
└── countrylanguage
    ├── CountryCode (FK)
    ├── Language
    ├── IsOfficial
    └── Percentage
```

---

## 🌟 Best Practices Applied

### SQL Coding Standards
```sql
-- ✅ Good: Readable, formatted
SELECT 
    Name,
    Population,
    Region
FROM world.country
WHERE Population > 1000000
ORDER BY Population DESC;

-- ❌ Bad: Hard to read
SELECT Name,Population,Region FROM world.country WHERE Population>1000000 ORDER BY Population DESC;
```

### Security Practices
- ✅ Use parameterized queries to prevent SQL injection
- ✅ Implement least privilege access
- ✅ Store credentials securely (never in code)
- ✅ Use SSL/TLS for database connections
- ✅ Regular backups and disaster recovery plans

### Performance Optimization
- ✅ Use indexes on frequently queried columns
- ✅ Avoid SELECT * in production code
- ✅ Use appropriate data types
- ✅ Limit result sets when possible
- ✅ Monitor query performance

---

## 📚 Additional Resources

### Official Documentation
- [MySQL Documentation](https://dev.mysql.com/doc/)
- [Amazon RDS User Guide](https://docs.aws.amazon.com/rds/)
- [SQL Tutorial](https://www.w3schools.com/sql/)

### Learning Platforms
- [MySQL Tutorial for Beginners](https://www.mysqltutorial.org/)
- [AWS RDS Workshop](https://aws.amazon.com/rds/resources/)
- [SQL Practice Problems](https://leetcode.com/problemset/database/)

### Tools & Extensions
- [MySQL Workbench](https://www.mysql.com/products/workbench/)
- [DBeaver](https://dbeaver.io/) - Universal Database Tool
- [VS Code MySQL Extension](https://marketplace.visualstudio.com/items?itemName=cweijan.vscode-mysql-client2)

---

## 🎯 Next Steps

### Continue Learning
1. **Advanced SQL Topics**
   - Stored procedures and functions
   - Triggers and events
   - Views and materialized views
   - Database optimization

2. **Cloud Databases**
   - Amazon Aurora
   - Read replicas
   - Cross-region replication
   - Backup and recovery strategies

3. **NoSQL Databases**
   - Amazon DynamoDB
   - MongoDB
   - Redis for caching

### Practice Projects
- Build a full-stack application with RDS backend
- Create a data analytics dashboard
- Implement a multi-tenant database architecture
- Design and optimize a high-traffic database

---

## 📝 Lab Completion Checklist

- [ ] Lab 1: Database Operations ✅
- [ ] Lab 2: Insert, Update, Delete ✅
- [ ] Lab 3: Selecting Data ✅
- [ ] Lab 4: Conditional Search ✅
- [ ] Lab 5: Working with Functions ✅
- [ ] Lab 6: Organizing Data ✅
- [ ] Lab 7: AWS RDS Setup ✅

**All labs completed!** 🎉

---

## 🤝 Connect & Feedback

Have questions or suggestions? Feel free to reach out!

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/muigaiedwin/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat&logo=github&logoColor=white)](https://github.com/MuigaiEdwin)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=flat&logo=gmail&logoColor=white)](mailto:muigaiedd@gmail.com)

---

## 📄 License

This project is part of the AWS re/Start program curriculum. All lab materials are for educational purposes.

---

<div align="center">

**Built with ❤️ for learning and growth**

⭐ Star this repo if you found it helpful!

</div>

---

## 📌 Repository Structure

```
Week_06_Databases/
├── README.md (this file)
├── database_operations.sql
├── insert_update_delete.sql
├── selecting_data.sql
├── conditional_search.sql
├── working_with_functions.sql
├── organizing_data.sql
└── rds_database_setup.md
```

---

**Last Updated:** October 2025  
**Version:** 1.0  
**AWS re/Start Program - Week 6 Database Labs**