# Managing Services - Monitoring Lab

## Overview

This lab teaches you essential service management and system monitoring skills for Linux-based cloud infrastructure. You'll learn how to manage system services using systemctl, monitor resource usage with Linux tools, and leverage AWS CloudWatch for comprehensive instance monitoring. These skills are critical for maintaining application availability, troubleshooting performance issues, and implementing proactive monitoring strategies in production environments.

## Learning Objectives

By completing this lab, you will be able to:

- Check service status using systemctl commands
- Start, stop, and manage the Apache HTTP server (httpd) service
- Verify web server functionality through HTTP connections
- Monitor system resources in real-time using the top command
- Simulate CPU workload to observe resource consumption
- Use AWS CloudWatch dashboards for instance monitoring
- Analyze CloudWatch metrics including CPU utilization and disk I/O
- Understand the relationship between local monitoring and cloud monitoring

## Lab Duration

Approximately 30 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux 2 EC2 instance
- Familiarity with Linux command-line operations
- Basic understanding of web servers and HTTP
- Access to AWS Management Console

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Amazon Linux 2 instance with Apache HTTP server installed
- **SSH Connection**: Secure remote access to instance
- **Apache HTTP Server (httpd)**: Web server service for testing
- **AWS CloudWatch**: Monitoring and observability service
- **Stress Script**: Pre-installed workload simulation tool

![Lab Dashboard Screenshot](/screenshots/cloudwatch-ec2.png)

## Tasks Overview

### Task 1: Connect to Amazon Linux EC2 Instance via SSH

Establish a secure connection to your Amazon Linux 2 instance.

#### For Windows Users

1. Select **Details** > **Show** to open Credentials window
2. Download `labsuser.ppk` file and note the **PublicIP**
3. Open PuTTY and configure SSH session with the downloaded key
4. Connect to the instance

#### For macOS and Linux Users

1. Select **Details** > **Show** to open Credentials window
2. Download `labsuser.pem` file and note the **PublicIP**
3. Set up SSH connection:
   ```bash
   cd ~/Downloads
   chmod 400 labsuser.pem
   ssh -i labsuser.pem ec2-user@<public-ip>
   ```

### Task 2: Check the Status of the httpd Service

Learn to manage system services using systemctl, the systemd service manager.

#### Understanding httpd

**httpd** (HTTP Daemon) is the Apache HTTP Server service—a widely-used web server that powers millions of websites worldwide. It serves web pages, handles HTTP requests, and delivers content to browsers.

#### Check Service Status

Verify the current state of the httpd service:
```bash
sudo systemctl status httpd.service
```

Expected output:
```
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: inactive (dead)
```

**Status interpretation**:
- **Loaded**: Service is installed and configuration is available
- **inactive (dead)**: Service is not currently running
- **disabled**: Service will not start automatically at boot

#### Start the Service

Start the httpd service:
```bash
sudo systemctl start httpd.service
```

This command starts Apache immediately but does not produce output if successful.

#### Verify Service is Running

Check status again to confirm:
```bash
sudo systemctl status httpd.service
```

Expected output:
```
● httpd.service - The Apache HTTP Server
   Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabled)
   Active: active (running) since Wed 2025-11-26 14:23:45 UTC; 5s ago
   Main PID: 1234 (httpd)
   Status: "Total requests: 0; Idle/Busy workers 100/0"
   CGroup: /system.slice/httpd.service
```

**Status interpretation**:
- **Active: active (running)**: Service is now running
- **Main PID**: Process ID of the main httpd process
- **CGroup**: Control group managing the service

#### Test Web Server Functionality

Verify the web server is responding to HTTP requests:

1. Open a new browser tab
2. Navigate to: `http://<public-ip>`
3. Replace `<public-ip>` with your instance's public IP address

**Expected result**: Apache HTTP Server Test Page displays, confirming the web server is operational.

**Test page elements**:
- Apache logo and branding
- Server configuration information
- Links to Apache documentation
- Confirmation of proper operation

#### Stop the Service

Stop the httpd service:
```bash
sudo systemctl stop httpd.service
```

Verify it stopped:
```bash
sudo systemctl status httpd.service
```

The service should now show `inactive (dead)` status again.

### Task 3: Monitor a Linux EC2 Instance

Learn multiple approaches to system monitoring using both Linux tools and AWS CloudWatch.

#### Part A: Monitor with Linux top Command

Monitor system resources in real-time using the top command.

**Display running processes**:
```bash
top
```

**Understanding top output**:

**Header section**:
```
top - 14:23:45 up 2:15, 1 user, load average: 0.00, 0.01, 0.05
Tasks:  93 total,   1 running,  48 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.2 sy,  0.0 ni, 99.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1009.2 total,    123.5 free,    234.6 used,    651.1 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.    567.9 avail Mem
```

**Key metrics**:
- **Load average**: System load over 1, 5, and 15 minutes
- **CPU usage**: User, system, idle, and I/O wait percentages
- **Memory**: Total, free, used, and buffer/cache amounts

Press **Q** to exit top and return to the shell.

#### Part B: Simulate Workload

Generate CPU load to observe resource consumption:

```bash
./stress.sh & top
```

**Command breakdown**:
- `./stress.sh`: Runs the stress simulation script
- `&`: Runs script in background
- `top`: Launches top to monitor resources

**Expected behavior**:
- CPU usage increases significantly
- The `stress` process appears in top with high CPU percentage (14-14.3% or higher)
- Script runs for 6 minutes before automatically stopping

**Observations in top**:
```
PID  USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
1234 ec2-user  20   0  4280840  30000    500 R  14.3   0.3   0:30.50 stress
```

The stress process consumes substantial CPU resources, simulating production workload.

#### Part C: Monitor with AWS CloudWatch

Use AWS CloudWatch for comprehensive instance monitoring and visualization.

**Open CloudWatch Console**:

1. Click the **AWS** button at the top right of your screen
2. This opens the AWS Management Console in a new tab
3. In the search bar at the top, type `CloudWatch` and press Enter
4. Click on **CloudWatch** in the search results

**Navigate to EC2 Dashboard**:

1. In the left navigation pane, select **Dashboards**
2. Select **Automatic dashboards**
3. From the list, select **EC2**

This opens the pre-configured EC2 monitoring dashboard created by AWS.

**CloudWatch EC2 Dashboard Metrics**:

The dashboard displays several key metrics:

- **CPU Utilization**: Percentage of allocated EC2 compute units currently in use
- **DiskReadBytes**: Bytes read from all instance store volumes
- **DiskReadOps**: Completed read operations from instance store volumes
- **DiskWriteBytes**: Bytes written to all instance store volumes
- **DiskWriteOps**: Completed write operations to instance store volumes
- **NetworkIn**: Bytes received by the instance on all network interfaces
- **NetworkOut**: Bytes sent by the instance on all network interfaces

**Observe CPU Spike**:

You should see a spike in the **CPU Utilization** graph corresponding to when you started the stress.sh script. This demonstrates correlation between local activities and CloudWatch metrics.

**Adjust Time Granularity**:

- By default, CloudWatch aggregates data over 5-minute intervals
- Change the time interval from "5 minutes" to "1 minute" for more granular monitoring
- Use the time range selector to view different time periods

**Wait and Observe Recovery**:

After 5-6 minutes, refresh the CloudWatch dashboard:

1. The stress script will have completed automatically
2. CPU utilization will drop back to normal levels
3. The graph shows the complete cycle: baseline → spike → recovery

**Expected graph pattern**:
- Initial baseline: Low CPU (~0-5%)
- Stress period: High CPU (~33-62.6%)
- Recovery: Return to baseline after script completion

## Key Concepts Covered

### systemd and systemctl

**systemd** is the init system and service manager for Linux systems. It manages services, handles system startup, and controls system states.

**systemctl** is the command-line tool for controlling systemd services.

### Service States

- **Active (running)**: Service is currently running
- **Active (exited)**: One-time service completed successfully
- **Inactive (dead)**: Service is not running
- **Failed**: Service attempted to start but failed

### Service Control Operations

- **start**: Begin running the service
- **stop**: Terminate the running service
- **restart**: Stop and then start the service
- **reload**: Reload configuration without stopping
- **enable**: Start service automatically at boot
- **disable**: Don't start service automatically at boot

### AWS CloudWatch

A monitoring and observability service that collects and tracks metrics, logs, and events from AWS resources and applications.

**Key features**:
- Real-time monitoring dashboards
- Customizable metrics and alarms
- Historical data analysis
- Integration with all AWS services
- Automatic dashboards for common services

### CloudWatch Metrics for EC2

AWS automatically publishes metrics to CloudWatch at no additional charge:

**Basic Monitoring** (5-minute intervals):
- CPU utilization
- Disk reads/writes
- Network in/out
- Status checks

**Detailed Monitoring** (1-minute intervals, additional cost):
- Same metrics with higher frequency
- Better for detecting short-duration issues

## Essential Commands Reference

### systemctl Commands

| Command | Purpose |
|---------|---------|
| `systemctl status service` | Check service status |
| `systemctl start service` | Start a service |
| `systemctl stop service` | Stop a service |
| `systemctl restart service` | Restart a service |
| `systemctl reload service` | Reload configuration |
| `systemctl enable service` | Enable service at boot |
| `systemctl disable service` | Disable service at boot |
| `systemctl is-active service` | Check if service is running |
| `systemctl is-enabled service` | Check if service starts at boot |
| `systemctl list-units --type=service` | List all services |

### Monitoring Commands

| Command | Purpose |
|---------|---------|
| `top` | Real-time process monitoring |
| `htop` | Enhanced process viewer |
| `free -h` | Memory usage |
| `df -h` | Disk space usage |
| `iostat` | CPU and I/O statistics |
| `vmstat` | Virtual memory statistics |
| `netstat` | Network connections |
| `ss` | Socket statistics |
| `uptime` | System uptime and load |

## Practical Examples

### Service Management

```bash
# Check if Apache is running
sudo systemctl status httpd

# Start Apache web server
sudo systemctl start httpd

# Enable Apache to start at boot
sudo systemctl enable httpd

# Restart Apache after config changes
sudo systemctl restart httpd

# Check all failed services
systemctl --failed

# View service logs
sudo journalctl -u httpd.service

# Follow service logs in real-time
sudo journalctl -u httpd.service -f
```

### Monitoring Scenarios

```bash
# Monitor CPU usage continuously
top -d 1

# Show only specific user's processes
top -u ec2-user

# Memory usage summary
free -h

# Disk usage by filesystem
df -h

# Disk usage by directory
du -sh /var/log/*

# Network connections
netstat -tuln

# Active network connections
ss -tuln

# System load averages
uptime

# Check CPU information
lscpu

# View system logs
journalctl -xe
```

### CloudWatch CLI Commands

```bash
# List available metrics
aws cloudwatch list-metrics --namespace AWS/EC2

# Get CPU utilization statistics
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --start-time 2025-11-26T00:00:00Z \
  --end-time 2025-11-26T23:59:59Z \
  --period 300 \
  --statistics Average

# Create CloudWatch alarm
aws cloudwatch put-metric-alarm \
  --alarm-name cpu-high \
  --alarm-description "Alarm when CPU exceeds 80%" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold
```

## Troubleshooting Tips

### Service Issues
- **Service won't start**: Check logs with `journalctl -u service-name -xe`
- **Port already in use**: Check what's using the port with `netstat -tuln | grep :80`
- **Permission denied**: Ensure using `sudo` for system services
- **Configuration errors**: Validate config files before restarting service

### Monitoring Issues
- **CloudWatch shows no data**: Wait 5-15 minutes for metrics to appear
- **Metrics delayed**: Basic monitoring has 5-minute delay
- **High CPU but nothing in top**: Check for I/O wait or system processes
- **Memory usage unclear**: Use `free -h` and check buffer/cache

### Web Server Issues
- **Cannot access web page**: Check security group allows port 80 inbound
- **Connection refused**: Verify httpd service is running
- **403 Forbidden**: Check file permissions and SELinux settings
- **404 Not Found**: Verify document root and file paths

## Important Notes

- This lab uses Amazon Linux 2 with systemd service management
- CloudWatch metrics are collected automatically for all EC2 instances
- Basic monitoring (5-minute intervals) is free; detailed monitoring costs extra
- The stress script runs for exactly 6 minutes before stopping automatically
- Stopping httpd makes the web server inaccessible but doesn't uninstall it
- Always use `sudo` for system service management commands

## Best Practices

### Service Management
- Always check status before starting/stopping services
- Use `enable` for services that should survive reboots
- Test configuration files before restarting services
- Monitor logs when troubleshooting service issues
- Use `reload` instead of `restart` when possible to avoid downtime
- Document service dependencies and startup order

### Monitoring Strategy
- Establish performance baselines during normal operation
- Set up CloudWatch alarms for critical thresholds
- Monitor trends over time, not just current values
- Use detailed monitoring for production workloads
- Combine local tools (top) with cloud monitoring (CloudWatch)
- Create custom dashboards for application-specific metrics

### CloudWatch Best Practices
- Use metric filters to create custom metrics from logs
- Set up SNS notifications for CloudWatch alarms
- Create dashboards for different stakeholder needs
- Use CloudWatch Logs for centralized log management
- Implement retention policies to manage costs
- Tag resources for organized monitoring

### Production Recommendations
```bash
# Enable httpd to start at boot
sudo systemctl enable httpd

# Set up log rotation for Apache
sudo logrotate -f /etc/logrotate.d/httpd

# Create CloudWatch alarm for high CPU
# (Use AWS CLI or Console)

# Monitor service health
sudo systemctl status httpd
sudo journalctl -u httpd -f
```

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting (Amazon Linux 2 instance)
- **AWS CloudWatch**: Monitoring and observability
- **AWS Management Console**: Service management interface

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **CloudWatch Alarms**: Set up notifications for threshold breaches
- **CloudWatch Logs**: Centralized log aggregation and analysis
- **CloudWatch Events/EventBridge**: Event-driven automation
- **Custom Metrics**: Publish application-specific metrics
- **CloudWatch Dashboards**: Create custom visualization dashboards
- **CloudWatch Insights**: Query and analyze log data
- **systemd Timers**: Replace cron with systemd timers
- **Service Dependencies**: Configure service startup order
- **Resource Limits**: Set CPU/memory limits with systemd
- **Prometheus/Grafana**: Alternative monitoring solutions
- **AWS Systems Manager**: Advanced instance management
- **AWS X-Ray**: Distributed tracing for applications

## Practice Exercises

To reinforce your learning:

1. **Create alarm** for CPU utilization above 80% for 5 minutes
2. **Configure Apache** to start automatically at boot
3. **Monitor memory** usage and create alert for low available memory
4. **Set up log analysis** to track HTTP error codes in Apache logs
5. **Create custom dashboard** combining CPU, memory, and disk metrics
6. **Implement automated recovery** to restart service if it fails
7. **Monitor network traffic** and alert on unusual patterns
8. **Configure retention** policies for CloudWatch logs

## Related Labs

- Introduction to Amazon EC2
- Introduction to Amazon Linux AMI
- Linux Command Line
- Managing Users and Groups
- Editing Files
- Working with the File System
- Working with Files
- Managing File Permissions
- Working with Commands
- Managing Processes

## Resources

- [systemd Documentation](https://www.freedesktop.org/wiki/Software/systemd/)
- [systemctl Manual](https://www.freedesktop.org/software/systemd/man/systemctl.html)
- [Apache HTTP Server Documentation](https://httpd.apache.org/docs/)
- [AWS CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [CloudWatch Metrics Reference](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux 2 Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-2-virtual-machine.html)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025

**Related Labs**: Introduction to Amazon EC2, Introduction to Amazon Linux AMI, Linux Command Line, Managing Users and Groups, Editing Files, Working with the File System, Working with Files, Managing File Permissions, Working with Commands, Managing Processes