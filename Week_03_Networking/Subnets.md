# Project: Creating Subnets and Allocating IP Addresses in an Amazon VPC

## Project Overview
As part of my personal upskilling in cloud networking and AWS, I decided to build a Virtual Private Cloud (VPC) environment from scratch. The goal was to understand how to create a VPC, design subnets, and allocate IP addresses efficiently while following best practices for network segmentation.

---

## Project Objectives
Through this project, I aimed to:

- Explore the process of creating a VPC and configuring subnets.
- Learn how to assign IPv4 CIDR blocks and calculate IP address ranges.
- Understand the difference between public and private subnets.
- Familiarize myself with the AWS Management Console and VPC services.
- Apply networking concepts like CIDR notation and subnetting in a practical environment.

---

## Project Scenario
I imagined a scenario where a startup requires a VPC setup:

- The VPC needs approximately 15,000 private IP addresses.
- There should be a public subnet with at least 50 IP addresses for operational resources.
- The VPC IPv4 range must be within the private 192.x.x.x range.

This helped me apply real-world networking requirements while experimenting in a safe AWS environment.

---

## Steps I Followed

### 1. Determine the CIDR Ranges
- Using RFC 1918 guidelines and a subnet calculator, I chose the following:

**VPC:**
- IPv4 CIDR: `192.168.0.0/18` → ~16,382 IP addresses (enough for 15,000 requirement)

**Public Subnet:**
- IPv4 CIDR: `192.168.1.0/26` → 62 IP addresses (covers the requirement of 50 IPs)

### 2. Create the VPC
- Opened **Amazon VPC** in AWS Management Console.
- Launched a new VPC and configured it with:
  - Name: `First VPC`
  - IPv4 CIDR: `192.168.0.0/18`
  - No IPv6 CIDR
  - Default tenancy

### 3. Create the Public Subnet
- Configured the subnet with:
  - Name: `Public subnet`
  - Availability Zone: No preference
  - IPv4 CIDR: `192.168.1.0/26`
- Ensured the subnet had a public route via an Internet Gateway for external access.

---

## Key Learnings

1. **VPC Architecture:**  
   - VPCs act like virtual data centers in the cloud, isolating resources within a logical network.

2. **Subnetting & CIDR Notation:**  
   - Learned how to calculate the number of IP addresses per subnet.
   - Applied CIDR ranges to meet specific IP requirements.

3. **Public vs Private Subnets:**  
   - Public subnets allow internet access using public IPs and an Internet Gateway.
   - Private subnets are isolated from the internet, ensuring secure internal communication.

4. **AWS Console Navigation:**  
   - Gained experience in launching VPCs, creating subnets, and understanding the AWS networking dashboard.

5. **Planning for Scale:**  
   - Designed the VPC to handle a large number of IP addresses (~15,000) while also allocating smaller subnets for specific operational needs.

---

## Conclusion
This project helped me gain hands-on experience in cloud networking on AWS. I now understand how to:

- Design and create a VPC with public and private subnets.
- Allocate IP addresses efficiently based on real-world requirements.
- Apply subnetting concepts and CIDR blocks in practical scenarios.
- Navigate and utilize the AWS Management Console for network setup.

This exercise has strengthened my confidence in AWS networking and prepared me for more complex cloud architecture tasks in future projects.
