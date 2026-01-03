# My Journey: Troubleshooting a Real Network Issue

## What I Built

I just completed a hands-on troubleshooting lab where I played cloud support engineer and fixed a customer's broken Apache web server. This wasn't just following steps—I had to actually figure out what was wrong.

## The Challenge

**Duration:** 1 hour (but worth every minute!)

**My Role:** Cloud Support Engineer at AWS

**The Customer Email I Received:**

> *"Hello, Cloud Support! When I create an Apache server through the command line, I cannot ping it. I also get an error when I enter the IP address in the browser. Can you please help figure out what is blocking my connection? Thanks! - Ana"*

Reading this, I thought "Okay, web server's running but nobody can reach it. Let's figure this out!"

---

## What I Learned

By the end of this lab, I can now:
- ✅ Diagnose why a working service isn't reachable
- ✅ Systematically check VPC configurations
- ✅ Fix security group and routing issues
- ✅ Think like a support engineer solving real problems

---

![Lab Dashboard Screenshot](/screenshots/CustomerD.png)
## My Troubleshooting Journey

### Step 1: Getting Connected

First, I needed to access Ana's environment (well, a replica of it).

**Windows users** - I used PuTTY with the `.ppk` file
**Mac/Linux users** - I used terminal:

```bash
cd ~/Downloads
chmod 400 labsuser.pem
ssh -i labsuser.pem ec2-user@<public-ip>
```

Once connected, I was in! Now to figure out what's broken.

---

### Step 2: Setting Up Apache (The Web Server)

Before troubleshooting, I needed to get the Apache web server running.

**First, I checked if Apache was installed:**
```bash
sudo systemctl status httpd.service
```

When I ran this, I saw:
```
● httpd.service - The Apache HTTP Server
   Loaded: loaded
   Active: inactive (dead)
```

Okay, so Apache is installed but not running. That's an easy fix!

**I started the service:**
```bash
sudo systemctl start httpd.service
```

**Then verified it was running:**
```bash
sudo systemctl status httpd.service
```

Now I saw:
```
● httpd.service - The Apache HTTP Server
   Loaded: loaded
   Active: active (running)
```

Perfect! Apache is running. But Ana said she couldn't reach it...

**I tried accessing it in my browser:**
```
http://<PUBLIC-IP-ADDRESS>
```

And... nothing. The page wouldn't load. Just like Ana described!

Now the real troubleshooting begins.

---

### Step 3: The Investigation Begins

Time to channel my inner detective. I opened the AWS Console and navigated to VPC services to check Ana's infrastructure.

Here's what I looked at:

#### 🔍 Check 1: Can I Reach the Internet?

First, I tested basic connectivity from the instance:
```bash
ping www.amazon.com
```

It worked! So the instance can reach the internet. This tells me:
- ✅ Internet Gateway exists and is attached
- ✅ Route table has a route to the internet
- ✅ Basic networking works

#### 🔍 Check 2: Subnet Configuration

I navigated to **VPC → Subnets** and checked:
- Is the EC2 instance in a public subnet?
- Does the subnet have a route to the internet gateway?

Looking at the configuration, everything seemed correct here.

#### 🔍 Check 3: Route Tables

Next, I checked **VPC → Route Tables**:
- Is there a route to `0.0.0.0/0` pointing to the internet gateway?
- Is the route table associated with the correct subnet?

Again, routes looked good!

#### 🔍 Check 4: Internet Gateway

Checked **VPC → Internet Gateways**:
- Does one exist?
- Is it attached to the VPC?

Yep, all good here too.

#### 🔍 Check 5: Security Groups (AHA! 💡)

This is where I found the problem!

I went to **EC2 → Security Groups** and looked at the inbound rules.

**What I saw:**
```
Type        Protocol    Port Range    Source
SSH         TCP         22            0.0.0.0/0
```

**What was missing:**
```
HTTP        TCP         80            0.0.0.0/0
```

**That's it!** The security group was blocking HTTP traffic!

Apache runs on port 80 (HTTP). Ana could SSH to the instance (port 22 was open), but couldn't access the web server because port 80 was blocked.

---

### Step 4: The Fix

I added the missing security group rule:

**In the AWS Console:**
1. Selected the security group
2. Clicked "Edit inbound rules"
3. Added a new rule:
   - Type: **HTTP**
   - Protocol: **TCP**
   - Port Range: **80**
   - Source: **0.0.0.0/0** (anywhere)
4. Saved the rules

---

### Step 5: The Moment of Truth

I refreshed my browser with the instance's public IP:
```
http://<PUBLIC-IP-ADDRESS>
```

**And there it was!** 🎉

The Apache test page loaded perfectly:
![Lab Dashboard Screenshot](/screenshots/apache.png)

> **"It works! This is the default web page for this server..."**

Success! I fixed it!

---

## What I Learned From This Experience

### The Troubleshooting Process

1. **Start with basics** - Is the service actually running?
2. **Test connectivity** - Can the instance reach the internet?
3. **Check systematically** - Go through each layer:
   - Network layer (routing, internet gateway)
   - Security layer (security groups, NACLs)
   - Application layer (service status)
4. **Don't assume** - Even if you think something should work, verify it
5. **Document as you go** - I made notes of what I checked

### Key Insights

**Security groups are stateful firewalls**
- They control what traffic can reach your instances
- Inbound rules = what can connect TO your instance
- If you forget to open a port, nobody can use that service

**Common ports to remember:**
- 22 = SSH (remote access)
- 80 = HTTP (web traffic)
- 443 = HTTPS (secure web traffic)
- 3306 = MySQL
- 5432 = PostgreSQL

**The debugging mindset:**
- Work from the outside in (internet → gateway → routing → security → instance → application)
- Eliminate possibilities one by one
- Use tools like ping to test hypotheses

---

## My Troubleshooting Checklist

Based on this experience, here's my mental checklist for similar issues:

**For "Can't reach my server" problems:**

✅ **1. Is the service running?**
```bash
sudo systemctl status service-name
```

✅ **2. Can the instance reach the internet?**
```bash
ping 8.8.8.8
```

✅ **3. Internet Gateway attached?**
- Check VPC → Internet Gateways

✅ **4. Route table configured?**
- Check for 0.0.0.0/0 → igw route

✅ **5. Security group rules?**
- Check inbound rules for required ports

✅ **6. Network ACL rules?**
- Check if NACLs are blocking traffic

---

## Real-World Applications

This lab taught me how to handle actual support tickets. In the real world:

**As a Support Engineer:**
- Customers rarely know exactly what's wrong
- You need to ask good questions
- Systematic troubleshooting saves time
- Documentation helps future you and teammates

**As a Developer:**
- Always check security groups when deploying
- Test services are accessible after deployment
- Keep a troubleshooting checklist handy

**As a SysAdmin:**
- Document your infrastructure
- Use consistent security group naming
- Tag resources properly for easier debugging

---

## Common Mistakes I'll Avoid

From this lab, I learned these common pitfalls:

❌ **Forgetting to open ports** - Just because a service runs doesn't mean people can reach it
❌ **Assuming routing is correct** - Always verify routes explicitly
❌ **Not testing from outside** - Test from a browser/external source, not just localhost
❌ **Changing too many things at once** - Fix one thing, test, then move to next
❌ **Not documenting what you tried** - Keep notes of what you've checked

---

## The Bigger Picture

This lab connected several concepts I'd learned separately:

**VPC Networking:**
- Subnets need routes to internet gateways
- Public vs private subnet differences matter

**Security:**
- Security groups = instance-level firewall
- Default deny = you must explicitly allow traffic

**Services:**
- Starting a service ≠ making it accessible
- systemctl is your friend for managing services

**Troubleshooting:**
- Work methodically, layer by layer
- Don't skip steps even if you "know" what's wrong
- Test your fix before declaring victory

---

## What I'd Do Differently

If I did this lab again or faced a similar real scenario:

1. **Start with security groups immediately** - They're the most common cause of connectivity issues
2. **Use the VPC Reachability Analyzer** - AWS has tools to help debug these exact scenarios
3. **Document the "before" state** - Makes it easier to explain what I fixed
4. **Test with curl first** - Faster than opening browser each time
   ```bash
   curl http://public-ip
   ```

---

## Skills I've Built

After this lab, I'm comfortable with:

✅ **Troubleshooting methodology** - Systematic, layer-by-layer approach
✅ **VPC debugging** - Checking gateways, routes, and security
✅ **Service management** - Starting/stopping/checking services with systemctl
✅ **Security group configuration** - Understanding and modifying rules
✅ **Customer communication** - Thinking about how to explain findings

---

## What's Next?

Building on this experience, I want to:

1. **Practice more troubleshooting scenarios** - Different services, different problems
2. **Learn about Network ACLs** - The other security layer
3. **Master VPC Flow Logs** - To see exactly what traffic is being blocked
4. **Automate checks** - Scripts to verify common misconfigurations
5. **Learn about VPC Peering** - For more complex network architectures

---

## Resources That Helped Me

- [VPC Documentation](https://docs.aws.amazon.com/vpc/)
- [Security Group Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
- [Troubleshooting Connectivity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-connectivity.html)

---

## Final Thoughts

This lab was incredibly valuable because it simulated a real support ticket. I wasn't just configuring things—I was *fixing* things. That's where the real learning happens.

The satisfaction of seeing that Apache test page load after figuring out the problem? That's what makes this field exciting.

**Key Takeaway:** Troubleshooting is a skill you build through practice. Each problem you solve makes you better at solving the next one.

---

**Lab Status:** ✅ Complete - Problem Solved!

**Customer Status:** 🎉 Happy - Ana can now access her Apache server!

**My Confidence:** 📈 Significantly improved!

**Last Updated:**   Jan 2026

---

*This lab took me about an hour, but I learned troubleshooting skills I'll use for years.*