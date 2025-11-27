# Software Management Lab

## Overview

Learn essential Linux package management skills using yum. You'll update packages, roll back changes, and install the AWS CLI—all critical skills for managing production Linux servers.

## What You'll Learn

- Update and upgrade Linux packages with yum
- Apply security updates to keep systems safe
- Roll back package updates when needed
- Install and configure the AWS CLI
- Manage package history and dependencies

## Duration

35 minutes

---

## Task 1: Connect to Your EC2 Instance

**Windows users:**
1. Download the `.ppk` file from Details → Show
2. Note the PublicIP address
3. Use PuTTY to connect ([PuTTY guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html))

**Mac/Linux users:**
```bash
cd ~/Downloads
chmod 400 labsuser.pem
ssh -i labsuser.pem ec2-user@<public-ip>
```

Type `yes` when prompted for first connection.

---

## Task 2: Update Your Linux Machine

### Step 1: Navigate to Working Directory

```bash
pwd  # Check current location
cd companyA  # If not already there
```

### Step 2: Check for Available Updates

```bash
sudo yum -y check-update
```

This queries repositories for all available package updates.

### Step 3: Apply Security Updates

```bash
sudo yum update --security
```

**Why this matters:** Security updates patch vulnerabilities. Always apply these first in production!

### Step 4: Upgrade All Packages

```bash
sudo yum -y upgrade
```

- `-y` flag automatically answers "yes" to prompts
- Updates all packages to latest versions
- May take a few minutes

**Note:** Your instance might already be up to date. That's fine—run the commands anyway for practice.

### Step 5: Install httpd and View History

```bash
sudo yum install httpd -y
```

This installs the Apache web server and shows you what's been updated on the system.

**What you'll see:**
- List of dependencies being installed
- Previous update history
- Current package versions

---

## Task 3: Roll Back a Package

Sometimes updates cause problems. Here's how to undo them.

### Step 1: View Package History

```bash
sudo yum history list
```

**Output example:**
```
ID  | Login user            | Date and time     | Action(s) | Altered
------------------------------------------------------------
2   | EC2 ... <ec2-user>    | Nov 27 14:30     | Install   | 9
1   | System <unset>        | Nov 27 12:00     | I, O, U   | 18
```

**Note the ID number** (usually 2) under the EC2 user—you'll need this!

### Step 2: View Details of Recent Changes

```bash
sudo yum history info 2
```

Replace `2` with your ID number from Step 1.

**What you'll see:**
- Transaction ID
- Time of installation
- User who made changes
- Command that was run
- List of packages affected

### Step 3: Undo the Transaction

```bash
sudo yum -y history undo 2
```

Replace `2` with your ID number.

**What happens:**
- Removes packages from transaction #2
- Shows all dependencies being removed
- Restores system to previous state

**Success!** The httpd package is now uninstalled.

---

## Task 4: Install the AWS CLI

The AWS Command Line Interface lets you manage AWS services from the terminal.

### Step 1: Verify Python is Installed

```bash
python3 --version
```

**Required:** Python 2.6.5+ or Python 3.3+

You should see something like: `Python 3.9.16`

### Step 2: Check for pip

```bash
pip3 --version
```

If you see "command not found," that's okay—we'll install AWS CLI without it.

### Step 3: Download AWS CLI Installer

```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

**What this does:**
- Downloads the AWS CLI v2 installer
- Saves it as `awscliv2.zip` in current directory

### Step 4: Unzip the Installer

```bash
unzip awscliv2.zip
```

Creates an `aws` directory with installation files.

### Step 5: Run the Installer

```bash
sudo ./aws/install
```

**This installs:**
- AWS CLI to `/usr/local/aws-cli`
- Creates symbolic link in `/usr/local/bin`

### Step 6: Verify Installation

```bash
aws help
```

You should see the AWS CLI help documentation.

**Press `q` to exit the help screen.**

---

## Task 5: Configure AWS CLI

Now let's connect the AWS CLI to your AWS account.

### Step 1: Get Your Credentials

1. Click **Details** (top of lab instructions)
2. Click **Show**
3. Next to **AWS CLI**, click **Show**
4. Copy the entire credentials section to a text editor:

```
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
aws_session_token=FwoGZXIvYXdzEBYaD...
```

### Step 2: Run AWS Configure

```bash
aws configure
```

**At the prompts:**
- AWS Access Key ID: *Leave blank, press Enter*
- AWS Secret Access Key: *Leave blank, press Enter*
- Default region name: `us-west-2` (press Enter)
- Default output format: `json` (press Enter)

### Step 3: Add Credentials to File

```bash
sudo nano ~/.aws/credentials
```

**Paste the entire credentials section** you copied in Step 1.

**Save and exit:**
1. Press `Ctrl + O` (save)
2. Press `Enter` (confirm filename)
3. Press `Ctrl + X` (exit)

### Step 4: Get Your Instance ID

1. Click **AWS** (top of instructions) to open AWS Console
2. Search for **EC2** and click it
3. Click **Instances (running)**
4. Find the **Command Host** instance
5. Copy the **Instance ID** (looks like `i-0123456789abcdef0`)

### Step 5: Test AWS CLI

```bash
aws ec2 describe-instance-attribute --instance-id i-YOUR-INSTANCE-ID --attribute instanceType
```

Replace `i-YOUR-INSTANCE-ID` with your actual instance ID.

**Expected output:**
```json
{
    "InstanceId": "i-0123456789abcdef0",
    "InstanceType": {
        "Value": "t3.micro"
    }
}
```

**Success!** Your AWS CLI is configured and working! 🎉

---

## Quick Reference

### Essential yum Commands

```bash
sudo yum check-update          # Check for updates
sudo yum update --security     # Apply security updates
sudo yum -y upgrade            # Upgrade all packages
sudo yum install <package>     # Install a package
sudo yum remove <package>      # Remove a package
sudo yum history list          # View package history
sudo yum history info <#>      # View transaction details
sudo yum history undo <#>      # Undo a transaction
```

### AWS CLI Basics

```bash
aws configure                  # Configure credentials
aws --version                  # Check AWS CLI version
aws help                       # View help documentation
aws <service> help             # Service-specific help
```

### Useful Flags

```bash
-y                 # Auto-answer yes to prompts
--security         # Only security-related updates
sudo               # Run as superuser (root)
```

---

## Common Issues & Fixes

**"Permission denied"**
```bash
# Add sudo before the command
sudo yum install httpd -y
```

**"No such file or directory" when unzipping**
```bash
# Make sure you're in the right directory
ls -l awscliv2.zip
# If not found, download again
```

**AWS CLI not found after install**
```bash
# Check if it's in the PATH
which aws
# If not found, try:
/usr/local/bin/aws --version
```

**"Unable to locate credentials" error**
```bash
# Verify credentials file exists
cat ~/.aws/credentials
# Make sure it contains your access keys
```

**Wrong transaction ID**
```bash
# List history again to get correct ID
sudo yum history list
# Use the number from the ID column
```

---

## Why This Matters

### Package Updates
- **Security patches** protect against vulnerabilities
- **Bug fixes** improve stability
- **New features** add functionality
- **Regular updates** are critical for production systems

### Rolling Back
- Not all updates work perfectly
- Some updates break compatibility
- Quick rollback minimizes downtime
- History tracking enables accountability

### AWS CLI
- Automate AWS tasks from command line
- Script infrastructure deployments
- Manage resources without GUI
- Essential for DevOps workflows

---

## Real-World Scenarios

**Scenario 1: Weekly Security Updates**
```bash
# Check for security updates
sudo yum check-update --security

# Apply them
sudo yum update --security -y

# Restart services if needed
sudo systemctl restart httpd
```

**Scenario 2: Package Broke Production**
```bash
# Find the problematic update
sudo yum history list

# Roll it back immediately
sudo yum history undo 5

# Verify services are working
sudo systemctl status httpd
```

**Scenario 3: Automate EC2 Management**
```bash
# List all running instances
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running"

# Stop development instances overnight
aws ec2 stop-instances --instance-ids i-1234567890abcdef0
```

---

## Best Practices

1. **Always test updates** in dev/staging before production
2. **Read release notes** before major upgrades
3. **Take snapshots** before significant changes
4. **Apply security updates** within 24-48 hours
5. **Keep AWS credentials secure** - never commit to git
6. **Use IAM roles** instead of access keys when possible
7. **Document changes** in the history with meaningful transaction IDs

---

## What's Next?

Now that you know package management and AWS CLI basics:

1. **Automate updates** with cron jobs
2. **Create AWS CLI scripts** for common tasks
3. **Set up monitoring** for package updates
4. **Practice disaster recovery** with snapshots
5. **Explore other AWS services** via CLI (S3, Lambda, RDS)

---

## Additional Resources

- [Red Hat yum documentation](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system_administrators_guide/ch-yum)
- [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/)
- [AWS CLI Configuration Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- [Package Management Best Practices](https://wiki.archlinux.org/title/System_maintenance)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025