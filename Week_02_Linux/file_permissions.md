# Managing File Permissions Lab

## Overview

This lab teaches you critical Linux security and access control skills through hands-on management of file and directory permissions. You'll learn how to assign ownership to users and groups, modify permission modes using both symbolic and numeric notation, and implement proper access control for organizational structures. These skills are fundamental for securing systems, managing multi-user environments, and maintaining proper data access boundaries in production environments.

## Learning Objectives

By completing this lab, you will be able to:

- Change file and folder ownership using chown command
- Modify group ownership for directories and files
- Apply recursive ownership changes to directory structures
- Use chmod in both symbolic and absolute (numeric) modes
- Understand read, write, and execute permissions
- Assign appropriate permissions based on organizational roles
- Verify permission changes with ls -l and ls -laR commands

## Lab Duration

Approximately 35 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux EC2 instance
- Familiarity with Linux users and groups
- Understanding of directory navigation and file operations
- Knowledge from "Managing Users and Groups" lab

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux with sudo privileges
- **SSH Connection**: Secure remote access to instance
- **Pre-existing Users**: Multiple users representing different organizational roles
- **Pre-existing Groups**: Personnel, HR, Finance, Shipping, Sales, CEO
- **Directory Structure**: CompanyA folder with departmental subdirectories

### Pre-existing Folder Structure

```
/home/ec2-user/companyA/
├── Documents/
├── Employees/
├── HR/
│   └── Finance/
├── Management/
├── Sales/
├── SharedFolders/
├── Shipping/
└── Roster.csv
```

### User Roles
- **mjackson**: CEO
- **ljuan**: HR Manager
- **mmajor**: Finance Manager
- **eowusu**: Shipping Manager
- **nwolf**: Sales Manager

## Tasks Overview

### Task 1: Connect to Amazon Linux EC2 Instance via SSH

Establish a secure connection to your Command Host instance.

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

### Task 2: Change File and Folder Ownership

Assign proper ownership to directories based on organizational hierarchy.

#### Verify Location

Confirm you're in the correct directory:
```bash
pwd
# Expected output: /home/ec2-user/companyA
# If not, navigate there: cd companyA
```

#### Change CompanyA Folder Ownership

Assign the entire companyA folder to CEO with Personnel group ownership:
```bash
sudo chown -R mjackson:Personnel /home/ec2-user/companyA
```

**Command breakdown**:
- `sudo`: Execute with root privileges
- `chown`: Change ownership command
- `-R`: Recursive (apply to all subdirectories and files)
- `mjackson`: New owner (CEO user)
- `:Personnel`: New group owner
- `/home/ec2-user/companyA`: Target directory path

#### Change HR Folder Ownership

Assign HR folder to HR manager with HR group ownership:
```bash
sudo chown -R ljuan:HR HR
```

This gives the HR manager (ljuan) ownership of the HR directory and assigns it to the HR group.

#### Change Finance Folder Ownership

Assign Finance folder (inside HR) to Finance manager:
```bash
sudo chown -R mmajor:Finance HR/Finance
```

Note the nested path: Finance folder is located inside the HR directory.

#### Verify Ownership Changes

View the complete directory structure with ownership information:
```bash
ls -laR
```

This displays:
- File and directory permissions (drwxr-xr-x)
- Owner (mjackson, ljuan, mmajor)
- Group (Personnel, HR, Finance)
- File sizes and timestamps
- All subdirectories recursively

### Task 3: Change Permission Modes

Learn both symbolic and absolute (numeric) modes for changing file permissions.

#### Verify Location

```bash
pwd
# Expected output: /home/ec2-user/companyA
```

#### Symbolic Mode Example

Create a file using vim:
```bash
sudo vi symbolic_mode_file
```

Press `ESC`, then type `:wq` and press Enter to save and exit.

Change permissions using symbolic notation:
```bash
sudo chmod g+w symbolic_mode_file
```

**Command breakdown**:
- `chmod`: Change mode (permissions)
- `g`: Group
- `+`: Add permission
- `w`: Write permission

**Result**: Group members can now write to the file.

#### Absolute (Numeric) Mode Example

Create another file:
```bash
sudo vi absolute_mode_file
```

Press `ESC`, then type `:wq` and press Enter to save and exit.

Change permissions using numeric notation:
```bash
sudo chmod 764 absolute_mode_file
```

**Numeric breakdown**:
- `7` (User/Owner): read(4) + write(2) + execute(1) = 7 (all permissions)
- `6` (Group): read(4) + write(2) = 6 (read and write)
- `4` (Others): read(4) = 4 (read only)

**Result**: Owner has full permissions, group can read/write, others can only read.

#### Verify Permission Changes

List files with detailed permissions:
```bash
ls -l
```

Expected output:
```
-rw-rw-r-- 1 root Personnel 0 Aug 10 14:30 symbolic_mode_file
-rwxrw-r-- 1 root Personnel 0 Aug 10 14:31 absolute_mode_file
```

### Task 4: Assign Permissions

Apply ownership changes to Shipping and Sales departments.

#### Verify Location

```bash
pwd
# Expected output: /home/ec2-user/companyA
```

#### Change Shipping Folder Ownership

Assign Shipping folder to shipping manager:
```bash
sudo chown -R eowusu:Shipping Shipping
```

Verify the change:
```bash
ls -laR Shipping
```

#### Change Sales Folder Ownership

Assign Sales folder to sales manager:
```bash
sudo chown -R nwolf:Sales Sales
```

Verify the change:
```bash
ls -laR Sales
```

**Result**: Each department folder is now owned by its respective manager with appropriate group ownership, enabling proper access control and collaboration within departments.

## Key Concepts Covered

### File Ownership
Every file and directory in Linux has two ownership attributes:
- **User (Owner)**: Individual user who owns the file
- **Group**: Group that owns the file

### File Permissions
Three types of permissions exist for three categories of users:

**Permission Types**:
- **r (read)**: View file contents or list directory contents
- **w (write)**: Modify file or create/delete files in directory
- **x (execute)**: Run file as program or enter directory

**User Categories**:
- **User (u)**: File owner
- **Group (g)**: Members of the file's group
- **Others (o)**: All other users
- **All (a)**: All three categories

### Permission Representation

**Symbolic notation**:
```
-rwxrw-r--
│││││││││└─ Others: read only
││││││││└── Others: no write
│││││││└─── Others: no execute
││││││└──── Group: read
│││││└───── Group: write
││││└────── Group: no execute
│││└─────── User: read
││└──────── User: write
│└───────── User: execute
└────────── File type (- = file, d = directory)
```

**Numeric notation**:
- 4 = read (r)
- 2 = write (w)
- 1 = execute (x)
- 0 = no permission (-)

Combine values: 7 = rwx (4+2+1), 6 = rw- (4+2), 5 = r-x (4+1)

### Chown Command
Changes user and/or group ownership of files and directories.

**Syntax options**:
```bash
chown user file           # Change owner only
chown user:group file     # Change owner and group
chown :group file         # Change group only
chown -R user:group dir/  # Recursive change
```

### Chmod Command
Changes permission modes (read, write, execute) for files and directories.

**Two modes**:
1. **Symbolic**: Uses letters (u, g, o, a) and symbols (+, -, =)
2. **Absolute**: Uses three-digit octal numbers (0-7)

## Essential Commands Reference

### Ownership Commands

| Command | Purpose |
|---------|---------|
| `chown user file` | Change file owner |
| `chown user:group file` | Change owner and group |
| `chown :group file` | Change group only |
| `chown -R user:group dir/` | Change ownership recursively |
| `chgrp group file` | Change group ownership only |

### Permission Commands - Symbolic Mode

| Command | Purpose |
|---------|---------|
| `chmod u+x file` | Add execute for user |
| `chmod g+w file` | Add write for group |
| `chmod o-r file` | Remove read for others |
| `chmod a+r file` | Add read for all |
| `chmod u=rwx file` | Set user to rwx exactly |
| `chmod go-w file` | Remove write from group and others |
| `chmod u+x,g+w file` | Multiple changes |

### Permission Commands - Absolute Mode

| Command | Permissions | Result |
|---------|-------------|--------|
| `chmod 777 file` | rwxrwxrwx | All permissions for everyone |
| `chmod 755 file` | rwxr-xr-x | Standard for executables |
| `chmod 644 file` | rw-r--r-- | Standard for files |
| `chmod 600 file` | rw------- | Owner only |
| `chmod 700 file` | rwx------ | Owner full access only |
| `chmod 664 file` | rw-rw-r-- | Group collaborative file |

### Viewing Permissions

| Command | Purpose |
|---------|---------|
| `ls -l` | List with permissions |
| `ls -la` | List all files with permissions |
| `ls -laR` | Recursive listing with permissions |
| `stat file` | Detailed file information |

## Common Permission Numbers

| Number | Permissions | Symbolic | Typical Use |
|--------|-------------|----------|-------------|
| 777 | rwxrwxrwx | Full access for all | Avoid (security risk) |
| 755 | rwxr-xr-x | Owner full, others read/execute | Executables, directories |
| 750 | rwxr-x--- | Owner full, group read/execute | Restricted directories |
| 700 | rwx------ | Owner only | Private directories |
| 666 | rw-rw-rw- | All can read/write | Avoid (security risk) |
| 664 | rw-rw-r-- | Owner/group write, others read | Shared files |
| 644 | rw-r--r-- | Owner write, all read | Regular files |
| 600 | rw------- | Owner only | Private files, SSH keys |
| 444 | r--r--r-- | Read-only for all | Protected files |
| 400 | r-------- | Owner read only | Highly sensitive files |

## Symbolic Mode Examples

### Adding Permissions
```bash
chmod u+x file.sh        # Add execute for user
chmod g+w document.txt   # Add write for group
chmod o+r public.txt     # Add read for others
chmod a+x script.sh      # Add execute for all
```

### Removing Permissions
```bash
chmod u-x file.sh        # Remove execute from user
chmod g-w document.txt   # Remove write from group
chmod o-r private.txt    # Remove read from others
chmod a-w readonly.txt   # Remove write from all
```

### Setting Exact Permissions
```bash
chmod u=rwx file         # User: exactly rwx
chmod g=rx file          # Group: exactly r-x
chmod o= file            # Others: no permissions
chmod u=rw,g=r,o= file   # All at once
```

### Multiple Changes
```bash
chmod u+x,g+w file       # Add execute to user, write to group
chmod u-w,g-w file       # Remove write from user and group
chmod ug+rw file         # Add read/write to user and group
```

## Practical Permission Scenarios

### Scenario 1: Shared Project Directory
```bash
# Create directory owned by project group
sudo mkdir /shared/project
sudo chown :developers /shared/project
sudo chmod 770 /shared/project
# Team can collaborate, others cannot access
```

### Scenario 2: Public Documentation
```bash
# Files readable by all, writable by owner
sudo chmod 644 documentation.txt
sudo chmod 755 /var/www/html/docs/
```

### Scenario 3: Private User Files
```bash
# Only owner can access
chmod 700 ~/private/
chmod 600 ~/.ssh/id_rsa
```

### Scenario 4: Web Server Files
```bash
# Typical web server permissions
sudo chown www-data:www-data /var/www/html/ -R
sudo chmod 755 /var/www/html/ -R
sudo chmod 644 /var/www/html/*.html
```

## Troubleshooting Tips

- **Permission denied**: Need sudo for files owned by other users
- **Cannot change ownership**: Only root can change file ownership
- **Changes don't apply**: Verify you're using correct path and -R for directories
- **Lost permissions**: Use `chmod 644` as safe default for files
- **Directory not accessible**: Directories need execute (x) permission to be entered
- **Scripts won't run**: Add execute permission with `chmod +x script.sh`

## Important Notes

- This lab builds on "Managing Users and Groups" lab
- Only root (via sudo) can change file ownership
- Users can only change permissions on files they own
- The `-R` flag applies changes recursively to all subdirectories
- Be cautious with 777 permissions—major security risk
- Execute permission on directories means ability to enter them
- Group ownership enables team collaboration

## Best Practices

### Security Considerations
- **Principle of Least Privilege**: Grant minimum necessary permissions
- **Avoid 777**: Never use full permissions for all users
- **Protect Private Keys**: Always use 600 for SSH private keys
- **Audit Regularly**: Review permissions periodically
- **Use Groups**: Leverage groups for team-based access control
- **Sensitive Data**: Use 600 or 400 for sensitive files

### Organization Standards
- **Consistent Permissions**: Establish standard permission schemes
- **Document Policies**: Maintain permission documentation
- **Regular Reviews**: Audit ownership and permissions quarterly
- **Training**: Ensure team understands permission model
- **Automation**: Use scripts for consistent permission application

### Common Permission Patterns
```bash
# Directories
755 - Public directories
750 - Team directories
700 - Private directories

# Files
644 - Public readable files
640 - Team readable files
600 - Private files

# Executables
755 - Public scripts/programs
750 - Team scripts/programs
700 - Private scripts/programs
```

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting (Command Host instance)
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **Access Control Lists (ACL)**: Fine-grained permissions with setfacl/getfacl
- **Special Permissions**: Setuid, setgid, and sticky bit
- **SELinux/AppArmor**: Mandatory access control systems
- **Umask**: Default permission masks for new files
- **File Attributes**: Immutable and append-only attributes with chattr
- **Sudo Configuration**: Granular privilege escalation
- **Permission Auditing**: Using find to locate insecure permissions
- **Capability-based Security**: Linux capabilities system
- **File System ACLs**: Extended attributes and permissions
- **Security Scanning**: Automated permission compliance checking

## Practice Exercises

To reinforce your learning:

1. **Create collaborative directory** where group members can create/edit files
2. **Set up web server permissions** for a static website directory
3. **Secure sensitive files** like configuration files with passwords
4. **Find insecure files** using `find / -perm -002 2>/dev/null`
5. **Create permission script** to standardize permissions across projects
6. **Implement least privilege** for a multi-user application directory
7. **Fix permission issues** by diagnosing and correcting access problems

## Related Labs

- Introduction to Amazon EC2
- Introduction to Amazon Linux AMI
- Linux Command Line
- Managing Users and Groups
- Editing Files
- Working with the File System
- Working with Files

## Resources

- [Linux File Permissions Explained](https://www.redhat.com/sysadmin/linux-file-permissions-explained)
- [chmod Manual Page](https://linux.die.net/man/1/chmod)
- [chown Manual Page](https://linux.die.net/man/1/chown)
- [Linux Security Best Practices](https://www.cyberciti.biz/tips/linux-security.html)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025

**Related Labs**: Introduction to Amazon EC2, Introduction to Amazon Linux AMI, Linux Command Line, Managing Users and Groups, Editing Files, Working with the File System, Working with Files