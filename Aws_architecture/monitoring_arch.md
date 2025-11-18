# AWS Infrastructure Monitoring Lab

A comprehensive hands-on lab for implementing monitoring, logging, and compliance tracking in AWS using CloudWatch, Systems Manager, and AWS Config.

## 📋 Overview

This lab demonstrates enterprise-grade monitoring practices including:
- Installing and configuring CloudWatch agents on EC2 instances
- Collecting and analyzing application logs
- Creating custom metrics and alarms
- Setting up real-time infrastructure notifications
- Implementing compliance monitoring with AWS Config

## 🏗️ Monitoring Architecture

![Lab Dashboard Screenshot](/screenshots/monitoring-architecture.png)

```
Amazon VPC
├── Public Subnet
│   └── Web Server (EC2)
│       ├── CloudWatch Agent
│       ├── Apache Web Server
│       └── System Logs
├── AWS Systems Manager
│   ├── Run Command
│   └── Parameter Store
├── Amazon CloudWatch
│   ├── CloudWatch Logs
│   ├── CloudWatch Metrics
│   └── CloudWatch Events
├── Amazon SNS (Notifications)
└── AWS Config (Compliance Monitoring)
```

## ⏱️ Duration

Approximately 60 minutes

## 🎯 Learning Objectives

By completing this lab, you will:
- ✅ Install CloudWatch agent using AWS Systems Manager Run Command
- ✅ Monitor application logs using CloudWatch Logs
- ✅ Monitor system metrics (CPU, memory, disk) using CloudWatch Metrics
- ✅ Create real-time notifications using CloudWatch Events
- ✅ Track infrastructure compliance using AWS Config

## 📚 Prerequisites

- AWS Account with appropriate permissions
- Valid email address for notifications
- Basic understanding of:
  - EC2 instances
  - Web server concepts
  - JSON configuration
  - Regular expressions (helpful but not required)

## 🚀 Lab Tasks

### Task 1: Installing the CloudWatch Agent

**What You'll Do:**
- Use AWS Systems Manager Run Command to deploy CloudWatch agent
- Configure agent to collect web server logs and system metrics
- Store configuration in Systems Manager Parameter Store

**Key Components:**
- **Package**: `AmazonCloudWatchAgent`
- **Configuration Storage**: Parameter Store (`Monitor-Web-Server`)
- **Logs Collected**: Apache access logs & error logs
- **Metrics Collected**: CPU, disk, memory, swap

**Configuration Details:**
```json
Logs:
  - HttpAccessLog (/var/log/httpd/access_log)
  - HttpErrorLog (/var/log/httpd/error_log)

Metrics (10-second intervals):
  - CPU: usage_idle, usage_iowait, usage_user, usage_system
  - Disk: used_percent, inodes_free
  - Disk I/O: io_time
  - Memory: mem_used_percent
  - Swap: swap_used_percent
```

---

### Task 2: Monitoring Application Logs

**What You'll Do:**
- Generate log data by accessing the web server
- View logs in CloudWatch Logs
- Create a metric filter to detect 404 errors
- Set up an alarm to notify when error threshold is exceeded

**Key Concepts:**
- **Log Groups**: HttpAccessLog, HttpErrorLog
- **Log Streams**: One per EC2 instance
- **Metric Filter**: Pattern matching for 404 status codes
- **Alarm Threshold**: ≥5 errors in 1 minute

**Metric Filter Pattern:**
```
[ip, id, user, timestamp, request, status_code=404, size]
```

**Testing:**
1. Access non-existent pages (e.g., `/start`, `/test`, `/page`)
2. Generate at least 5× 404 errors within 1 minute
3. Receive email notification when alarm triggers

---

### Task 3: Monitoring Instance Metrics

**What You'll Do:**
- Explore built-in EC2 metrics (external view)
- Examine CloudWatch agent metrics (internal view)
- Compare hypervisor-level vs instance-level metrics

**Available Metrics:**

| Category | Built-in EC2 | CloudWatch Agent |
|----------|--------------|------------------|
| CPU | ✅ Basic | ✅ Detailed (idle, iowait, user, system) |
| Disk | ❌ | ✅ Space usage, inodes |
| Memory | ❌ | ✅ Used percentage |
| Network | ✅ Basic | ✅ Enhanced |

**Exploration Path:**
```
CloudWatch → Metrics → All metrics → CWAgent
├── device, fstype, host, path (disk metrics)
└── host (memory metrics)
```

---

### Task 4: Creating Real-Time Notifications

**What You'll Do:**
- Create CloudWatch Events rule for instance state changes
- Configure SNS notifications for stopped/terminated instances
- Test by stopping the Web Server instance

**Event Rule Configuration:**
- **Service**: EC2
- **Event Type**: EC2 Instance State-change Notification
- **States Monitored**: `stopped`, `terminated`
- **Target**: SNS Topic
- **Notification**: Email

**Use Cases:**
- Security alerts for unauthorized instance termination
- Cost management (instances accidentally left running)
- Operational awareness during deployments
- Compliance tracking for infrastructure changes

---

### Task 5: Monitoring Infrastructure Compliance

**What You'll Do:**
- Enable AWS Config
- Create compliance rules for resource tagging
- Monitor EBS volume attachment status
- View compliance reports

**Config Rules Implemented:**

1. **required-tags**
   - Purpose: Ensure all resources have a `project` tag
   - Compliance: Compliant if tag exists, non-compliant otherwise

2. **ec2-volume-inuse-check**
   - Purpose: Identify unattached EBS volumes (cost optimization)
   - Compliance: Compliant if attached, non-compliant if detached

**Compliance Results:**
- View resources by compliance status
- Identify non-compliant resources for remediation
- Track compliance trends over time

---

## 🛠️ Key Commands & Configurations

### Systems Manager - Installing CloudWatch Agent

```bash
# Run Command: AWS-ConfigureAWSPackage
Action: Install
Name: AmazonCloudWatchAgent
Version: latest
Target: Web Server instance
```

### Parameter Store Configuration

```bash
# Create parameter
Name: Monitor-Web-Server
Description: Collect web logs and system metrics
Value: [JSON configuration provided in lab]
```

### Starting CloudWatch Agent

```bash
# Run Command: AmazonCloudWatch-ManageAgent
Action: configure
Mode: ec2
Configuration Source: ssm
Configuration Location: Monitor-Web-Server
Restart: yes
Target: Web Server instance
```

### Testing Log Generation

```bash
# Access web server
http://[WebServerIP]/

# Generate 404 errors
http://[WebServerIP]/start
http://[WebServerIP]/test
http://[WebServerIP]/page1
http://[WebServerIP]/page2
http://[WebServerIP]/page3
```

### CloudWatch Logs - Metric Filter

```bash
Filter Pattern: [ip, id, user, timestamp, request, status_code=404, size]
Metric Namespace: LogMetrics
Metric Name: 404Errors
Metric Value: 1
```

### CloudWatch Alarm Configuration

```bash
Alarm Name: 404 Errors
Metric: LogMetrics/404Errors
Period: 1 minute
Condition: Greater/Equal than 5
Notification: SNS Topic (email)
```

---

## 📊 Monitoring Best Practices Demonstrated

### 1. **Layered Monitoring Approach**
- External metrics (hypervisor-level)
- Internal metrics (OS-level)
- Application logs
- Custom business metrics

### 2. **Proactive Alerting**
- Threshold-based alarms
- Anomaly detection patterns
- Real-time event notifications

### 3. **Compliance Automation**
- Continuous compliance checking
- Automated resource discovery
- Policy enforcement

### 4. **Centralized Logging**
- Aggregated logs from multiple sources
- Searchable and filterable
- Long-term retention

---

## 🔔 Email Notifications You'll Receive

1. **SNS Subscription Confirmation** (Task 2)
   - Confirm to start receiving alerts
   
2. **404 Errors Alarm** (Task 2)
   - Triggered when ≥5 errors in 1 minute
   
3. **Instance State Change** (Task 4)
   - Notifies when instance is stopped/terminated

---

## 📈 Metrics Collection Intervals

| Metric Type | Collection Interval | Retention |
|-------------|---------------------|-----------|
| CloudWatch Agent Metrics | 10 seconds | Up to 15 months |
| EC2 Basic Metrics | 5 minutes (free) | Up to 15 months |
| EC2 Detailed Metrics | 1 minute (paid) | Up to 15 months |
| CloudWatch Logs | Real-time | Configurable |

---

## 🎓 Key Concepts Explained

### **CloudWatch Agent vs Built-in Metrics**

**Built-in EC2 Metrics (Free):**
- Collected by AWS hypervisor
- External view of instance
- Limited to: CPU, network, disk I/O, status checks
- Cannot see inside the OS

**CloudWatch Agent Metrics:**
- Runs inside the instance
- Full visibility into OS
- Includes: memory, disk space, process metrics
- Requires installation and configuration

### **Log Groups vs Log Streams**

- **Log Group**: Container for related logs (e.g., HttpAccessLog)
- **Log Stream**: Individual log source (e.g., one per EC2 instance)

### **Metric Filters**

Convert log data into numerical metrics that can be:
- Graphed over time
- Used in alarms
- Aggregated across multiple sources

---

## 🔍 Troubleshooting

### CloudWatch Agent Not Sending Data

```bash
# Check agent status
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
  -a query -m ec2 -c ssm:Monitor-Web-Server -s

# View agent logs
sudo tail -f /opt/aws/amazon-cloudwatch-agent/logs/amazon-cloudwatch-agent.log
```

### Logs Not Appearing

- Wait 1-2 minutes for initial data collection
- Verify IAM role permissions
- Check agent configuration in Parameter Store
- Ensure log files exist and are readable

### Alarm Not Triggering

- Verify metric filter is created
- Check that test pattern shows results
- Confirm SNS subscription is confirmed
- Wait for full evaluation period (1 minute)

---

## 💰 Cost Considerations

**Included in Free Tier:**
- First 5GB of log ingestion per month
- First 10 custom metrics
- First 10 alarms
- Basic monitoring (5-minute intervals)

**Paid Services:**
- Detailed monitoring (1-minute intervals)
- Additional custom metrics
- Log storage beyond free tier
- AWS Config rule evaluations

---

## 🧹 Cleanup

After completing the lab:

1. **Stop/Terminate EC2 Instances**
   ```bash
   # Via Console: EC2 → Instances → Select → Instance State → Terminate
   ```

2. **Delete CloudWatch Resources**
   - Delete alarms
   - Delete metric filters
   - Delete log groups (if desired)

3. **Remove CloudWatch Events Rules**
   - Delete Instance_Stopped_Terminated rule

4. **Disable AWS Config**
   - Stop recording
   - Delete rules

5. **Delete SNS Topics** (if no longer needed)
   - Default_CloudWatch_Alarms_Topic

---

## 📖 Additional Resources

- [CloudWatch Agent Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
- [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [AWS Config Rules Library](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)
- [CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/)
- [Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

---

## 🎯 Real-World Applications

This lab prepares you for:

- **DevOps Engineer**: Implementing comprehensive monitoring
- **SRE**: Building reliable, observable systems
- **Security Analyst**: Detecting anomalous behavior
- **Compliance Officer**: Ensuring policy adherence
- **Cost Optimization**: Identifying unused resources

---

## ✅ Success Criteria

- [ ] CloudWatch agent installed and running
- [ ] Web server logs visible in CloudWatch Logs
- [ ] System metrics (CPU, memory, disk) being collected
- [ ] 404 error alarm created and tested
- [ ] Email notifications received for alarm and instance state changes
- [ ] AWS Config rules evaluating compliance
- [ ] Identified compliant and non-compliant resources

---

## 🤝 Contributing

Improvements and suggestions welcome! Please submit issues or pull requests.

## 📄 License

This lab guide is provided for educational purposes.

---

**Ready to start monitoring?** Follow the lab instructions step by step and build enterprise-grade observability! 🚀