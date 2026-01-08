# My Journey: Building a Complete VPC and Launching a Web Server

## What I Just Accomplished

I just built a complete, production-ready VPC from scratch and launched a working web server! This wasn't just clicking through a wizard—I created the entire network infrastructure, configured security, set up routing, and deployed a real application. 

**Time invested:** 45 minutes
**Result:** A fully functional web architecture for a Fortune 100 customer

---

## The Challenge

**Customer Requirements:**
- Create a custom VPC with proper network isolation
- Set up both public and private subnets
- Configure security groups to allow web traffic
- Launch a web server that's accessible from the internet
- Make everything highly available

Looking at their architecture diagram, I thought "This looks complex, but let's break it down step by step."
![Lab Dashboard Screenshot](/screenshots/VPC2architecture.png)
---

## What I Built

By the end, I created:
- ✅ 1 VPC with custom IP addressing (10.0.0.0/16)
- ✅ 2 Public subnets (across 2 availability zones)
- ✅ 2 Private subnets (across 2 availability zones)
- ✅ Internet Gateway for internet access
- ✅ NAT Gateway for private subnet internet access
- ✅ Custom route tables for traffic control
- ✅ Security group with firewall rules
- ✅ EC2 instance running Apache web server
- ✅ Fully working website accessible from anywhere!

---

## My Building Process

### Task 1: Creating the VPC Foundation

This was my first time building a VPC from scratch. I opened the AWS Console and navigated to the VPC service.

**What I did:**

Instead of creating everything manually, I used the **VPC Wizard** (smart move!). Here's what I configured:

```
VPC Name: Lab VPC
IPv4 CIDR: 10.0.0.0/16  (gives me 65,536 IP addresses!)
Availability Zones: 1 (I'll add more later)
Public Subnets: 1
Private Subnets: 1
```

**My subnet configuration:**
- **Public Subnet 1:** `10.0.0.0/24` (256 IPs for internet-facing resources)
- **Private Subnet 1:** `10.0.1.0/24` (256 IPs for internal resources)

I clicked **Create VPC** and watched as AWS built:
- The VPC itself
- An Internet Gateway (automatically attached!)
- Public and Private Route Tables
- A NAT Gateway (for private subnet internet access)
- All the route associations

**Moment of excitement:** Seeing "Success! Your VPC has been created" felt amazing. The foundation was laid!

---

### Task 2: Adding More Subnets (High Availability!)

One availability zone isn't enough for production. What if it goes down? I needed redundancy.

**I created two more subnets:**

**Public Subnet 2:**
```
VPC: Lab VPC
Name: Public Subnet 2
Availability Zone: Different from Subnet 1
CIDR: 10.0.2.0/24
```

This subnet will host web servers in a second location.

**Private Subnet 2:**
```
VPC: Lab VPC
Name: Private Subnet 2
Availability Zone: Different from Subnet 1
CIDR: 10.0.3.0/24
```

This subnet keeps databases and internal services isolated.

**Why this matters:** If one availability zone has issues, my infrastructure keeps running in the other. That's real-world resilience!

---

### Task 3: Configuring Routes (The Traffic Directors)

Creating subnets isn't enough—I needed to tell traffic where to go. This is where route tables come in.

**For Public Subnets:**

I went to **Route Tables** and selected **Public Route Table**.

Under **Subnet Associations**, I added:
- Public Subnet 2

Now both public subnets know how to reach the internet (through the Internet Gateway).

**For Private Subnets:**

I selected **Private Route Table** and associated:
- Private Subnet 2

Private subnets route internet traffic through the NAT Gateway (for security).

**The "aha" moment:** Route tables are like road signs—they tell your traffic which way to go!

![Lab Dashboard Screenshot](/screenshots/VPC1.png)
---

### Task 4: Setting Up Security (The Firewall)

No way was I leaving my web server wide open. Time to create a security group.

**I navigated to Security Groups and created:**

```
Name: Web Security Group
Description: Enable HTTP access
VPC: Lab VPC
```

**Inbound Rules I added:**
```
Type: HTTP
Port: 80
Source: 0.0.0.0/0 (Anywhere - this is a public web server!)
Description: Permit web requests
```

**What this does:**
- Allows anyone on the internet to access my web server on port 80 (HTTP)
- Blocks everything else by default
- SSH access would need a separate rule (security first!)

**Mental note:** This is the exact issue I learned to troubleshoot in my previous lab. Always check security groups!

---

### Task 5: Launching My Web Server

The moment I'd been waiting for—launching the actual EC2 instance!

**I went to EC2 Console → Launch Instance**

**Instance Configuration:**
```
Name: Web Server 1
AMI: Amazon Linux 2
Instance Type: t3.micro (free tier!)
Key Pair: vockey (for SSH access if needed)
```

**Network Settings:**
```
VPC: Lab VPC
Subnet: Public Subnet 2 (my newly created subnet!)
Auto-assign Public IP: ENABLED (crucial for internet access!)
Security Group: Web Security Group
```

**The Magic Part - User Data Script:**

I scrolled to **Advanced Details** and pasted this script:

```bash
#!/bin/bash
# Install Apache Web Server and PHP
yum install -y httpd mysql php

# Download Lab files
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RESTRT-1/267-lab-NF-build-vpc-web-server/s3/lab-app.zip
unzip lab-app.zip -d /var/www/html/

# Turn on web server
chkconfig httpd on
service httpd start
```

**What this script does:**
- Installs Apache web server automatically
- Downloads the website files
- Starts the web server
- All happening while the instance boots!

I clicked **Launch Instance** and held my breath...

---

### The Moment of Truth

**Waiting for initialization:**

I watched the instance status:
- Initializing... ⏳
- Running... ✓
- 1/2 status checks passed... ⏳
- 2/2 status checks passed! ✓✓

**Time to test!**

I copied the **Public IPv4 DNS** from the instance details and opened it in my browser:

```
http://ec2-xx-xxx-xx-xx.us-west-2.compute.amazonaws.com
```

**AND IT WORKED!** 🎉

![Lab Dashboard Screenshot](/screenshots/VPCservergood.png)

The page loaded with:
- AWS logo
- "Congratulations!"
- Instance details
- A fully functional web application

I actually did a fist pump. This was MY infrastructure serving a real website!

---

## What I Learned

### Technical Skills

**VPC Architecture:**
- I now understand CIDR blocks (10.0.0.0/16 = 65,536 IPs)
- Subnet sizing (/24 = 256 IPs per subnet)
- Why you need both public and private subnets

**Routing:**
- Public subnets route to Internet Gateway
- Private subnets route to NAT Gateway
- Route table associations matter!

**Security:**
- Security groups = instance-level firewall
- Inbound rules control what can reach your servers
- Default deny = you must explicitly allow traffic

**High Availability:**
- Multiple availability zones = redundancy
- If one zone fails, others keep working
- This is how real production systems are built

### Problem-Solving Insights

**Breaking down complexity:**
Before starting, the architecture diagram looked intimidating. But by breaking it into tasks (VPC → Subnets → Routes → Security → Instance), it became manageable.

**The importance of order:**
I couldn't launch an instance without:
1. VPC existing first
2. Subnets created
3. Security group configured
4. Routes properly set up

Each step built on the previous one.

**Testing as you go:**
I verified each step before moving forward. When the instance launched successfully, I knew everything before it was correct.

---

## My Thought Process Throughout

**During VPC creation:**
"Okay, 10.0.0.0/16 gives me 65,000+ IPs. That's way more than I need now, but it gives room to grow. Smart planning!"

**Adding subnets:**
"Two availability zones means if one AWS data center has issues, my stuff keeps running in the other. That's why companies pay for cloud!"

**Configuring routes:**
"So public subnets need direct internet access through the IGW, but private subnets go through NAT for security. Makes sense—databases shouldn't be directly on the internet."

**Setting up security:**
"Port 80 for HTTP. If I was doing HTTPS, I'd add port 443. And I'm only allowing what's needed—good security practice!"

**Launching instance:**
"The user data script is brilliant—it automates the entire server setup. No manual SSH needed!"

**Seeing success:**
"That website is running on infrastructure *I* built. Every request is flowing through routers and firewalls *I* configured. This is real!"

---

## What I'd Do Differently Next Time

**Better subnet planning:**
I'd document my IP address scheme first:
- 10.0.0.0/24 = Public Subnet 1
- 10.0.1.0/24 = Private Subnet 1
- 10.0.2.0/24 = Public Subnet 2
- 10.0.3.0/24 = Private Subnet 2
- 10.0.4.0-10.0.255.0 = Future expansion

**Add HTTPS:**
I only set up HTTP (port 80). In production, I'd add HTTPS (port 443) and get an SSL certificate.

**Create a bastion host:**
For accessing private subnet resources, I'd set up a jump box in the public subnet.

**Use Auto Scaling:**
Instead of one instance, I'd create an Auto Scaling group with multiple instances across both availability zones.

**Add a load balancer:**
Distribute traffic across multiple web servers for better performance and reliability.

---

## Real-World Applications

### What I Could Build Now

**E-commerce Platform:**
- Web servers in public subnets
- Database in private subnets
- NAT Gateway for private subnet updates
- Security groups controlling all access

**Multi-tier Application:**
- Frontend (public subnet)
- API layer (public subnet)
- Database (private subnet)
- Each tier isolated and secure

**Corporate Infrastructure:**
- VPN into private subnets
- Internal services never exposed to internet
- Secure communication between tiers

---

## Challenges I Overcame

**Challenge 1: Understanding CIDR notation**
Initially, `/16` and `/24` seemed confusing. But breaking it down:
- /16 = 65,536 IPs (big network)
- /24 = 256 IPs (subnet)
- Makes sense when you think in powers of 2!

**Challenge 2: Route table associations**
At first, I wasn't sure which subnets needed which route tables. But the logic clicked:
- Public = needs internet gateway route
- Private = needs NAT gateway route

**Challenge 3: Security group configuration**
I had to think: "What traffic do I actually need?" Not just opening everything. Port 80 for web traffic, that's it.

---

## The Complete Architecture I Built

**What I started with:** Nothing

**What I ended with:**

```
Lab VPC (10.0.0.0/16)
│
├── Public Subnet 1 (10.0.0.0/24) ─┐
├── Public Subnet 2 (10.0.2.0/24) ─┤→ Internet Gateway → Internet
│                                   │
├── Private Subnet 1 (10.0.1.0/24) ─┤
├── Private Subnet 2 (10.0.3.0/24) ─┘→ NAT Gateway → Internet
│
├── Web Security Group (Port 80 open)
│
└── Web Server 1 (Public Subnet 2)
    └── Running Apache + PHP
    └── Public IP Address
    └── Serving live website!
```

**From diagram to reality:** The customer's architecture diagram became my running infrastructure!

![Lab Dashboard Screenshot](/screenshots/
---

## Key Takeaways

**Planning is crucial:**
- Decide IP ranges before creating anything
- Plan for growth (I have room for 60+ more subnets!)
- Think about security from the start

**Automation saves time:**
- User data scripts set up servers automatically
- No manual configuration needed
- Repeatable and consistent

**High availability requires redundancy:**
- Multiple availability zones
- Multiple subnets
- Proper load distribution

**Security is non-negotiable:**
- Security groups control access
- Private subnets protect sensitive resources
- Only open necessary ports

---

## Skills I've Developed

After completing this lab, I can:

✅ Design and implement VPC architectures
✅ Calculate and allocate CIDR blocks
✅ Create and configure subnets
✅ Set up routing for public and private traffic
✅ Configure security groups with appropriate rules
✅ Launch and configure EC2 instances
✅ Use user data scripts for automation
✅ Implement high availability across availability zones
✅ Troubleshoot connectivity issues
✅ Think about infrastructure as code

---

## What's Next for Me

**Immediate goals:**
1. **Add HTTPS support** - Get SSL certificate, add port 443
2. **Create load balancer** - Distribute traffic across instances
3. **Set up monitoring** - CloudWatch metrics and alarms
4. **Implement auto scaling** - Handle traffic spikes automatically

**Learning objectives:**
1. **Infrastructure as Code** - Learn Terraform or CloudFormation
2. **Advanced networking** - VPC peering, Transit Gateway
3. **Database integration** - RDS in private subnets
4. **CI/CD pipeline** - Automate deployments

**Portfolio projects:**
1. Build a fully automated deployment pipeline
2. Create a multi-region architecture
3. Implement disaster recovery setup
4. Design a secure microservices architecture

---

## Resources That Helped Me

- [VPC Documentation](https://docs.aws.amazon.com/vpc/)
- [CIDR.xyz](https://cidr.xyz/) - Visual CIDR calculator
- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [VPC Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)

---

## My Reflection

This lab was a game-changer. I didn't just learn *about* VPCs—I *built* one. I didn't just read about security groups—I *configured* them. I didn't just understand subnets—I *created* and *routed* them.

The moment my web page loaded, I realized: I just built the same infrastructure that powers real companies. The architecture diagram the customer provided? I delivered it, fully