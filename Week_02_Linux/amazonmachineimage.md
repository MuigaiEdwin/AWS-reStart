# Introduction to Amazon Linux Amazon Machine Image (AMI) Lab

## Overview

This lab introduces you to the fundamentals of interacting with Amazon Linux through command-line interface (CLI) operations. You'll gain hands-on experience using SSH to access an EC2 instance and explore the Linux manual pages system—essential skills for managing cloud infrastructure.

Amazon Linux is a Linux distribution optimized for use on Amazon EC2, providing a secure, stable, and high-performance execution environment. This lab builds a solid foundation for learning Linux commands and system administration within AWS.

## Learning Objectives

By completing this lab, you will be able to:

- Use SSH (Secure Shell) to connect to an Amazon Linux EC2 instance
- Understand the purpose and structure of Linux man pages
- Navigate and search within the man page system
- Identify and examine key man page sections and headers
- Establish secure remote connections to cloud instances

## Lab Duration

Approximately 30 minutes

## Prerequisites

- AWS account access with lab environment setup
- SSH client (built-in on macOS/Linux; PuTTY required for Windows)
- Basic understanding of terminal/command-line concepts
- Text editor for key file management (if needed)

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux (in public subnet)
- **Amazon VPC**: Isolated virtual private cloud with public subnet
- **Security Group**: Preconfigured to allow SSH access
- **Key Pair**: labsuser.pem (macOS/Linux) or labsuser.ppk (Windows)

## Tasks Overview

### Task 1: Connect to Amazon Linux EC2 Instance via SSH

Establish a secure connection to the command host instance.

#### For Windows Users

1. Download the key pair file:
   - Select **Details** dropdown above instructions
   - Choose **Show** to open Credentials window
   - Click **Download PPK** to save `labsuser.ppk`
   - Note the **PublicIP** address

2. Configure and launch PuTTY:
   - Download [PuTTY](https://www.putty.org/) if not already installed
   - Open `putty.exe`
   - Follow PuTTY SSH configuration steps
   - Use the saved `.ppk` file for authentication

#### For macOS and Linux Users

1. Download the key pair file:
   - Select **Details** dropdown above instructions
   - Choose **Show** to open Credentials window
   - Click **Download PEM** to save `labsuser.pem`
   - Note the **PublicIP** address

2. Establish SSH connection:
   ```bash
   cd ~/Downloads  # Or location where labsuser.pem was saved
   chmod 400 labsuser.pem
   ssh -i labsuser.pem ec2-user@<public-ip>
   ```

3. Accept the remote server connection when prompted with "yes"

**Note**: No password will be requested since key-pair authentication is used.

### Task 2: Explore Linux Man Pages

Discover and navigate the Linux manual pages system—the standard help documentation for commands and system functions.

#### Opening Man Pages

Enter the command to view the manual for the man command itself:
```bash
man man
```

#### Understanding Man Page Structure

Man pages contain standardized sections with important headers:

- **NAME**: Brief description of the command
- **SYNOPSIS**: Command syntax and usage format
- **DESCRIPTION**: Detailed explanation of the command's functionality
- **OVERVIEW**: High-level purpose and context
- **OPTIONS**: Available command-line flags and parameters
- **EXAMPLES**: Sample usage scenarios
- **FILES**: Related system files
- **SEE ALSO**: Cross-references to related commands

#### Navigation Tips

- **Move Up/Down**: Use arrow keys to scroll through pages
- **Search**: Press `/` followed by search term to find text within the page
- **Next Match**: Press `n` to find next occurrence
- **Previous Match**: Press `N` to find previous occurrence
- **Exit**: Press `q` to quit and return to prompt

#### Examining Section Numbers

Pay close attention to the DESCRIPTION section, which identifies different man page categories by section number:

- Section 1: User commands
- Section 2: System calls
- Section 3: Library functions
- Section 5: File formats
- Section 8: System administration commands

## Key Concepts Covered

### Secure Shell (SSH)
SSH is a cryptographic network protocol that provides secure remote access to systems. It uses public-key cryptography for authentication and encrypted communication channels.

### Public Key Infrastructure (PKI)
Uses a pair of mathematically-linked keys:
- **Private Key**: Kept secure on your local machine; never shared
- **Public Key**: Installed on the remote server; used to verify your identity

### Linux Manual Pages
Comprehensive documentation system built into Linux. Access man pages for any installed command or system function for detailed reference documentation.

### Amazon Linux
AWS-optimized Linux distribution that provides automatic security updates, long-term support, and integration with AWS services.

## Troubleshooting Tips

- **Lab Timeout**: Click "Start Lab" again to extend the lab session timer
- **Pop-up Blocked**: Enable pop-ups in browser settings to open AWS Management Console
- **SSH Connection Refused**: Verify the correct public IP address and key file
- **Permission Denied**: Ensure key file permissions are set to 400 with `chmod 400 labsuser.pem`
- **PuTTY Connection Issues**: Verify the instance is running and security group allows SSH (port 22)
- **Man Pages Not Found**: Command might not have a man page; try `command --help` instead

## Important Notes

- This lab environment has restricted AWS service access to prevent accidental costs
- The EC2 instance is in a public subnet with proper security group configuration
- SSH (port 22) is the primary access method for this lab
- Key pair files should be kept secure and never shared
- Lab resources are temporary and will be cleaned up automatically

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting
- **Amazon VPC**: Virtual private cloud networking
- **AWS IAM**: Identity and access management (key pairs)
- **AWS Management Console**: Service management interface

## Linux Commands Reference

Common commands useful after connecting:

```bash
# Display current directory
pwd

# List directory contents
ls -la

# View system information
uname -a

# Check disk usage
df -h

# Display current user
whoami

# View command help
man <command>          # Full manual
command --help         # Quick help
```

## Next Steps

After completing this lab, explore:

- **Advanced Linux Administration**: User management, permissions, file systems
- **Scripting**: Bash scripting and automation
- **System Monitoring**: Tools like `top`, `ps`, `netstat`
- **Package Management**: Using `yum` to install and manage software
- **Log Management**: Viewing and analyzing system logs
- **AWS CLI**: Command-line interface for AWS services
- **Infrastructure as Code**: Automating EC2 deployment with Terraform or CloudFormation

## Resources

- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)
- [SSH/PuTTY Connection Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)
- [Linux Man Pages Online](https://man7.org/linux/man-pages/)
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025