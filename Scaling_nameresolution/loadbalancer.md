# AWS Auto Scaling and Load Balancing Lab

## Overview
Hands-on lab implementing Elastic Load Balancing (ELB) and EC2 Auto Scaling to create a fault-tolerant, automatically scalable web infrastructure on AWS.

## Architecture Evolution

**Starting State:**
- Single web server in public subnet

**Final State:**
- Application Load Balancer
- Auto Scaling Group with 2-4 EC2 instances
- Instances distributed across 2 Availability Zones in private subnets
- CloudWatch alarms for monitoring

## What You'll Build

### 1. **Custom AMI Creation**
- Create Amazon Machine Image from existing EC2 instance
- Capture web server configuration for auto scaling

### 2. **Application Load Balancer**
- Configure ALB across multiple Availability Zones
- Set up target groups for health checks
- Route HTTP traffic to backend instances

### 3. **Launch Template**
- Define instance configuration (AMI, instance type, security groups)
- Create reusable template for Auto Scaling

### 4. **Auto Scaling Group**
- **Min instances:** 2
- **Max instances:** 4
- **Scaling policy:** Target tracking at 50% CPU utilization
- Deploy instances in private subnets across 2 AZs

### 5. **CloudWatch Monitoring**
- Configure alarms for CPU utilization
- Automatic scaling based on performance metrics

## Key Hands-On Tasks

### Task 1: Create AMI
```
EC2 → Instances → Select Web Server 1 → Actions → Image and templates → Create image
```

### Task 2: Configure Load Balancer
```
EC2 → Load Balancers → Create ALB → Configure:
- VPC: Lab VPC
- Subnets: Public Subnet 1 & 2
- Security Group: Web Security Group
- Target Group: lab-target-group
```

### Task 3: Build Launch Template
```
EC2 → Launch Templates → Create template:
- Name: lab-app-launch-template
- AMI: Web Server AMI
- Instance type: t3.micro
- Security Group: Web Security Group
```

### Task 4: Setup Auto Scaling
```
Auto Scaling Groups → Create:
- Launch template: lab-app-launch-template
- VPC: Lab VPC
- Subnets: Private Subnet 1 & 2
- Attach to load balancer target group
- Health checks: ELB
- Group size: Desired=2, Min=2, Max=4
- Scaling policy: Target tracking (50% CPU)
```

### Task 5: Verify Load Balancing
- Check instance health status in target group
- Access application via load balancer DNS name
- Confirm traffic distribution

### Task 6: Test Auto Scaling
- Use Load Test application to generate CPU load
- Monitor CloudWatch alarms (AlarmHigh/AlarmLow)
- Observe automatic instance scaling when CPU > 50%

## Testing the Setup

1. **Access the application:**
   ```
   http://<load-balancer-dns-name>
   ```
![Lab Dashboard Screenshot](/screenshots/Load%20Test.png)

2. **Generate load:**
   - Click "Load Test" in the application
   - Watch CPU utilization increase in CloudWatch

   ![Lab Dashboard Screenshot](/screenshots/)

3. **Monitor scaling:**
   - AlarmHigh triggers when CPU > 50% for 3 minutes
   - Auto Scaling launches additional instances (up to 4)
   - AlarmLow triggers when load decreases

## Key Concepts Demonstrated

- **High Availability:** Multi-AZ deployment
- **Fault Tolerance:** Load balancer distributes traffic
- **Elasticity:** Automatic scaling based on demand
- **Cost Optimization:** Scale down during low usage
- **Monitoring:** CloudWatch alarms for proactive management

## Configuration Summary

| Component | Configuration |
|-----------|--------------|
| Load Balancer | Application Load Balancer (HTTP) |
| Instance Type | t3.micro (fallback: t2.micro) |
| Subnets | Private subnets in 2 AZs |
| Scaling Metric | Average CPU Utilization |
| Scaling Target | 50% CPU |
| Instance Range | 2-4 instances |
| Health Check | ELB health checks |

## Prerequisites
- AWS Account with lab environment
- VPC with public and private subnets
- Security groups configured for HTTP traffic
- Existing Web Server 1 instance

## Duration
⏱️ Approximately 45 minutes

## Optional Challenge
Create an AMI using AWS CLI:
```bash
# Configure credentials
aws configure

# Create AMI
aws ec2 create-image \
  --instance-id <instance-id> \
  --name "CLI-Created-AMI" \
  --description "AMI created via CLI"
```

## Troubleshooting

- **Instance type unavailable:** Use t2.micro instead of t3.micro
- **Health check failing:** Wait 30-60 seconds and refresh
- **Alarm not triggering:** Ensure load test is running continuously

## Clean Up
Remember to terminate resources after lab completion to avoid charges:
- Delete Auto Scaling Group
- Delete Load Balancer
- Delete Target Group
- Deregister AMI
- Terminate Web Server 1 instance

## Learning Outcomes
✅ Create and manage AMIs  
✅ Configure Application Load Balancers  
✅ Implement Auto Scaling groups  
✅ Set up CloudWatch monitoring  
✅ Design highly available architectures  
✅ Optimize costs through automatic scaling  

---

**Note:** This lab uses AWS-provided infrastructure. Ensure you're working within the lab environment and not your personal AWS account.