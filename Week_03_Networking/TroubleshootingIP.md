# Network Troubleshooting Commands Lab

## Overview

Learn the essential commands every network admin needs to diagnose connection problems. You'll practice the tools used daily to figure out why things aren't working—from "can't reach the server" to "which port is open?"

## What You'll Learn

- Test if a server is reachable with `ping`
- Trace network paths and find slow hops with `traceroute`
- Check which ports are open with `netstat`
- Test specific port connections with `telnet`
- Verify web services with `curl`

## Duration

30 minutes

## Your Role

You're a network admin troubleshooting customer issues. Each command solves a different type of problem.

---

## Task 1: Connect to Your Instance

**Windows:**
- Download `.ppk` file → Use PuTTY

**Mac/Linux:**
```bash
cd ~/Downloads
chmod 400 labsuser.pem
ssh -i labsuser.pem ec2-user@<public-ip>
```

---

## Task 2: Your Troubleshooting Toolkit

### Command 1: ping - "Can I Reach It?"

**Customer Problem:**
"I just launched an EC2 instance. How do I know if it's reachable?"

**Your Solution:**
```bash
ping 8.8.8.8 -c 5
```

**What it does:**
- Sends 5 test packets to Google's DNS server
- Each reply shows round-trip time
- Confirms basic network connectivity

**What you'll see:**
```
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=1.23 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=1.18 ms
...
5 packets transmitted, 5 received, 0% packet loss
```

**Reading the results:**
- ✅ **Getting replies?** Connection works!
- ❌ **Request timeout?** Can't reach server (firewall? security group?)
- ⚠️ **Packet loss?** Unstable connection

**Real-world use:**
- First step in troubleshooting connectivity
- Check if security groups allow ICMP
- Verify internet gateway works

---

### Command 2: traceroute - "Where's the Slowdown?"

**Customer Problem:**
"My connection is slow and I'm getting packet loss. Is it AWS or my ISP?"

**Your Solution:**
```bash
traceroute 8.8.8.8
```

**What it does:**
- Shows every hop (router) between you and destination
- Measures latency at each hop
- Helps pinpoint where problems occur

**What you'll see:**
```
1  192.168.1.1 (192.168.1.1)  1.234 ms
2  10.0.0.1 (10.0.0.1)  5.678 ms
3  * * *  (Request timed out)
4  8.8.8.8 (8.8.8.8)  12.345 ms
```

**Reading the results:**
- Each line = one hop (router/server)
- Times = how long that hop took
- `* * *` = that hop isn't responding (might be normal if router ignores traceroute)

**Where's the problem?**
- **Early hops slow?** → Local network or ISP issue
- **Last hops slow?** → Destination server issue
- **Consistent high times?** → Bandwidth problem

---

### Command 3: netstat - "What Ports Are Open?"

**Customer Problem:**
"Security scan found a compromised port on our subnet. Can you verify what's actually listening?"

**Your Solution:**
```bash
netstat -tp     # Show active connections
netstat -tlp    # Show listening services
netstat -ntlp   # Show listening services with port numbers
```

**What it does:**
- Shows all network connections on your machine
- Lists which ports are listening for connections
- Identifies which programs are using which ports

**What you'll see:**
```
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      1234/sshd
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      5678/mysqld
```

**Reading the results:**
- **Local Address** - What your machine is listening on
- **State: LISTEN** - Port is open and waiting for connections
- **State: ESTABLISHED** - Active connection
- **PID/Program** - Which service is using the port

**Common ports to know:**
- 22 = SSH
- 80 = HTTP
- 443 = HTTPS
- 3306 = MySQL
- 5432 = PostgreSQL

**Real-world use:**
- Verify only expected services are running
- Check if port is already in use before starting service
- Security audits

---

### Command 4: telnet - "Can I Connect to This Port?"

**Customer Problem:**
"My security group should be blocking port 80, but I want to verify it's actually blocked."

**First, install telnet:**
```bash
sudo yum install telnet -y
```

**Then test the connection:**
```bash
telnet www.google.com 80
```

**What it does:**
- Tests if you can connect to a specific port
- Different from ping (which tests general reachability)
- Helps verify firewall/security group rules

**What you'll see:**

**Success (port open):**
```
Trying 142.250.80.46...
Connected to www.google.com.
Escape character is '^]'.
```

**Failed (port blocked):**
```
Trying 192.168.10.5...
telnet: connect to address 192.168.10.5: Connection refused
```

**Timeout (no route):**
```
Trying 192.168.10.5...
telnet: connect to address 192.168.10.5: Connection timed out
```

**What each error means:**
- **Connection refused** = Port is blocked (firewall, security group)
- **Connection timed out** = Can't reach server at all (network routing issue)
- **Connected** = Port is open and accepting connections

**Real-world use:**
- Verify security group rules work correctly
- Test if web server port is accessible
- Check database port connectivity

---

### Command 5: curl - "Is the Web Service Working?"

**Customer Problem:**
"My Apache server is running. Can you verify it's responding correctly?"

**Your Solution:**
```bash
curl -vLo /dev/null https://aws.com
```

**What it does:**
- Makes HTTP/HTTPS requests to web servers
- Shows detailed connection information
- Verifies web service is responding properly

**Understanding the flags:**
- `-v` = Verbose (show everything that's happening)
- `-L` = Follow redirects
- `-o /dev/null` = Throw away the HTML response (we just want headers)

**What you'll see:**
```
* Connected to aws.com (54.239.28.85) port 443
* SSL connection using TLSv1.3
> GET / HTTP/1.1
> Host: aws.com
< HTTP/1.1 200 OK
< Content-Type: text/html
```

**Reading the results:**
- **200 OK** = Success! Server responding normally
- **301/302** = Redirect (usually fine)
- **403 Forbidden** = Server refuses request
- **404 Not Found** = Page doesn't exist
- **500 Server Error** = Something broken on server
- **Connection refused** = Can't connect at all

**Other useful curl commands:**
```bash
curl -I https://aws.com           # Just headers
curl -i https://aws.com           # Headers + content
curl -k https://badssl.com        # Ignore SSL errors
curl https://api.github.com       # Test API endpoints
```

**Real-world use:**
- Verify web server is up and running
- Check SSL certificate validity
- Test API endpoints
- Monitor HTTP response codes

---

## Quick Troubleshooting Guide

### "Can't Connect to Server"

**Step 1: Can you reach it at all?**
```bash
ping server-ip
```
- ❌ No response → Network/routing issue
- ✅ Getting replies → Server reachable, check further

**Step 2: Where's the problem?**
```bash
traceroute server-ip
```
- Slow/failed early → Your network/ISP
- Slow/failed late → Destination network

**Step 3: Is the port open?**
```bash
telnet server-ip 80
```
- Connection refused → Port blocked
- Connected → Port open, check application

**Step 4: Is the service responding?**
```bash
curl http://server-ip
```
- 200 OK → Everything works!
- Other codes → Application issue

---

## Common Scenarios

### Scenario 1: Website Down
```bash
# Quick diagnosis
ping example.com              # Server reachable?
telnet example.com 80         # Port open?
curl -I http://example.com    # HTTP working?
```

### Scenario 2: Database Connection Issues
```bash
# Check from app server
telnet db-server 3306         # Can reach MySQL?
netstat -ntlp | grep 3306     # Is DB listening?
```

### Scenario 3: Security Group Verification
```bash
# Test if port actually blocked
telnet server-ip 22           # Should succeed (SSH)
telnet server-ip 80           # Should fail if blocked
```

### Scenario 4: Latency Investigation
```bash
# Find where latency occurs
traceroute slow-server.com
# Look for hops with high ms values
```

---

## Command Cheat Sheet

| Command | What It Tests | Use When |
|---------|--------------|----------|
| `ping` | Basic connectivity | "Can I reach it?" |
| `traceroute` | Network path | "Where's the slowdown?" |
| `netstat` | Open ports/connections | "What's listening?" |
| `telnet` | Specific port | "Is this port open?" |
| `curl` | Web service | "Is the site working?" |

---

## Pro Tips

1. **Always start with ping** - Establish basic connectivity first
2. **Traceroute takes time** - Be patient, especially over internet
3. **Remember security groups** - AWS blocks ICMP and ports by default
4. **Document your findings** - Copy/paste output for customer tickets
5. **Test from both directions** - Client to server AND server to client

---

## Common Issues & Fixes

**"Ping: Network unreachable"**
- Check your network connection
- Verify route to destination exists

**"Traceroute: all asterisks"**
- ICMP might be blocked
- Try with `-I` flag: `traceroute -I example.com`

**"Netstat: permission denied"**
- Use sudo: `sudo netstat -ntlp`

**"Telnet: command not found"**
- Install it: `sudo yum install telnet -y`

**"Curl: SSL certificate problem"**
- Ignore SSL errors (testing only): `curl -k https://site.com`

---

## Practice Exercises

Try these to build your troubleshooting skills:

1. **Ping your instance** from your local machine
2. **Traceroute to google.com** - count the hops
3. **List all listening ports** on your instance
4. **Test port 443** to various websites
5. **Curl a few sites** and compare response times

---

## Related Labs

- Managing Services - Monitoring
- Create Subnets in Amazon VPC
- Introduction to Amazon EC2

## Resources

- [Ping Manual](https://linux.die.net/man/8/ping)
- [Traceroute Guide](https://www.cloudflare.com/learning/network-layer/what-is-traceroute/)
- [Netstat Documentation](https://linux.die.net/man/8/netstat)
- [Curl Manual](https://curl.se/docs/manual.html)

---

**Lab Status**: Complete ✓

**You're now ready to troubleshoot network issues like a pro!** 🎯

**Last Updated**: November 2025