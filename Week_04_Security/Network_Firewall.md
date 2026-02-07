# Malware Protection Using AWS Network Firewall

A hands-on lab demonstrating how to configure AWS Network Firewall to block access to malicious websites and prevent malware downloads in a corporate network environment.

## Overview

This project simulates a real-world security scenario where a security engineer must protect an organization's network from malware threats. The lab demonstrates how to implement network-level security controls using AWS Network Firewall with Suricata IPS rules to block specific malicious URLs.

## Technologies Used

- **AWS Network Firewall** - Managed network firewall service for VPC protection
- **Suricata** - Open-source intrusion prevention system (IPS) with rule-based language
- **AWS EC2** - Elastic Compute Cloud instance for testing
- **AWS Systems Manager** - Session Manager for secure instance access
- **AWS VPC** - Virtual Private Cloud for network isolation
- **IAM** - Identity and Access Management for secure access control

## Lab Objectives

- ✅ Update and configure a network firewall
- ✅ Create a stateful firewall rules group using Suricata syntax
- ✅ Implement IPS rules to block malicious URLs
- ✅ Verify and test that access to malicious sites is blocked

## Business Scenario

**AnyCompany Security Challenge:**
- Users accidentally downloading malware from specific websites
- IT team identified URLs hosting malicious files
- Security engineer tasked with blocking access to these sites
- Need network-level solution to protect all users

## Architecture

```
Internet
    │
    ├─── Malicious Site (malware.wicar.org)
    │
    ▼
┌─────────────────────────────────────────┐
│     AWS Network Firewall                │
│  ┌─────────────────────────────────┐   │
│  │  Firewall Policy                │   │
│  │  ├─ Stateless Rules              │   │
│  │  │   └─ Forward to Stateful     │   │
│  │  └─ Stateful Rule Group          │   │
│  │      └─ Suricata IPS Rules       │   │
│  │         ├─ Block js_crypto_miner │   │
│  │         └─ Block java_jre17_exec │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
              │
              ▼
    ┌──────────────────┐
    │   LabVPC         │
    │  ┌────────────┐  │
    │  │ Perimeter  │  │
    │  │   Zone     │  │
    │  │ ┌────────┐ │  │
    │  │ │  Test  │ │  │
    │  │ │Instance│ │  │
    │  │ └────────┘ │  │
    │  └────────────┘  │
    └──────────────────┘
```

## Key Concepts

### Malware Types
- **Viruses** - Self-replicating programs that infect files
- **Worms** - Standalone malware that replicates across networks
- **Trojans** - Malicious programs disguised as legitimate software
- **Spyware** - Software that secretly monitors user activity
- **Adware** - Unwanted software that displays advertisements
- **Ransomware** - Malware that encrypts data and demands payment

### Firewall Concepts

**Stateful vs Stateless Inspection:**

| Feature | Stateful | Stateless |
|---------|----------|-----------|
| **Context** | Inspects packets in context of traffic flow | Inspects each packet in isolation |
| **Complexity** | Supports complex rules | Simple, fast rules |
| **Direction** | Considers traffic direction | No directional awareness |
| **Performance** | May delay packets for grouping | Prioritizes speed |
| **Use Case** | Deep inspection, logging, alerts | Quick filtering, DoS protection |

### AWS Network Firewall Components

1. **Firewall** - The managed firewall resource
2. **Firewall Policy** - Defines firewall behavior
3. **Rule Groups** - Reusable sets of inspection criteria
   - Stateful rule groups
   - Stateless rule groups

## Lab Tasks

### Task 1: Confirm Reachability

**Objective:** Verify that malicious URLs are accessible before implementing controls.

```bash
# Navigate to home directory
cd ~
pwd

# Download malicious test files (in protected lab environment only)
wget http://malware.wicar.org/data/js_crypto_miner.html
wget http://malware.wicar.org/data/java_jre17_exec.html

# Verify downloads
ls
```

**Expected Output:**
```
HTTP request sent, awaiting response... 200 OK
Length: [SIZE] (text/html)
Saving to: 'js_crypto_miner.html'
```

**Result:** ✅ Successfully confirmed that malicious files are accessible (vulnerability exists)

### Task 2: Inspect the Network Firewall

**Objective:** Review existing firewall configuration and prepare for updates.

**Steps:**
1. Navigated to VPC → Network Firewall → Firewalls
2. Selected `LabFirewall`
3. Opened associated `LabFirewallPolicy`
4. Updated stateless default actions:
   - Fragmented packets: **Use the same actions for all packets**
   - Action: **Forward to stateful rule groups**

**Result:** ✅ Configured firewall to forward all traffic to stateful inspection

### Task 3: Create a Firewall Rule Group

**Objective:** Create Suricata IPS rules to block malicious URLs.

**Configuration:**
- **Rule Group Type:** Stateful rule group
- **Rule Group Format:** Suricata compatible rule string
- **Rule Evaluation Order:** Action order
- **Name:** StatefulRuleGroup
- **Capacity:** 100

**Suricata IPS Rules Created:**

```suricata
drop http $HOME_NET any -> $EXTERNAL_NET 80 (msg:"MALWARE custom solution"; flow: to_server,established; classtype:trojan-activity; sid:2002001; content:"/data/js_crypto_miner.html";http_uri; rev:1;)

drop http $HOME_NET any -> $EXTERNAL_NET 80 (msg:"MALWARE custom solution"; flow: to_server,established; classtype:trojan-activity; sid:2002002; content:"/data/java_jre17_exec.html";http_uri; rev:1;)
```

**Suricata Rule Breakdown:**

| Component | Description |
|-----------|-------------|
| `drop` | Action to take (drop the packet) |
| `http` | Protocol to inspect |
| `$HOME_NET any` | Source network and port |
| `$EXTERNAL_NET 80` | Destination network and port |
| `msg:"..."` | Alert message description |
| `flow: to_server,established` | Direction and connection state |
| `classtype:trojan-activity` | Classification type |
| `sid:2002001` | Unique signature ID |
| `content:"/data/..."` | URI content to match |
| `http_uri` | Apply content match to HTTP URI |
| `rev:1` | Revision number |

**Result:** ✅ Created stateful rule group with Suricata IPS rules

### Task 4: Attach Rule Group to Network Firewall

**Objective:** Apply the rule group to the active firewall.

**Steps:**
1. Selected `LabFirewall`
2. Opened associated `LabFirewallPolicy`
3. Added unmanaged stateful rule group
4. Selected `StatefulRuleGroup`
5. Confirmed successful attachment

**Result:** ✅ Rule group successfully attached to firewall policy

### Task 5: Validate the Solution

**Objective:** Test that malicious URLs are now blocked.

```bash
# Navigate to home directory
cd ~
pwd

# Attempt to download blocked file #1
wget http://malware.wicar.org/data/js_crypto_miner.html

# Expected output: HTTP request sent, awaiting response... (hangs)
# Press Ctrl+C to stop

# Attempt to download blocked file #2
wget http://malware.wicar.org/data/java_jre17_exec.html

# Expected output: HTTP request sent, awaiting response... (hangs)
# Press Ctrl+C to stop

# Clean up test files
rm java_jre17_exec.html js_crypto_miner.html

# Verify cleanup
ls
```

**Before Firewall Rules:**
```
HTTP request sent, awaiting response... 200 OK
Saving to: 'js_crypto_miner.html'
```

**After Firewall Rules:**
```
HTTP request sent, awaiting response...
(connection blocked - hangs indefinitely)
```

**Result:** ✅ Malicious URLs successfully blocked by network firewall

## Security Best Practices Implemented

- ✅ **Network Segmentation** - Isolated test instance in perimeter zone
- ✅ **Intrusion Prevention** - Suricata IPS rules for threat detection
- ✅ **Stateful Inspection** - Deep packet inspection with traffic context
- ✅ **Defense in Depth** - Multiple layers of security controls
- ✅ **Least Privilege** - IAM roles with minimal necessary permissions
- ✅ **Centralized Policy** - Reusable rule groups for consistent enforcement
- ✅ **Testing & Validation** - Verified controls before production deployment

## Firewall Rule Management

### Creating Effective Suricata Rules

**Rule Syntax:**
```
[action] [protocol] [source] [port] [direction] [destination] [port] ([options])
```

**Common Actions:**
- `drop` - Block and log the packet
- `reject` - Block and send reset/ICMP unreachable
- `alert` - Log but allow the packet
- `pass` - Allow without logging

**Best Practices:**
- Use specific content matches to reduce false positives
- Include meaningful message descriptions
- Assign unique signature IDs (sid)
- Classify threats appropriately
- Test rules in non-production first
- Document rule purpose and maintenance

## Advantages of AWS Network Firewall

✅ **Managed Service**
- AWS handles infrastructure and patching
- Automatic scaling and high availability
- No hardware to maintain

✅ **Flexible Rules**
- Suricata-compatible IPS rules
- Stateful and stateless rule support
- Domain list filtering

✅ **VPC Integration**
- Native AWS integration
- Works with existing VPC architecture
- Supports multiple availability zones

✅ **Logging & Monitoring**
- CloudWatch integration
- S3 log storage
- Flow logs and alert logs

## Common Use Cases

1. **Malware Protection** - Block known malicious domains and IPs
2. **Data Exfiltration Prevention** - Control outbound traffic
3. **Compliance Requirements** - Meet regulatory security standards
4. **Threat Intelligence** - Apply threat feeds as firewall rules
5. **Application Protection** - Filter traffic to specific applications
6. **Intrusion Prevention** - Detect and block attack patterns

## Troubleshooting

### Issue: Rules Not Blocking Traffic

**Possible Causes:**
- Rule group not attached to firewall policy
- Stateless rules not forwarding to stateful inspection
- Incorrect Suricata syntax
- Rule order issues

**Solutions:**
- Verify rule group attachment in firewall policy
- Check stateless default action configuration
- Validate Suricata rule syntax
- Review rule evaluation order

### Issue: Legitimate Traffic Blocked

**Possible Causes:**
- Overly broad content matches
- Incorrect source/destination networks
- False positive in IPS signature

**Solutions:**
- Narrow content matches to specific threats
- Use more precise network definitions
- Test rules against known good traffic
- Adjust rule severity or action

## Learning Outcomes

Through this lab, I gained hands-on experience with:
- Configuring AWS Network Firewall for malware protection
- Writing Suricata IPS rules for threat detection
- Understanding stateful vs stateless packet inspection
- Implementing network-level security controls
- Testing and validating firewall configurations
- Applying defense-in-depth security principles
- Managing firewall policies and rule groups
- Troubleshooting network security issues

## Prerequisites

- AWS Account with appropriate permissions
- Understanding of network security concepts
- Basic knowledge of VPC and EC2
- Familiarity with command-line interfaces
- Understanding of HTTP protocol

## Duration

Approximately 45 minutes

## Important Notes

⚠️ **Test Malware Files**
- The malware files used (`js_crypto_miner.html`, `java_jre17_exec.html`) are specifically created for anti-malware testing purposes
- These files are safe in the protected lab environment
- **DO NOT** use these files outside of this controlled environment

⚠️ **Production Considerations**
- Always test firewall rules in non-production first
- Monitor firewall logs for false positives
- Maintain documentation of all rules
- Regularly review and update threat intelligence
- Implement change management procedures

## Cost Optimization

In a production environment, consider:
- Right-sizing firewall capacity reservations
- Using rule groups efficiently (reusability)
- Monitoring and optimizing log retention
- Reviewing unused rule groups

## References

- [AWS Network Firewall Documentation](https://docs.aws.amazon.com/network-firewall/)
- [Suricata Rules Documentation](https://suricata.readthedocs.io/en/latest/rules/)
- [AWS VPC Security Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/security-best-practices.html)
- [AWS Network Firewall Pricing](https://aws.amazon.com/network-firewall/pricing/)

## Related Labs

- AWS WAF (Web Application Firewall) Configuration
- AWS Security Groups and NACLs
- AWS GuardDuty for Threat Detection
- VPC Flow Logs Analysis
- AWS Shield for DDoS Protection

## License

This is an educational lab project for learning AWS Network Firewall and network security concepts.

---

**Note**: This lab was completed as part of AWS security training. The environment and malware files are for controlled educational purposes only. Always follow your organization's security policies when implementing firewall rules in production environments.