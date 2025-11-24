# Working with Files Lab

## Overview

This lab teaches you essential file archiving and backup management skills using the tar command—one of the most important tools for system administration and data management. You'll create compressed backups of directory structures, maintain backup logs with timestamps, and transfer archives between locations. These skills are fundamental for disaster recovery, data migration, and system maintenance in production environments.

## Learning Objectives

By completing this lab, you will be able to:

- Create compressed backup archives using tar with gzip compression
- Understand tar command options and flags
- Log backup operations with date, time, and filename information
- Use echo and tee commands to write to files and terminal simultaneously
- Transfer backup files between directories
- Verify archive creation and file transfers

## Lab Duration

Approximately 30 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux EC2 instance
- Familiarity with directory navigation and file operations
- Understanding of file system hierarchy

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux
- **SSH Connection**: Secure remote access to instance
- **Pre-existing Directory Structure**: CompanyA folder with subdirectories and files
- **Tar Utility**: Built-in archiving tool for creating compressed backups

### Pre-existing Folder Structure

```
/home/ec2-user/CompanyA/
├── Employees/
│   └── Schedules.csv
├── Finance/
│   └── Salary.csv
├── HR/
│   ├── Assessments.csv
│   └── Managers.csv
├── IA/
├── Management/
│   ├── Promotions.csv
│   └── Sections.csv
└── SharedFolders/
```

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

### Task 2: Create a Backup

Create a compressed archive of the entire CompanyA directory structure.

#### Verify Location and Structure

Confirm you're in the correct directory:
```bash
pwd
# Expected output: /home/ec2-user
```

Verify the CompanyA folder exists and view its structure:
```bash
ls -R CompanyA
```

Expected output:
```
CompanyA/:
Employees  Finance  HR  IA  Management  SharedFolders

CompanyA/Employees:
Schedules.csv

CompanyA/Finance:
Salary.csv

CompanyA/HR:
Assessments.csv  Managers.csv

CompanyA/IA:

CompanyA/Management:
Promotions.csv  Sections.csv
```

#### Create Compressed Backup

Create a compressed tar archive of the entire CompanyA folder:
```bash
tar -csvpzf backup.CompanyA.tar.gz CompanyA
```

**Command breakdown**:
- `tar`: Tape archive utility
- `-c`: Create new archive
- `-s`: Sort files by name
- `-v`: Verbose output (show files being archived)
- `-p`: Preserve permissions and ownership
- `-z`: Compress with gzip
- `-f`: Specify filename
- `backup.CompanyA.tar.gz`: Output archive filename
- `CompanyA`: Directory to archive

Expected output shows all files being added to archive:
```
CompanyA/
CompanyA/Management/
CompanyA/Management/Sections.csv
CompanyA/Management/Promotions.csv
CompanyA/Employees/
CompanyA/Employees/Schedules.csv
CompanyA/Finance/
CompanyA/Finance/Salary.csv
CompanyA/HR/
CompanyA/HR/Managers.csv
CompanyA/HR/Assessments.csv
CompanyA/IA/
CompanyA/SharedFolders/
```

#### Verify Archive Creation

Confirm the backup file was created:
```bash
ls
# Output: backup.CompanyA.tar.gz  CompanyA
```

The `backup.CompanyA.tar.gz` file contains all folders and files from CompanyA. You can copy it to another location or host and extract it to restore the entire directory structure.

### Task 3: Log the Backup

Create a log file to track backup operations with timestamps.

#### Navigate to CompanyA Directory

Change to the CompanyA folder:
```bash
cd /home/ec2-user/CompanyA
```

#### Create Empty Log File

Create an empty CSV file for backup logs:
```bash
touch SharedFolders/backups.csv
```

#### Add Log Entry

Write backup information to the log file:
```bash
echo "25 Aug 25 2021, 16:59, backup.CompanyA.tar.gz" | sudo tee SharedFolders/backups.csv
```

Expected output:
```
25 Aug 25 2021, 16:59, backup.CompanyA.tar.gz
```

**Command breakdown**:
- `echo`: Prints text to standard output
- `"..."`: Text string with date, time, and filename
- `|`: Pipe redirector (sends output of first command to second)
- `sudo tee`: Writes to both terminal and file simultaneously
- `SharedFolders/backups.csv`: Target log file

**Why use tee?** The `tee` command allows you to see the output in the terminal while simultaneously writing it to a file—useful for verification and logging.

#### Verify Log Entry

Display the contents of the log file:
```bash
cat SharedFolders/backups.csv
```

Expected output:
```
25 Aug 25 2021, 16:59, backup.CompanyA.tar.gz
```

### Task 4: Move the Backup File

Transfer the backup archive to another directory for access control or organization purposes.

#### Verify Current Location

Confirm you're in the CompanyA directory:
```bash
pwd
# Output: /home/ec2-user/CompanyA
```

#### Move Backup to IA Folder

Transfer the backup file from the parent directory to the IA folder:
```bash
mv ../backup.CompanyA.tar.gz IA/
```

**Path explanation**:
- `../`: Refers to parent directory (/home/ec2-user)
- `backup.CompanyA.tar.gz`: Backup file in parent directory
- `IA/`: Target destination (subdirectory of current location)

#### Verify File Transfer

List contents of both current directory and IA folder:
```bash
ls . IA
```

Expected output:
```
.:
Employees  Finance  HR  IA  Management  SharedFolders

IA:
backup.CompanyA.tar.gz
```

**Interpretation**: The backup file is no longer in the parent directory (not shown in current directory listing) and has been successfully moved to the IA folder.

In a real-world scenario, this allows you to:
- Share backups with specific teams (IA team in this case)
- Organize backups by department or purpose
- Control access through directory permissions
- Prepare files for transfer to external storage

## Key Concepts Covered

### Tar (Tape Archive)
A Unix utility for creating archive files, often combined with compression tools like gzip. Tar preserves file permissions, ownership, and directory structure—essential for system backups.

### Archive vs. Compression
- **Archive**: Combines multiple files/directories into single file (tar does this)
- **Compression**: Reduces file size (gzip, bzip2, xz do this)
- **tar.gz**: Archived AND compressed (best of both)

### Gzip Compression
Fast, widely-supported compression algorithm. The `.gz` extension indicates gzip compression. Alternative compression methods include bzip2 (`.bz2`) and xz (`.xz`).

### Redirection and Piping
- **|** (pipe): Sends output of one command as input to another
- **>** (redirect): Writes output to file (overwrites)
- **>>** (append): Adds output to end of file
- **tee**: Writes to both file and terminal simultaneously

### Backup Best Practices
- Include timestamps in backup filenames
- Maintain logs of backup operations
- Store backups in separate locations
- Test backup restoration periodically
- Compress backups to save space

## Essential Commands Reference

### Tar Commands

| Command | Purpose |
|---------|---------|
| `tar -cvf archive.tar dir/` | Create uncompressed archive |
| `tar -czvf archive.tar.gz dir/` | Create gzip compressed archive |
| `tar -cjvf archive.tar.bz2 dir/` | Create bzip2 compressed archive |
| `tar -xvf archive.tar` | Extract archive |
| `tar -xzvf archive.tar.gz` | Extract gzip archive |
| `tar -tvf archive.tar` | List contents without extracting |
| `tar -cvpf archive.tar dir/` | Create archive preserving permissions |

### Tar Options Explained

| Flag | Purpose |
|------|---------|
| `-c` | Create new archive |
| `-x` | Extract archive |
| `-t` | List archive contents |
| `-v` | Verbose (show files being processed) |
| `-f` | Specify filename (must be last flag before filename) |
| `-z` | Use gzip compression (.gz) |
| `-j` | Use bzip2 compression (.bz2) |
| `-J` | Use xz compression (.xz) |
| `-p` | Preserve permissions and ownership |
| `-s` | Sort files by name |
| `-C` | Change to directory before extracting |

### File Operations Commands

| Command | Purpose |
|---------|---------|
| `echo "text"` | Print text to terminal |
| `echo "text" > file.txt` | Write text to file (overwrite) |
| `echo "text" >> file.txt` | Append text to file |
| `tee file.txt` | Write to file and display on terminal |
| `cat file.txt` | Display file contents |
| `mv source destination` | Move or rename file |
| `touch filename` | Create empty file or update timestamp |

## Working with Archives

### Creating Archives

**Simple archive (no compression):**
```bash
tar -cvf backup.tar directory/
```

**Compressed with gzip (most common):**
```bash
tar -czvf backup.tar.gz directory/
```

**Maximum compression with bzip2:**
```bash
tar -cjvf backup.tar.bz2 directory/
```

**With timestamp in filename:**
```bash
tar -czvf backup-$(date +%Y%m%d-%H%M%S).tar.gz directory/
```

### Extracting Archives

**Extract in current directory:**
```bash
tar -xzvf backup.tar.gz
```

**Extract to specific directory:**
```bash
tar -xzvf backup.tar.gz -C /path/to/destination/
```

**List contents without extracting:**
```bash
tar -tzvf backup.tar.gz
```

**Extract single file:**
```bash
tar -xzvf backup.tar.gz path/to/file.txt
```

## Practical Examples

### Create Timestamped Backup
```bash
# Create backup with current date/time in filename
tar -czvf backup-$(date +%Y%m%d-%H%M%S).tar.gz CompanyA/

# Create backup and log it
BACKUP_FILE="backup-$(date +%Y%m%d-%H%M%S).tar.gz"
tar -czvf $BACKUP_FILE CompanyA/
echo "$(date), $BACKUP_FILE" >> backup-log.txt
```

### Automated Backup Script
```bash
#!/bin/bash
# Simple backup script
BACKUP_DIR="/home/ec2-user/backups"
SOURCE_DIR="/home/ec2-user/CompanyA"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_FILE="backup-$TIMESTAMP.tar.gz"

# Create backup
tar -czvf $BACKUP_DIR/$BACKUP_FILE $SOURCE_DIR

# Log it
echo "$TIMESTAMP, $BACKUP_FILE" >> $BACKUP_DIR/backup-log.csv
```

### Verify Archive Integrity
```bash
# Test if archive is valid
tar -tzf backup.tar.gz > /dev/null && echo "Archive OK" || echo "Archive corrupted"
```

## Troubleshooting Tips

- **Permission denied**: Add `sudo` before tar command for system directories
- **Archive too large**: Use bzip2 (`-j`) for better compression than gzip
- **Disk space issues**: Check available space with `df -h` before creating large archives
- **Path issues**: Use absolute paths or ensure you're in correct directory
- **Cannot find file**: Verify path with `ls` before archiving
- **Extraction overwrites files**: Use different directory or backup existing files first

## Important Notes

- This lab builds on knowledge from all previous labs
- Tar preserves directory structure when creating archives
- The order of tar flags matters: `-f` must come before the filename
- Gzip compression is fast but bzip2 offers better compression ratios
- Moving files with `mv` is instant (same filesystem); copying is slower
- Backup logs help track when backups were created and prevent duplicates

## Best Practices

### Backup Strategy
- **Naming Convention**: Include dates/timestamps in backup filenames
- **Regular Schedule**: Automate backups with cron jobs
- **Multiple Copies**: Follow 3-2-1 rule (3 copies, 2 different media, 1 offsite)
- **Compression**: Always compress backups to save disk space
- **Verification**: Test restoration periodically to ensure backups work
- **Documentation**: Maintain logs of all backup operations

### Archive Management
- Use consistent naming conventions
- Store archives in dedicated backup directories
- Set up automated cleanup of old backups
- Monitor disk space on backup storage
- Encrypt sensitive backups before transfer

### Security Considerations
- Restrict access to backup directories
- Use encryption for sensitive data archives
- Verify archive integrity with checksums
- Secure backup transfer with scp or rsync over SSH
- Rotate and expire old backups according to policy

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting (Command Host instance)
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **Automated Backups**: Schedule with cron or systemd timers
- **Incremental Backups**: Use tar with `--listed-incremental`
- **Remote Backups**: Transfer with scp, rsync, or AWS S3
- **Backup Encryption**: Use gpg to encrypt archives
- **Differential Backups**: Backup only changed files
- **Backup Scripts**: Create comprehensive backup automation
- **Compression Comparison**: Test gzip vs bzip2 vs xz
- **Archive Splitting**: Split large archives with split command
- **Checksum Verification**: Use md5sum or sha256sum
- **Backup Rotation**: Implement grandfather-father-son strategy
- **Cloud Integration**: Sync backups to Amazon S3 or Glacier
- **Disaster Recovery**: Develop full restoration procedures

## Practice Exercises

To reinforce your learning:

1. **Create daily backup script** that includes date in filename
2. **Extract specific files** from an archive without extracting everything
3. **Compare compression ratios** between gzip, bzip2, and xz
4. **Create incremental backup** that only archives changed files
5. **Automate cleanup** of backups older than 30 days
6. **Transfer backup** to remote server using scp
7. **Verify archive integrity** using checksums

## Related Labs

- Introduction to Amazon EC2
- Introduction to Amazon Linux AMI
- Linux Command Line
- Managing Users and Groups
- Editing Files
- Working with the File System

## Resources

- [GNU Tar Manual](https://www.gnu.org/software/tar/manual/)
- [Gzip Documentation](https://www.gnu.org/software/gzip/manual/)
- [Linux Backup Strategies](https://wiki.archlinux.org/title/System_backup)
- [AWS Backup Best Practices](https://docs.aws.amazon.com/aws-backup/latest/devguide/best-practices.html)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025

**Related Labs**: Introduction to Amazon EC2, Introduction to Amazon Linux AMI, Linux Command Line, Managing Users and Groups, Editing Files, Working with the File System