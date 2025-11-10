# AWS Lambda Sales Analysis Report System

![AWS](https://img.shields.io/badge/AWS-Lambda-orange)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![License](https://img.shields.io/badge/License-MIT-green)

A serverless sales analysis reporting system built with AWS Lambda that automatically generates and emails daily sales reports by querying a MySQL database.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Components](#components)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)

## 🎯 Overview

This project implements a serverless computing solution using AWS Lambda to generate automated sales analysis reports. The system pulls data from a MySQL database running on an EC2 instance, processes it, and delivers formatted reports via email using Amazon SNS.

### Key Capabilities

- **Automated Scheduling**: Reports generated daily at 8 PM (Monday-Saturday) via CloudWatch Events
- **Serverless Architecture**: No server management required
- **Secure Configuration**: Database credentials stored in AWS Systems Manager Parameter Store
- **Email Notifications**: Automated delivery via Amazon SNS
- **Scalable Design**: Lambda functions with reusable layers

## 🏗️ Architecture

![Lab Dashboard Screenshot](/screenshots/lambda-activity-architecture.png)
### Workflow Steps

1. CloudWatch Events triggers `salesAnalysisReport` function daily
2. Main function invokes `salesAnalysisReportDataExtractor`
3. Data extractor queries the café database
4. Query results returned to main function
5. Report formatted and published to SNS topic
6. SNS sends email to subscribed administrators

## ✨ Features

- **Lambda Layers**: Reusable PyMySQL library layer
- **VPC Integration**: Secure database access within VPC
- **IAM Role Management**: Principle of least privilege
- **CloudWatch Integration**: Comprehensive logging and monitoring
- **Parameter Store**: Secure credential management
- **SNS Integration**: Multi-subscriber email delivery
- **Cron Scheduling**: Flexible scheduling with CloudWatch Events

## 📦 Prerequisites

### AWS Services Required

- AWS Lambda
- Amazon EC2 (LAMP stack)
- Amazon SNS
- AWS Systems Manager (Parameter Store)
- Amazon CloudWatch Events
- AWS IAM
- Amazon VPC

### Tools & Dependencies

- Python 3.9
- AWS CLI
- PyMySQL library
- Access to AWS Management Console

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/aws-lambda-sales-analysis.git
cd aws-lambda-sales-analysis
```

### 2. Set Up Lambda Layer

```bash
# Create Lambda layer from PyMySQL library
cd layers
zip -r pymysql-v3.zip python/
```

### 3. Deploy Lambda Functions

```bash
# Deploy Data Extractor
cd ../functions/data-extractor
zip -r salesAnalysisReportDataExtractor-v3.zip .
aws lambda create-function \
  --function-name salesAnalysisReportDataExtractor \
  --runtime python3.9 \
  --zip-file fileb://salesAnalysisReportDataExtractor-v3.zip \
  --handler salesAnalysisReportDataExtractor.lambda_handler \
  --role arn:aws:iam::ACCOUNT_ID:role/salesAnalysisReportDERole

# Deploy Main Report Function
cd ../sales-analysis
zip -r salesAnalysisReport-v2.zip .
aws lambda create-function \
  --function-name salesAnalysisReport \
  --runtime python3.9 \
  --zip-file fileb://salesAnalysisReport-v2.zip \
  --handler salesAnalysisReport.lambda_handler \
  --role arn:aws:iam::ACCOUNT_ID:role/salesAnalysisReportRole
```

## ⚙️ Configuration

### 1. Parameter Store Setup

Store database credentials in AWS Systems Manager Parameter Store:

```bash
aws ssm put-parameter --name /cafe/dbUrl --value "your-db-endpoint" --type String
aws ssm put-parameter --name /cafe/dbName --value "cafe_db" --type String
aws ssm put-parameter --name /cafe/dbUser --value "dbuser" --type String
aws ssm put-parameter --name /cafe/dbPassword --value "password" --type SecureString
```

### 2. IAM Roles

#### salesAnalysisReportRole Permissions:
- AmazonSNSFullAccess
- AmazonSSMReadOnlyAccess
- AWSLambdaBasicExecutionRole
- AWSLambdaRole (invoke other functions)

#### salesAnalysisReportDERole Permissions:
- AWSLambdaBasicExecutionRole
- AWSLambdaVPCAccessExecutionRole

### 3. VPC Configuration

Configure the data extractor function with:
- VPC: Cafe VPC
- Subnet: Cafe Public Subnet 1
- Security Group: CafeSecurityGroup (allow MySQL port 3306)

### 4. Environment Variables

Set for `salesAnalysisReport` function:
```
topicARN=arn:aws:sns:region:account-id:salesAnalysisReportTopic
```

### 5. SNS Topic Setup

```bash
# Create SNS topic
aws sns create-topic --name salesAnalysisReportTopic

# Subscribe email
aws sns subscribe \
  --topic-arn arn:aws:sns:region:account-id:salesAnalysisReportTopic \
  --protocol email \
  --notification-endpoint your-email@example.com
```

### 6. CloudWatch Events Trigger

Schedule expression (8 PM daily, Monday-Saturday):
```
cron(0 20 ? * MON-SAT *)
```

## 🎮 Usage

### Manual Invocation

#### Test Data Extractor Function

```json
{
  "dbUrl": "database-endpoint",
  "dbName": "cafe_db",
  "dbUser": "admin",
  "dbPassword": "your-password"
}
```

#### Test Main Report Function

```json
{}
```

### Automated Execution

The function automatically runs based on the CloudWatch Events schedule. Check your email for daily reports.

## 🧩 Components

### Directory Structure

```
aws-lambda-sales-analysis/
├── README.md
├── architecture-diagram.png
├── functions/
│   ├── data-extractor/
│   │   ├── salesAnalysisReportDataExtractor.py
│   │   └── requirements.txt
│   └── sales-analysis/
│       ├── salesAnalysisReport.py
│       └── requirements.txt
├── layers/
│   └── pymysql/
│       └── python/
│           └── pymysql/
├── iam-policies/
│   ├── salesAnalysisReportRole.json
│   └── salesAnalysisReportDERole.json
├── cloudformation/
│   └── template.yaml
└── docs/
    ├── setup-guide.md
    ├── troubleshooting.md
    └── architecture.md
```

### Lambda Functions

#### 1. salesAnalysisReportDataExtractor
- **Runtime**: Python 3.9
- **Purpose**: Query MySQL database for sales data
- **Dependencies**: PyMySQL (via Lambda Layer)
- **Timeout**: 10 seconds
- **Memory**: 128 MB

#### 2. salesAnalysisReport
- **Runtime**: Python 3.9
- **Purpose**: Orchestrate report generation and delivery
- **Dependencies**: boto3 (AWS SDK)
- **Timeout**: 30 seconds
- **Memory**: 128 MB

## 🧪 Testing

### Unit Testing

```bash
# Test data extractor locally
python -m pytest tests/test_data_extractor.py

# Test main report function
python -m pytest tests/test_sales_report.py
```

### Integration Testing

1. Place test orders on the café website
2. Invoke Lambda function manually via AWS Console
3. Verify email receipt
4. Check CloudWatch Logs for execution details

### Common Test Scenarios

- Empty database (no orders)
- Single product order
- Multiple product orders
- Database connection timeout
- Invalid credentials

## 🔧 Troubleshooting

### Timeout Errors

**Symptom**: Function times out after 3 seconds

**Solution**: 
- Increase timeout value in Lambda configuration
- Verify security group allows MySQL port 3306
- Check VPC and subnet configuration

### Database Connection Issues

**Symptom**: Cannot connect to database

**Solution**:
- Verify Parameter Store values
- Check security group inbound rules
- Ensure Lambda function is in correct VPC/subnet
- Validate database endpoint accessibility

### Email Not Received

**Symptom**: No email notification

**Solution**:
- Confirm SNS subscription
- Check spam folder
- Verify topicARN environment variable
- Review CloudWatch Logs for errors

### CloudWatch Logs

View logs for debugging:
```bash
aws logs tail /aws/lambda/salesAnalysisReport --follow
aws logs tail /aws/lambda/salesAnalysisReportDataExtractor --follow
```

## 📊 Monitoring

### CloudWatch Metrics

Monitor the following:
- Invocation count
- Error count
- Duration
- Throttles
- Concurrent executions

### Alarms

Set up CloudWatch Alarms for:
- Function errors > threshold
- Duration > timeout warning
- Throttling events

## 🔒 Security Best Practices

1. **Credentials**: Never hardcode credentials; use Parameter Store
2. **IAM Roles**: Apply least privilege principle
3. **VPC**: Run functions in private subnets when accessing databases
4. **Encryption**: Use SecureString for sensitive parameters
5. **Security Groups**: Restrict inbound rules to necessary ports only

## 📈 Performance Optimization

- **Memory Allocation**: Start with 128 MB, adjust based on metrics
- **Timeout**: Set appropriate timeout (avoid excessive values)
- **Connection Pooling**: Reuse database connections when possible
- **Lambda Layers**: Share common dependencies
- **Cold Start**: Keep functions warm with scheduled invocations

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- Your Name - [GitHub Profile](https://github.com/yourusername)

## 🙏 Acknowledgments

- AWS Lambda Documentation
- AWS Well-Architected Framework
- PyMySQL Contributors

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Contact: your-email@example.com

---

**Note**: This is a lab/educational project. For production use, implement additional security measures, monitoring, and error handling.