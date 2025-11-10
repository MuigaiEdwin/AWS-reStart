# Amazon Route 53 Failover Routing Lab

A hands-on lab demonstrating automated failover configuration using AWS Route 53 for high availability web applications.

## Overview

This lab configures DNS-based failover routing for a café web application deployed across two Availability Zones. When the primary instance becomes unavailable, Route 53 automatically redirects traffic to the secondary instance, ensuring continuous service availability.

## Architecture

- **Primary Instance**: EC2 in us-west-2a running LAMP stack with café application
- **Secondary Instance**: EC2 in us-west-2b (standby) with identical configuration
- **Route 53**: Health checks and failover DNS records
- **Monitoring**: SNS email notifications for health check failures

## Learning Objectives

- Configure Route 53 health checks with email notifications
- Implement failover routing policies
- Test automated failover during simulated outages
- Understand DNS-based high availability patterns

## Lab Tasks

### Task 1: Verify Café Websites
Confirm both EC2 instances are running the application in separate Availability Zones.

### Task 2: Configure Health Check
Create a Route 53 health check monitoring the primary website endpoint with:
- 10-second check interval
- 2 failure threshold
- SNS email notifications

### Task 3: Configure DNS Records
Set up failover routing with:
- **Primary A Record**: Points to CafeInstance1 with health check
- **Secondary A Record**: Points to CafeInstance2 (standby)
- 15-second TTL for fast failover

### Task 4: Verify DNS Resolution
Test that the domain correctly resolves to the primary instance.

### Task 5: Test Failover
Simulate failure by stopping the primary instance and verify:
- Health check detects failure
- Traffic automatically routes to secondary instance
- Email alert is received

## Key Configuration Details

```
Health Check:
- Endpoint: Primary instance IP
- Protocol: HTTP
- Path: /cafe
- Interval: Fast (10 seconds)
- Failure threshold: 2

DNS Records:
- Record type: A (IPv4)
- TTL: 15 seconds
- Routing policy: Failover
```

## Prerequisites

- AWS account with lab environment access
- Two pre-configured EC2 instances with LAMP stack
- Route 53 hosted zone
- Valid email address for notifications

## Duration

Approximately 45 minutes

## Expected Results

When the primary instance fails:
1. Health check status changes to "Unhealthy" within minutes
2. DNS automatically points to secondary instance
3. Email alert is sent via SNS
4. Website remains accessible with minimal downtime

## Technologies Used

- AWS Route 53
- Amazon EC2
- Amazon SNS
- LAMP Stack (Linux, Apache, MySQL, PHP)

## Notes

- DNS changes may take a few minutes to propagate
- Confirm subscription to SNS notifications via email
- Monitor health check status in Route 53 console
- TTL of 15 seconds enables faster failover response

## Lab Completion

Successfully demonstrates:
- ✅ Automated health monitoring
- ✅ DNS-based failover routing
- ✅ Email alerting for failures
- ✅ Multi-AZ high availability architecture

---

**Region**: us-west-2 (Oregon)  
**Availability Zones**: us-west-2a, us-west-2b