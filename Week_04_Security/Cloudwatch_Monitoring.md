# Monitor an EC2 Instance Using CloudWatch

A hands-on lab demonstrating how to implement monitoring and alerting for EC2 instances using Amazon CloudWatch and Amazon SNS for security incident detection.

## Overview

This project demonstrates the implementation of logging and monitoring techniques to detect potential security incidents. The lab simulates a malicious actor spiking CPU utilization on an EC2 instance and shows how CloudWatch alarms with SNS notifications can alert administrators to suspicious activity.

## Technologies Used

- **Amazon CloudWatch** - Monitoring and observability service for AWS resources
- **Amazon SNS** - Simple Notification Service for application-to-application and application-to-person messaging
- **AWS EC2** - Elastic Compute Cloud instance for stress testing
- **AWS Systems Manager** - Session Manager for secure instance access
- **IAM** - Identity and Access Management for secure access control
- **Linux stress utility** - Tool for CPU load testing

## Lab Objectives

- ✅ Create an Amazon SNS notification topic and subscription
- ✅ Configure a CloudWatch alarm with metric thresholds
- ✅ Stress test an EC2 instance to simulate security incident
- ✅ Confirm that Amazon SNS email notifications are sent
- ✅ Create a CloudWatch dashboard for metric visualization

## Security Scenario

**Simulated Attack:**
- Malicious actor gains control of EC2 instance
- CPU utilization spikes to 100%
- Potential causes: malware, cryptomining, DoS attack
- CloudWatch alarm detects anomaly and sends alert

## Architecture

```
┌─────────────────────────────────────────────────────┐
│              EC2 Instance (Stress Test)             │
│  ┌────────────────────────────────────────────┐    │
│  │  CPU Load: 0% → 100% (Stress Command)     │    │
│  └────────────────────────────────────────────┘    │
└────────────────────┬────────────────────────────────┘
                     │
                     │ Metrics
                     ▼
        ┌────────────────────────┐
        │   Amazon CloudWatch    │
        │  ┌──────────────────┐  │
        │  │ CPUUtilization   │  │
        │  │    Metric        │  │
        │  └──────────────────┘  │
        │  ┌──────────────────┐  │
        │  │  Alarm Rules     │  │
        │  │  Threshold: 60%  │  │
        │  │  Period: 1 min   │  │
        │  └──────────────────┘  │
        └────────┬───────────────┘
                 │
                 │ Threshold Exceeded
                 ▼
        ┌────────────────────┐
        │   Amazon SNS       │
        │  ┌──────────────┐  │
        │  │  MyCwAlarm   │  │
        │  │    Topic     │  │
        │  └──────────────┘  │
        └────────┬───────────┘
                 │
                 │ Email Notification
                 ▼
        ┌────────────────────┐
        │  Administrator     │
        │  Email Alert       │
        └────────────────────┘
```

## Key Concepts

### Logging vs Monitoring

| Aspect | Logging | Monitoring |
|--------|---------|------------|
| **Purpose** | Record and store data events | Analyze and collect data for performance |
| **Output** | Log files with low-level details | Metrics, dashboards, alerts |
| **Use Case** | Troubleshooting, audit trails | Real-time performance optimization |
| **Security Value** | Identify red flags and anomalies | Detect unauthorized access |
| **Data Type** | Discrete events | Aggregated metrics over time |

### Amazon CloudWatch Components

**Metrics**
- Time-ordered data points published to CloudWatch
- Represent system performance characteristics
- Examples: CPUUtilization, NetworkIn, DiskReadOps

**Alarms**
- Watch metrics and trigger actions based on thresholds
- States: OK, ALARM, INSUFFICIENT_DATA
- Actions: SNS notifications, Auto Scaling, EC2 actions

**Dashboards**
- Customizable views of metrics and alarms
- Monitor resources across multiple Regions
- Single-pane-of-glass visibility

### Amazon SNS

**Pub/Sub Messaging:**
- Publishers send messages to topics
- Subscribers receive messages from topics
- Protocols: Email, SMS, HTTP/HTTPS, Lambda, SQS

**Communication Types:**
- **A2A** (Application-to-Application): Microservices, distributed systems
- **A2P** (Application-to-Person): Mobile notifications, email alerts

## Lab Tasks

### Task 1: Configure Amazon SNS

**Objective:** Create notification mechanism for CloudWatch alarms.

**Steps:**

1. **Create SNS Topic**
   ```
   Type: Standard
   Name: MyCwAlarm
   ```

2. **Create Subscription**
   ```
   Protocol: Email
   Endpoint: [your-email@example.com]
   ```

3. **Confirm Subscription**
   - Check email inbox
   - Click "Confirm subscription" link
   - Verify status changes to "Confirmed"

**Result:** ✅ SNS topic configured and ready to send email notifications

### Task 2: Create a CloudWatch Alarm

**Objective:** Configure alarm to detect CPU utilization anomalies.

**Metric Configuration:**
```
Metric Name: CPUUtilization
Instance: Stress Test
Statistic: Average
Period: 1 minute
```

**Alarm Conditions:**
```
Threshold Type: Static
Condition: Greater than threshold
Threshold Value: 60%
```

**Alarm Actions:**
```
Alarm State Trigger: In alarm
SNS Topic: MyCwAlarm
```

**Alarm Details:**
```
Name: LabCPUUtilizationAlarm
Description: CloudWatch alarm for Stress Test EC2 instance CPUUtilization
```

**Alarm States:**

| State | Description | Trigger |
|-------|-------------|---------|
| **OK** | Metric is within threshold | CPU ≤ 60% |
| **ALARM** | Metric exceeded threshold | CPU > 60% |
| **INSUFFICIENT_DATA** | Not enough data to evaluate | Metric unavailable |

**Result:** ✅ CloudWatch alarm configured to monitor CPU utilization

### Task 3: Test the CloudWatch Alarm

**Objective:** Simulate security incident and verify alert mechanism.

**Stress Test Command:**
```bash
sudo stress --cpu 10 -v --timeout 400s
```

**Command Breakdown:**

| Parameter | Description |
|-----------|-------------|
| `--cpu 10` | Spawn 10 CPU-intensive workers |
| `-v` | Verbose output |
| `--timeout 400s` | Run for 400 seconds (6.67 minutes) |

**Monitoring Command:**
```bash
top
```
This displays live CPU usage statistics.

**Expected Timeline:**

```
Time 0s:     CPU at 0%         [OK State]
Time 30s:    CPU rises to 100% [ALARM State triggered]
Time 60s:    Email notification sent
Time 400s:   Stress test ends
Time 430s:   CPU returns to 0% [OK State]
```

**Email Notification:**
```
Subject: ALARM: "LabCPUUtilizationAlarm" in US East (N. Virginia)
From: AWS Notifications

You are receiving this email because your Amazon CloudWatch Alarm 
"LabCPUUtilizationAlarm" in the US East (N. Virginia) region has 
entered the ALARM state...

State Change: OK -> ALARM
Reason: Threshold Crossed: 1 datapoint [95.0] was greater than the 
threshold (60.0).
```

**Result:** ✅ CPU spike detected, alarm triggered, and email notification received

### Task 4: Create a CloudWatch Dashboard

**Objective:** Build custom monitoring dashboard for quick access.

**Dashboard Configuration:**
```
Dashboard Name: LabEC2Dashboard
Widget Type: Line chart
Metric Source: EC2 Per-Instance Metrics
Instance: Stress Test
Metric: CPUUtilization
```

**Dashboard Benefits:**
- Quick access to critical metrics
- Customizable views
- Multi-region monitoring
- Real-time visualization
- Shareable URLs

**Result:** ✅ Custom dashboard created for CPUUtilization monitoring

## Monitoring Best Practices

### Alarm Configuration

✅ **Do:**
- Set meaningful threshold values based on baseline
- Use appropriate evaluation periods
- Configure multiple notification channels
- Test alarms after creation
- Document alarm purpose and response procedures
- Use composite alarms for complex conditions

❌ **Don't:**
- Set thresholds too sensitive (alert fatigue)
- Forget to test notification delivery
- Create alarms without clear action plans
- Ignore insufficient data states

### Metric Selection

**Critical EC2 Metrics:**

| Metric | Threshold Example | Alert Indicates |
|--------|-------------------|-----------------|
| **CPUUtilization** | > 80% for 5 min | High load, possible attack |
| **NetworkIn** | Unusual spike | Data exfiltration, DDoS |
| **DiskReadOps** | > baseline × 3 | Malware scanning files |
| **StatusCheckFailed** | > 0 | Instance or system failure |
| **MemoryUtilization*** | > 90% | Memory leak, resource exhaustion |

*Requires CloudWatch agent installation

### Notification Strategy

**Severity Levels:**

```
CRITICAL (immediate): CPUUtilization > 95%, Page on-call engineer
HIGH (15 min):        CPUUtilization > 80%, Email team + Slack
MEDIUM (1 hour):      CPUUtilization > 60%, Email team
LOW (24 hours):       CPUUtilization > 50%, Dashboard review
```

## Security Use Cases

### Detecting Malicious Activity

**CPU Spike Indicators:**
1. **Cryptomining** - Sustained 100% CPU usage
2. **Malware Execution** - Sudden CPU increase
3. **Brute Force Attacks** - Periodic CPU spikes
4. **DDoS Attacks** - CPU + network metric correlation

**Response Workflow:**
```
Alert Received
    ↓
Investigate CloudWatch Metrics
    ↓
Check CloudTrail Logs for API Calls
    ↓
Review VPC Flow Logs for Network Activity
    ↓
Isolate Instance (Security Group Change)
    ↓
Take Snapshot for Forensics
    ↓
Terminate Compromised Instance
    ↓
Launch Clean Replacement
```

### Monitoring Patterns

**Normal Behavior:**
```
CPU: Steady 5-20%
Network: Consistent baseline
Disk: Predictable I/O patterns
```

**Suspicious Behavior:**
```
CPU: Sudden 100% spike
Network: Outbound traffic surge
Disk: Unusual read/write patterns
Status: Failed health checks
```

## Advanced CloudWatch Features

### Composite Alarms

Combine multiple alarms with AND/OR logic:
```
ALARM IF (CPUUtilization > 80% AND NetworkOut > 1GB)
```

### Anomaly Detection

CloudWatch can automatically detect anomalies:
```
Uses machine learning
Adapts to changing patterns
Reduces false positives
```

### Log Insights

Query and analyze log data:
```
Filter for specific events
Aggregate metrics from logs
Create visualizations
Set up alerts on log patterns
```

### Metric Math

Perform calculations on metrics:
```
Example: Calculate CPU efficiency
METRIC1 / METRIC2 * 100
```

## Cost Optimization

**Free Tier:**
- 10 custom metrics
- 10 alarms
- 1 million API requests
- 5GB log data ingestion

**Best Practices:**
- Use metric filters efficiently
- Set appropriate retention periods
- Delete unused alarms and dashboards
- Use standard resolution (1-minute) vs high (1-second)

## Troubleshooting

### Alarm Not Triggering

**Possible Causes:**
- Insufficient data points
- Incorrect metric namespace
- Wrong statistic type
- Evaluation period too long

**Solutions:**
- Check metric availability in CloudWatch
- Verify alarm configuration matches metric
- Reduce evaluation periods for faster detection
- Review alarm history for details

### Email Not Received

**Possible Causes:**
- Subscription not confirmed
- Email in spam folder
- SNS topic permissions
- Invalid email address

**Solutions:**
- Confirm subscription status in SNS
- Check spam/junk folders
- Verify topic policy allows CloudWatch
- Test subscription with manual publish

## Learning Outcomes

Through this lab, I gained hands-on experience with:
- Configuring CloudWatch alarms for security monitoring
- Creating SNS topics and email subscriptions
- Simulating security incidents through stress testing
- Understanding CPU utilization patterns and thresholds
- Building CloudWatch dashboards for metric visualization
- Implementing automated alerting for incident response
- Differentiating between logging and monitoring
- Applying monitoring best practices for security

## Real-World Applications

**DevOps:**
- Performance monitoring
- Auto-scaling triggers
- Application health checks

**Security:**
- Intrusion detection
- Resource abuse detection
- Compliance monitoring

**Operations:**
- Capacity planning
- Incident response
- SLA monitoring

## Prerequisites

- AWS Account with appropriate permissions
- Access to email for SNS subscription
- Understanding of EC2 and basic Linux commands
- Familiarity with monitoring concepts

## Duration

Approximately 60 minutes

## Cleanup

To avoid charges (if running outside lab environment):
- Delete CloudWatch alarms
- Delete SNS topics and subscriptions
- Delete CloudWatch dashboards
- Stop or terminate EC2 instances

## References

- [Amazon CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [Amazon SNS Documentation](https://docs.aws.amazon.com/sns/)
- [CloudWatch Alarm Actions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)
- [EC2 Metrics Reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)
- [CloudWatch Best Practices](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Best_Practice_Recommended_Alarms_AWS_Services.html)

## Related Labs

- CloudWatch Logs for Application Monitoring
- Auto Scaling with CloudWatch Metrics
- AWS CloudTrail for API Auditing
- VPC Flow Logs Analysis
- CloudWatch Events (EventBridge) Automation

## License

This is an educational lab project for learning AWS monitoring and security incident detection.

---

**Note**: This lab was completed as part of AWS training. The stress test scenario simulates a security incident for educational purposes in a controlled environment. Always implement proper monitoring and alerting in production environments following your organization's security policies.