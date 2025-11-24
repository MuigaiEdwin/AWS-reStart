# Working with the File System Lab

## Overview

This hands-on lab reinforces your Linux file system management skills by combining knowledge from previous labs into practical scenarios. You'll create complex directory structures, manipulate files and folders, and reorganize file hierarchies—essential skills for system administration, application deployment, and maintaining organized server environments. This lab simulates real-world scenarios where you need to structure and reorganize company data.

## Learning Objectives

By completing this lab, you will be able to:

- Create multi-level folder structures using mkdir
- Create empty files using touch
- Navigate directory hierarchies with relative and absolute paths
- Copy files and directories recursively
- Move files and directories to new locations
- Delete files and directories safely
- Verify directory structures and file locations
- Use relative path notation (.., ../, ./) effectively

## Lab Duration

Approximately 30 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux EC2 instance
- Familiarity with basic Linux navigation commands (cd, pwd, ls)
- Understanding of directory hierarchies and file paths

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux
- **SSH Connection**: Secure remote access to instance
- **File System**: Linux directory structure for hands-on practice

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

### Task 2: Create a Folder Structure

Create a complete directory hierarchy representing a company's organizational structure.

#### Target Directory Structure

```
/home/ec2-user/CompanyA/
├── Finance/
│   ├── ProfitAndLossStatements.csv
│   └── Salary.csv
├── HR/
│   ├── Assessments.csv
│   └── TrialPeriod.csv
└── Management/
    ├── Managers.csv
    └── Schedule.csv
```

#### Step-by-Step Creation

**Verify starting location:**
```bash
pwd
# Output: /home/ec2-user
# If not, navigate there: cd /home/ec2-user
```

**Create top-level directory:**
```bash
mkdir CompanyA
cd CompanyA
```

**Create subdirectories:**
```bash
mkdir Finance HR Management
ls
# Output: Finance HR Management
```

**Create files in HR directory:**
```bash
cd HR
touch Assessments.csv TrialPeriod.csv
ls
# Output: Assessments.csv TrialPeriod.csv
```

**Create files in Finance directory:**
```bash
cd ../Finance
touch Salary.csv ProfitAndLossStatements.csv
ls
# Output: Salary.csv ProfitAndLossStatements.csv
```

**Navigate back to CompanyA and create Management files:**
```bash
cd ..
touch Management/Managers.csv Management/Schedule.csv
ls Management
# Output: Managers.csv Schedule.csv
```

**Verify complete structure:**
```bash
ls -laR
```

This displays the entire directory tree with all files and subdirectories, including permissions and timestamps.

#### Path Notation Examples

**Working directly in current directory:**
- `ls` - List current directory contents
- `touch myFile.csv` - Create file in current directory

**Using relative paths:**
- `ls Management` - List contents of Management subfolder
- `touch Management/myFile.csv` - Create file in Management subfolder
- `cd ../Finance` - Navigate to parent directory, then into Finance
- `touch ../Management/myFile.csv` - Create file in sibling directory

### Task 3: Delete and Reorganize Folders

Reorganize the directory structure to reflect organizational changes.

#### New Target Structure

```
/home/ec2-user/CompanyA/
└── HR/
    ├── Employees/
    │   ├── Assessments.csv
    │   └── TrialPeriod.csv
    ├── Finance/
    │   ├── ProfitAndLossStatements.csv
    │   └── Salary.csv
    └── Management/
        ├── Managers.csv
        └── Schedule.csv
```

#### Changes Required:
1. Copy Finance folder into HR and remove original
2. Move Management folder inside HR
3. Create new Employees folder in HR
4. Move assessment files into Employees folder

#### Step-by-Step Reorganization

**Verify starting location:**
```bash
pwd
# Output: /home/ec2-user/CompanyA
```

**Copy Finance folder to HR:**
```bash
cp -r Finance HR
ls HR/Finance
# Output: ProfitAndLossStatements.csv Salary.csv
```

**Attempt to remove Finance directory:**
```bash
rmdir Finance
# Output: rmdir: failed to remove 'Finance/': Directory not empty
```

**Understanding rmdir limitation:**
`rmdir` only works on empty directories. You have two options:
1. Remove files first, then remove directory
2. Use `rm -r` to recursively delete directory and contents

**Remove files from Finance, then remove directory:**
```bash
rm Finance/ProfitAndLossStatements.csv Finance/Salary.csv
ls Finance
# Output: (empty)

rmdir Finance
ls
# Output: HR Management
```

**Move Management folder into HR:**
```bash
mv Management HR
ls . HR/Management
# Output shows Management is now inside HR
```

**Navigate to HR and create Employees folder:**
```bash
cd HR
mkdir Employees
```

**Move assessment files into Employees:**
```bash
mv Assessments.csv TrialPeriod.csv Employees
ls . Employees
# Output:
# .: Employees Finance Management
# Employees/: Assessments.csv TrialPeriod.csv
```

**Verify final structure:**
```bash
cd ..
ls -laR HR
```

## Key Concepts Covered

### Directory Hierarchy
Linux uses a tree-like file system structure starting from root (`/`). Every file and directory has a path that describes its location.

### Absolute vs. Relative Paths
- **Absolute Path**: Complete path from root (e.g., `/home/ec2-user/CompanyA/Finance`)
- **Relative Path**: Path relative to current directory (e.g., `Finance` or `../Finance`)

### Special Path Notations
- `.` (dot): Current directory
- `..` (dot-dot): Parent directory
- `~` (tilde): Current user's home directory
- `/` (slash): Root directory or path separator

### Recursive Operations
Many commands support recursive operations with the `-r` or `-R` flag to process directories and all their contents.

### Directory vs. File Deletion
- Files: Use `rm filename`
- Empty directories: Use `rmdir dirname`
- Non-empty directories: Use `rm -r dirname`

### Copy vs. Move
- **Copy (cp)**: Creates duplicate; original remains
- **Move (mv)**: Relocates file/directory; original is removed
- Both can be used to rename files/directories

## Essential Commands Reference

| Command | Purpose | Example |
|---------|---------|---------|
| `mkdir` | Create directory | `mkdir Finance` |
| `mkdir -p` | Create parent directories | `mkdir -p Company/HR/Finance` |
| `touch` | Create empty file | `touch file.csv` |
| `cd` | Change directory | `cd Finance` |
| `pwd` | Print working directory | `pwd` |
| `ls` | List directory contents | `ls -la` |
| `ls -R` | List recursively | `ls -R` |
| `cp` | Copy file | `cp file1.txt file2.txt` |
| `cp -r` | Copy directory recursively | `cp -r Finance HR` |
| `mv` | Move or rename | `mv file.txt newname.txt` |
| `rm` | Remove file | `rm file.txt` |
| `rm -r` | Remove directory recursively | `rm -r Finance` |
| `rmdir` | Remove empty directory | `rmdir Finance` |

## Command Options Explained

### ls Command Options
- `-l`: Long format (permissions, owner, size, date)
- `-a`: Show hidden files (starting with .)
- `-R`: Recursive listing of subdirectories
- `-h`: Human-readable file sizes

### cp Command Options
- `-r` or `-R`: Copy directories recursively
- `-i`: Interactive (prompt before overwrite)
- `-v`: Verbose (show files being copied)
- `-p`: Preserve permissions and timestamps

### rm Command Options
- `-r` or `-R`: Remove directories recursively
- `-f`: Force removal without prompts
- `-i`: Interactive (prompt before each removal)
- `-v`: Verbose (show files being removed)

**Warning**: `rm -rf` is extremely dangerous—it forcibly removes directories and all contents without confirmation!

## Helpful Hints

### Validation Strategy
After each operation, use these commands to verify success:
- `pwd` - Confirm current location
- `ls` - View directory contents
- `ls -la` - View detailed directory contents including hidden files
- `ls -R` - View entire directory tree

### Path Navigation Tips
- Use `cd ..` to move up one directory level
- Use `cd ../..` to move up two directory levels
- Use `cd -` to return to previous directory
- Use `cd ~` or just `cd` to return to home directory

### File Creation Shortcuts
- Create multiple files: `touch file1.txt file2.txt file3.txt`
- Create multiple directories: `mkdir dir1 dir2 dir3`
- Create nested directories: `mkdir -p parent/child/grandchild`

## Troubleshooting Tips

- **Directory not empty**: Use `rm -r` instead of `rmdir`, or remove contents first
- **Permission denied**: Add `sudo` before command for system directories
- **No such file or directory**: Verify path with `pwd` and `ls`
- **Typo in filename**: Use tab completion to avoid typing errors
- **Lost in filesystem**: Use `pwd` to find location, `cd ~` to return home
- **Accidentally deleted files**: No undo for `rm`—be careful and use `rm -i` for important files

## Important Notes

- This lab combines knowledge from all previous labs
- Reference previous labs if you need command syntax help
- Linux file system is case-sensitive: `Finance` ≠ `finance`
- Spaces in filenames require quotes or escape characters
- The `rm` command is permanent—deleted files cannot be easily recovered
- Always verify your location with `pwd` before destructive operations

## Best Practices

### Before Deleting
- Use `ls` to confirm what you're about to delete
- Double-check directory location with `pwd`
- Consider using `rm -i` for interactive confirmation
- Back up important data before major reorganizations

### Directory Organization
- Use clear, descriptive names without spaces
- Maintain consistent naming conventions
- Group related files in appropriate directories
- Document directory structure for team members

### Safe File Operations
- Test commands on non-critical files first
- Use relative paths when working within a project
- Verify results after each operation
- Keep backups of important directory structures

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting (Command Host instance)
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **Symbolic Links**: Create shortcuts with `ln -s`
- **Hard Links**: Create multiple references to same file
- **File Permissions**: Master chmod for access control
- **File Searching**: Use `find` and `locate` commands
- **Disk Usage**: Monitor space with `du` and `df`
- **File Compression**: Use `tar`, `gzip`, `zip`
- **Rsync**: Efficient file synchronization
- **Wildcards**: Use `*`, `?`, `[]` for pattern matching
- **Shell Globbing**: Advanced filename pattern matching
- **Automated Backups**: Script directory backups

## Practice Exercises

To reinforce your learning:

1. **Create a project structure** for a web application with folders for `src`, `tests`, `docs`, and `config`
2. **Reorganize logs** by moving old log files into dated subdirectories
3. **Bulk rename files** using a combination of `mv` and shell loops
4. **Create backup directory** and copy important files while preserving timestamps
5. **Clean up** temporary files using `find` and `rm` together

## Related Labs

- Introduction to Amazon EC2
- Introduction to Amazon Linux AMI
- Linux Command Line
- Managing Users and Groups
- Editing Files

## Resources

- [Linux File System Hierarchy](https://www.pathname.com/fhs/)
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/)
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025

**Related Labs**: Introduction to Amazon EC2, Introduction to Amazon Linux AMI, Linux Command Line, Managing Users and Groups, Editing Files