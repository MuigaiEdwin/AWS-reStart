# Internet Protocols: Public and Private IP Addresses

## Summary
This project focuses on exploring how public and private IP addressing works within AWS. I investigated a real-world networking scenario involving EC2 connectivity issues, analyzed the root cause, and documented findings related to IP addressing and VPC design.

---

## Scenario Overview
During the lab, I acted as a cloud support engineer responding to a customer issue.  
The customer had:

- A VPC with CIDR **10.0.0.0/16**
- Two EC2 instances (Instance A and Instance B) in the same subnet
- Correct routing and an Internet Gateway already attached

The problem:  
**Instance A could not reach the internet, while Instance B could — despite having similar configurations.**

The customer also asked whether it is acceptable to use a public IP range such as **12.0.0.0/16** when creating a new VPC.

---

## Investigation and Analysis

### EC2 Networking Review
I inspected the networking configuration for both EC2 instances.  
Key findings:

- **Instance A** had only a **private IPv4 address**
- **Instance B** had both a **private and a public IPv4 address**

This difference immediately suggested why one instance could reach the internet and the other could not.

### SSH Connectivity Test
To validate the findings, I attempted SSH connections:

- **Instance B** → Successfully connected via its public IP  
- **Instance A** → Connection failed  

This confirmed that Instance A lacked a public IP and therefore had no direct path to the internet or external access.

### Root Cause
**Instance A could not access the internet because it did not have a public IP address.**  

Although subnet routing and the internet gateway were correctly configured, the instance itself needed a public IP assignment for external connectivity.

---

## Insight on Using Public CIDR Ranges for VPCs
The customer asked whether it is advisable to use a public IP block (such as **12.0.0.0/16**) for a new VPC.

### Conclusion
It is **not recommended** to use public, non-RFC1918 address ranges for private AWS VPCs.

### Reasons:
- Public IP ranges are globally routable on the internet  
- They risk conflicting with external networks using the same range  
- Routing responses may behave unpredictably  
- AWS networking best practices are designed around **private RFC1918 ranges**

### Valid Private IP Ranges (RFC1918)
- **10.0.0.0/8**
- **172.16.0.0/12**
- **192.168.0.0/16**

Using these ranges avoids conflicts and ensures smooth routing within AWS and on corporate networks.

---

## Conclusion
Through the investigation, I identified that the internet connectivity issue was caused by the absence of a public IP on Instance A. I also concluded that using public CIDR blocks for VPC creation can create routing conflicts and is not an AWS-recommended practice.

This exercise reinforced my understanding of:

- The difference between public and private IP addresses  
- How IP addressing affects EC2 connectivity  
- Best practices when designing VPC CIDR allocations  

---

## References
- AWS EC2 Instance IP Addressing  
- Amazon VPC CIDR Documentation  
- RFC1918 – Private IP Address Standards