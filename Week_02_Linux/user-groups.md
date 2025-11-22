# Managing Users and Groups Lab

## Overview

This lab teaches you fundamental system administration skills for managing user accounts and group memberships on Linux systems. You'll create multiple user accounts with specific roles, organize them into logical groups, and explore access control and privilege escalation mechanisms. These skills are essential for maintaining secure and organized multi-user systems in production environments.

## Learning Objectives

By completing this lab, you will be able to:

- Create new user accounts with default passwords using command-line tools
- Create user groups and organize users by role and department
- Assign users to multiple groups based on job responsibilities
- Switch between user accounts and understand file permissions
- Understand sudo privileges and access control mechanisms
- Review and interpret security logs for administrative actions

## Lab Duration

Approximately 45 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux EC2 instance
- Familiarity with basic Linux commands
- Understanding of file permissions concepts

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux with sudo privileges
- **SSH Connection**: Secure remote access to instance
- **Linux User Management**: System files (`/etc/passwd`, `/etc/group`, `/etc/sudoers`)
- **System Logging**: Security audit logs (`/var/log/secure`)

## Tasks Overview

### Task 1: Connect to Amazon Linux EC2 Instance via SSH

Establish a secure connection to your command host instance.

#### For Windows Users

1. Select **Details** > **Show** to open Credentials window
2. Download `labsuser.ppk` file and note the **PublicIP**
3. Open PuTTY and configure SSH session with the downloaded key
4. Connect to the instance

#### For macOS and Linux Users

1. Select **Details** > **Show** to open Credentials window
2. Download `labsuser.pem` file and note the **PublicIP**
3. Set up SSH connection:
   ```bash
   cd ~/Downloads
   chmod 400 labsuser.pem
   ssh -i labsuser.pem ec2-user@<public-ip>
   ```

### Task 2: Create Users

Create ten new user accounts with the following details and default password `P@ssword1234!`:

| First Name | Last Name | User ID | Job Role | Password |
|------------|-----------|---------|----------|----------|
| Alejandro | Rosalez | arosalez | Sales Manager | P@ssword1234! |
| Efua | Owusu | eowusu | Shipping | P@ssword1234! |
| Jane | Doe | jdoe | Shipping | P@ssword1234! |
| Li | Juan | ljuan | HR Manager | P@ssword1234! |
| Mary | Major | mmajor | Finance Manager | P@ssword1234! |
| Mateo | Jackson | mjackson | CEO | P@ssword1234! |
| Nikki | Wolf | nwolf | Sales Representative | P@ssword1234! |
| Paulo | Santos | psantos | Shipping | P@ssword1234! |
| Sofia | Martinez | smartinez | HR Specialist | P@ssword1234! |
| Saanvi | Sarkar | ssarkar | Finance Specialist | P@ssword1234! |

#### Creating User Accounts

Verify you're in the home directory:
```bash
pwd
# Output: /home/ec2-user
```

Create the first user (Alejandro Rosalez):
```bash
sudo useradd arosalez
sudo passwd arosalez
# Enter password twice: P@ssword1234!
# Note: Password input is hidden (no characters display)
```

Verify user creation:
```bash
sudo cat /etc/passwd | cut -d: -f1
# Shows all usernames including arosalez
```

Create remaining users using the same commands with each User ID from the table above:
```bash
sudo useradd <User ID>
sudo passwd <User ID>
```

Verify all users were created:
```bash
sudo cat /etc/passwd | cut -d: -f1
# Should display all 10 new users plus ec2-user
```

#### Command Explanation

**useradd**: Creates a new user account with system defaults
- **sudo**: Runs command with administrator privileges (root)
- User ID: Unique login name for the account

**passwd**: Sets or changes a user's password
- Prompts twice for security confirmation
- Display is hidden while typing for security

**cat /etc/passwd | cut -d: -f1**: Displays only usernames
- **cat**: Displays file contents
- **|**: Pipes output to next command
- **cut -d: -f1**: Extracts first field using colon as delimiter

### Task 3: Create Groups

Create seven groups to organize users by department and role:

- Sales
- HR
- Finance
- Shipping
- Managers
- CEO
- Personnel

#### Creating Groups

Verify you're in the home directory:
```bash
pwd
```

Create the first group (Sales):
```bash
sudo groupadd Sales
```

Verify group creation:
```bash
cat /etc/group
# Shows Sales:x:1014: (GID may vary)
```

Create remaining groups:
```bash
sudo groupadd HR
sudo groupadd Finance
sudo groupadd Shipping
sudo groupadd Managers
sudo groupadd CEO
sudo groupadd Personnel
```

Verify all groups were created:
```bash
cat /etc/group
# Should display all 7 new groups
```

#### Assigning Users to Groups

Add first user (arosalez) to Sales group:
```bash
sudo usermod -a -G Sales arosalez
```

Verify user was added to group:
```bash
cat /etc/group
# Sales:x:1014:arosalez
```

Add remaining users to their appropriate groups using the assignment table:

| Group | Users |
|-------|-------|
| Sales | arosalez, nwolf |
| HR | ljuan, smartinez |
| Finance | mmajor, ssarkar |
| Shipping | eowusu, jdoe, psantos |
| Managers | arosalez, ljuan, mmajor |
| CEO | mjackson |
| Personnel | (all employees) |

**Command format**:
```bash
sudo usermod -a -G <Group> <User ID>
```

**Example**:
```bash
sudo usermod -a -G Sales nwolf
sudo usermod -a -G HR ljuan
# ... continue for all users
```

Add ec2-user to all groups:
```bash
sudo usermod -a -G Sales ec2-user
sudo usermod -a -G HR ec2-user
sudo usermod -a -G Finance ec2-user
sudo usermod -a -G Shipping ec2-user
sudo usermod -a -G Managers ec2-user
sudo usermod -a -G CEO ec2-user
sudo usermod -a -G Personnel ec2-user
```

Verify all group memberships:
```bash
sudo cat /etc/group
```

Expected output shows all users assigned to their groups:
```
Sales:x:1014:arosalez,nwolf,ec2-user
HR:x:1015:ljuan,smartinez,ec2-user
Finance:x:1016:mmajor,ssarkar,ec2-user
Shipping:x:1017:eowusu,jdoe,psantos,ec2-user
Managers:x:1018:arosalez,ljuan,mmajor,ec2-user
CEO:x:1019:mjackson,ec2-user
Personnel:x:1020:...all employees...
```

#### Command Explanation

**groupadd**: Creates a new group
- Groups organize users for permission and resource management
- GID (Group ID) is automatically assigned

**usermod -a -G**: Adds user to supplementary groups
- **-a**: Append (don't remove existing group memberships)
- **-G**: Specifies supplementary groups
- Users can belong to multiple groups simultaneously

### Task 4: Log In Using New Users

Test user accounts and understand access control and sudo privileges.

#### Switching Users

Switch to the arosalez account:
```bash
su arosalez
# Enter password: P@ssword1234!
```

Verify current user and location:
```bash
pwd
# Shows: /home/ec2-user (inherited from previous session)
```

#### Testing File Permissions

Attempt to create a file in ec2-user's home directory:
```bash
touch myFile.txt
# Error: Permission denied
```

**Why it failed**: User arosalez does not have write permissions to the /home/ec2-user directory.

Attempt with sudo privilege escalation:
```bash
sudo touch myFile.txt
# Error: arosalez is not in the sudoers file. This incident will be reported.
```

**Why it failed**: arosalez is not in the sudoers file and cannot execute administrative commands.

#### Understanding Sudoers

The sudoers file controls which users can execute commands with root privileges. Only authorized users should have this access for security reasons.

#### Examining Security Logs

Exit to return to ec2-user:
```bash
exit
```

View security logs to see the unauthorized sudo attempt:
```bash
sudo cat /var/log/secure
```

Scroll to the bottom to find entries similar to:
```
Aug  9 14:45:55 ip-10-0-10-217 sudo: arosalez : user NOT in sudoers ; TTY=pts/1 ; PWD=/home/ec2-user ; USER=root ; COMMAND=/bin/touch myFile.txt
```

#### Log Information Breakdown

- **Date/Time**: When the attempt occurred
- **Host**: System where attempt occurred (ip-10-0-10-217)
- **User**: arosalez (attempted)
- **Status**: user NOT in sudoers (denied)
- **TTY**: Terminal type (pts/1)
- **PWD**: Current working directory
- **USER**: Requested privilege level (root)
- **COMMAND**: Command that was attempted

## Key Concepts Covered

### User Accounts
Individual login credentials that represent a person or service on the system. Each user has a unique User ID (UID) and home directory.

### Groups
Collections of users that can be assigned permissions collectively. Users can belong to multiple groups simultaneously, enabling flexible permission management.

### /etc/passwd File
System file containing user account information:
- Username
- Password placeholder (x = stored in /etc/shadow)
- UID
- GID
- User info/comment field
- Home directory
- Login shell

### /etc/group File
System file containing group information:
- Group name
- Password placeholder (usually x)
- GID (Group ID)
- Member list (comma-separated usernames)

### /etc/sudoers File
Configuration file controlling sudo privileges. Defines which users can execute commands as root or other users.

### Sudo (Super User Do)
Mechanism allowing authorized users to execute commands with root (administrator) privileges. All sudo attempts are logged in `/var/log/secure`.

### File Permissions
Unix-based systems use permissions (read, write, execute) for user, group, and others to control file access.

### Security Logging
System logs administrative actions for audit trails. `/var/log/secure` records authentication and authorization events.

## Essential Commands Reference

| Command | Purpose |
|---------|---------|
| `sudo useradd <user>` | Create new user account |
| `sudo passwd <user>` | Set user password |
| `sudo groupadd <group>` | Create new group |
| `sudo usermod -a -G <group> <user>` | Add user to group |
| `cat /etc/passwd` | View all users |
| `cat /etc/group` | View all groups |
| `su <user>` | Switch to different user |
| `sudo cat /var/log/secure` | View security logs |
| `id <user>` | Show user and group IDs |
| `whoami` | Display current user |

## Troubleshooting Tips

- **Password Entry Hidden**: Normal behavior; type password and press Enter
- **Permission Denied**: User doesn't have write permission to directory
- **Not in sudoers**: User is not authorized for sudo; only root can add users to sudoers
- **Group Not Found**: Verify group name spelling with `cat /etc/group`
- **User Not Found**: Verify user ID spelling with `cat /etc/passwd`
- **Cannot Switch User**: Verify password is correct and user exists

## Important Notes

- This lab builds on knowledge from previous AWS and Linux courseware
- Password policy typically requires special characters, numbers, and uppercase
- Default password `P@ssword1234!` should be changed after first login in production
- AWS service access is restricted to lab requirements
- User IDs must be spelled correctly for default credential login
- Managers belong to multiple groups (note the distinction from personnel)

## Best Practices

- **Security**: Change default passwords at first login
- **Organization**: Use meaningful group names reflecting departments/roles
- **Documentation**: Maintain records of users and group assignments
- **Least Privilege**: Only grant sudo access to users who need it
- **Auditing**: Regularly review logs for unauthorized access attempts
- **Multiple Groups**: Assign users to multiple groups for flexible permissions

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **File Permissions**: Deep dive into chmod and chown commands
- **Sudoers Configuration**: Granting selective sudo privileges
- **Home Directories**: Creating and managing user home directory structures
- **Shell Environments**: Customizing user shell configurations
- **User Quotas**: Limiting disk space per user
- **Account Expiration**: Setting password and account expiration policies
- **SSH Key Management**: Alternative authentication methods
- **SELinux/AppArmor**: Advanced access control mechanisms
- **Log Analysis**: Advanced security log review and monitoring
- **User Provisioning**: Automation and scripting for user creation

## Related Labs

- Introduction to Amazon EC2
- Introduction to Amazon Linux AMI
- Linux Command Line

## Resources

- [Linux User and Group Management](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_basic_system_settings/managing-users-and-groups_configuring-basic-system-settings)
- [Sudo Manual Page](https://linux.die.net/man/8/sudo)
- [Linux /etc/passwd Format](https://linux.die.net/man/5/passwd)
- [Linux /etc/group Format](https://linux.die.net/man/5/group)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025

**Related Labs**: Introduction to Amazon EC2, Introduction to Amazon Linux AMI, Linux Command Line