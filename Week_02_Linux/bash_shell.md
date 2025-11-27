# The Bash Shell Lab

## Overview

This lab teaches you essential bash shell customization and environment management skills that enhance productivity and workflow efficiency. You'll learn how to create command aliases for common operations, understand and modify the PATH environment variable, and configure your shell environment for optimal usability. These skills are fundamental for system administrators, developers, and anyone working extensively in Linux command-line environments.

## Learning Objectives

By completing this lab, you will be able to:

- Create and use command aliases for complex operations
- Understand the purpose and syntax of bash aliases
- Work with the PATH environment variable
- Add custom directories to PATH for executable discovery
- Understand how bash searches for and executes commands
- Troubleshoot command execution issues related to PATH
- Apply shell customization techniques for improved workflow

## Lab Duration

Approximately 30 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux EC2 instance
- Familiarity with Linux commands and file operations
- Understanding of directory navigation and file permissions
- Knowledge of tar command from "Working with Files" lab

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux with bash shell
- **SSH Connection**: Secure remote access to instance
- **Pre-existing Directory Structure**: CompanyA folder with bin subdirectory
- **Sample Script**: hello.sh in CompanyA/bin directory

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

### Task 2: Create an Alias for a Backup Operation

Learn to create command shortcuts that simplify complex operations.

#### Understanding Aliases

An **alias** is a custom shortcut that replaces a long command with a shorter one. Aliases improve efficiency by reducing typing and standardizing common operations.

**Benefits of aliases**:
- Reduce typing for frequently-used commands
- Prevent syntax errors in complex commands
- Standardize operations across team members
- Improve productivity and workflow efficiency

#### Verify Location

Confirm you're in the home directory:
```bash
pwd
# Expected output: /home/ec2-user/
```

#### Create the backup Alias

Create an alias named `backup` using the tar command:
```bash
alias backup='tar -cvzf '
```

**Command breakdown**:
- `alias`: Command to create an alias
- `backup`: Name of the new alias
- `'tar -cvzf '`: Command that the alias will execute
  - `tar`: Archive utility
  - `-c`: Create new archive
  - `-v`: Verbose (show files being archived)
  - `-z`: Compress with gzip
  - `-f`: Specify filename (next parameter)

**Understanding tar flags**:
- **-c**: Create archive
- **-v**: Verbose output (displays what's being archived)
- **-z**: Compress using gzip (.gz format)
- **-f**: File (must be followed by archive filename)

**Alternative combinations**:
- `tar -cf`: Creates archive without compression or verbose output
- `tar -cvf`: Creates archive with verbose output but no compression
- `tar -czf`: Creates compressed archive without verbose output

#### Use the backup Alias

Back up the CompanyA folder using your new alias:
```bash
backup backup_companyA.tar.gz CompanyA
```

**Command interpretation**:
```bash
backup                        # Your alias
backup_companyA.tar.gz       # First parameter: output filename
CompanyA                     # Second parameter: directory to backup
```

**What actually executes**:
```bash
tar -cvzf backup_companyA.tar.gz CompanyA
```

Expected output shows all archived files:
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
CompanyA/bin/hello.sh
```

#### Verify Archive Creation

Confirm the backup file was created:
```bash
ls
# Output: backup_companyA.tar.gz  CompanyA
```

**Result**: You've successfully created a reusable backup command that compresses and archives directories with a simple, memorable syntax.

### Task 3: Explore and Update the PATH Environment Variable

Learn how bash finds and executes commands using the PATH variable.

#### Navigate to bin Directory

Change to the CompanyA bin directory:
```bash
cd /home/ec2-user/CompanyA/bin
```

**Alternative navigation**:
```bash
pwd  # Verify location: /home/ec2-user
cd CompanyA/bin
```

#### Attempt 1: Run Script with Relative Path

Execute the script using relative path notation:
```bash
./hello.sh
```

Expected output:
```
hello ec2-user
```

**Explanation**: `./` tells bash to look in the current directory. This method works because you specify exactly where the script is located.

#### Attempt 2: Navigate to Parent and Run with Path

Move to parent directory and try again:
```bash
cd ..
# Now in: /home/ec2-user/CompanyA
```

Run the script with relative path:
```bash
./bin/hello.sh
```

Expected output:
```
hello ec2-user
```

**Explanation**: `./bin/hello.sh` specifies the path relative to current directory. This works because you're explicitly telling bash where to find the script.

#### Attempt 3: Run Script Without Path (Fails)

Try running the script without specifying a path:
```bash
hello.sh
```

Expected output:
```
bash: hello.sh: command not found
```

**Why it failed**: When you don't specify a path (no `./` or `/`), bash searches only in directories listed in the PATH variable. Since `/home/ec2-user/CompanyA/bin` isn't in PATH, bash cannot find the script.

#### Display the PATH Variable

View the current PATH contents:
```bash
echo $PATH
```

Expected output:
```
/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/ec2-user/.local/bin:/home/ec2-user/bin
```

**PATH structure**:
- Multiple directories separated by colons (`:`)
- Bash searches directories in order from left to right
- First match wins when multiple executables have the same name

**Current PATH directories**:
- `/usr/local/bin`: User-installed system-wide programs
- `/usr/bin`: Standard system programs
- `/usr/local/sbin`: User-installed system administration programs
- `/usr/sbin`: System administration programs
- `/home/ec2-user/.local/bin`: User-specific Python/pip installations
- `/home/ec2-user/bin`: User's personal scripts

**Notice**: `/home/ec2-user/CompanyA/bin` is NOT in the PATH, explaining why `hello.sh` wasn't found.

#### Add Directory to PATH

Add the CompanyA/bin directory to PATH:
```bash
PATH=$PATH:/home/ec2-user/CompanyA/bin
```

**Command breakdown**:
- `PATH=`: Set the PATH variable
- `$PATH`: Include current PATH contents (preserves existing directories)
- `:`: Directory separator
- `/home/ec2-user/CompanyA/bin`: New directory to add

**Result**: The new directory is appended to the end of PATH.

#### Verify Script Now Works

Try running the script again without a path:
```bash
hello.sh
```

Expected output:
```
hello ec2-user
```

**Success!** Bash now finds the script because `/home/ec2-user/CompanyA/bin` is in the PATH.

## Key Concepts Covered

### Bash Shell

The **Bourne Again SHell (bash)** is the default command-line interpreter for most Linux distributions. It executes commands, runs scripts, and provides a powerful interactive environment.

### Command Aliases

Shortcuts that map a simple name to a longer command or command sequence. Aliases exist only in the current shell session unless saved to shell configuration files.

**Alias characteristics**:
- Session-specific (lost when you log out)
- Can include options and flags
- Cannot accept parameters directly (use functions for that)
- Override existing commands (use carefully)

### Environment Variables

Variables that define the shell environment and affect how the system behaves. They're accessible by all processes spawned from the shell.

**Common environment variables**:
- `PATH`: Directories to search for executables
- `HOME`: User's home directory
- `USER`: Current username
- `SHELL`: Path to current shell
- `PWD`: Present working directory
- `LANG`: System language settings

### PATH Variable

A colon-separated list of directories where the shell searches for executable programs. When you type a command, bash searches PATH directories in order until it finds a match.

**PATH search behavior**:
1. Check if command includes a path (`/` or `./`)
2. If yes, look in specified location only
3. If no, search each PATH directory in order
4. Execute first match found
5. Report "command not found" if no match

### Command Execution Priority

When you type a command, bash searches in this order:
1. **Aliases**: Checked first
2. **Functions**: Custom bash functions
3. **Builtins**: Commands built into bash (cd, echo, etc.)
4. **Executables in PATH**: External programs

### Relative vs Absolute Paths

**Absolute path**: Full path from root directory
- Example: `/home/ec2-user/CompanyA/bin/hello.sh`
- Works from any location

**Relative path**: Path relative to current directory
- Example: `./hello.sh` or `../bin/hello.sh`
- Depends on current working directory

## Essential Commands Reference

### Alias Commands

| Command | Purpose |
|---------|---------|
| `alias name='command'` | Create new alias |
| `alias` | List all aliases |
| `unalias name` | Remove specific alias |
| `unalias -a` | Remove all aliases |
| `type name` | Show if name is alias, function, or command |
| `\command` | Bypass alias (run original command) |

### Environment Variable Commands

| Command | Purpose |
|---------|---------|
| `echo $VARIABLE` | Display variable value |
| `printenv` | Show all environment variables |
| `export VAR=value` | Create/set environment variable |
| `env` | Display environment |
| `set` | Show all variables and functions |
| `unset VARIABLE` | Remove variable |

### PATH Manipulation

| Command | Purpose |
|---------|---------|
| `echo $PATH` | Display current PATH |
| `PATH=$PATH:/new/dir` | Add directory to end of PATH |
| `PATH=/new/dir:$PATH` | Add directory to beginning of PATH |
| `export PATH` | Make PATH available to child processes |
| `which command` | Show full path of command |
| `whereis command` | Locate command, source, and man pages |

## Practical Examples

### Common Aliases

```bash
# Navigation shortcuts
alias ..='cd ..'
alias ...='cd ../..'
alias home='cd ~'

# Directory listing variations
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Safety nets
alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# System information
alias ports='netstat -tulanp'
alias meminfo='free -m -l -t'
alias cpuinfo='lscpu'

# Git shortcuts
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'

# Docker shortcuts
alias dps='docker ps'
alias dimg='docker images'
alias dexec='docker exec -it'

# System updates
alias update='sudo yum update -y'
alias upgrade='sudo yum upgrade -y'
```

### PATH Management

```bash
# View current PATH
echo $PATH

# Add directory temporarily (current session only)
PATH=$PATH:/opt/myapp/bin

# Add multiple directories
PATH=$PATH:/opt/app1/bin:/opt/app2/bin

# Add directory to beginning (higher priority)
PATH=/opt/priority/bin:$PATH

# Remove directory from PATH (requires manual editing)
PATH=$(echo $PATH | sed 's|:/unwanted/path||')

# Verify command location
which python3
whereis nginx

# Show all locations of a command
type -a ls
```

### Making Changes Permanent

Add aliases and PATH changes to shell configuration files:

**For bash** (most common):
```bash
# Edit .bashrc
nano ~/.bashrc

# Add aliases
alias backup='tar -cvzf'
alias ll='ls -alF'

# Add to PATH
export PATH=$PATH:/home/ec2-user/CompanyA/bin

# Save and reload
source ~/.bashrc
```

**For all users** (requires sudo):
```bash
# System-wide aliases
sudo nano /etc/profile.d/custom-aliases.sh

# System-wide PATH
sudo nano /etc/environment
```

## Troubleshooting Tips

### Alias Issues
- **Alias not working**: Check spelling with `alias` command
- **Alias doesn't persist**: Add to `~/.bashrc` and run `source ~/.bashrc`
- **Alias interferes with command**: Use `\command` to bypass alias
- **Syntax error**: Check quotes and spacing in alias definition

### PATH Issues
- **Command not found**: Check if directory is in PATH with `echo $PATH`
- **PATH changes don't persist**: Add `export PATH=...` to `~/.bashrc`
- **Script won't execute**: Check file permissions with `ls -l`, may need `chmod +x`
- **Wrong command executes**: Check order in PATH, use `which command` to verify
- **PATH reset after logout**: Changes are session-only; add to config file

### Script Execution Issues
- **Permission denied**: Run `chmod +x script.sh` to make executable
- **Bad interpreter**: Check shebang line (`#!/bin/bash`) at top of script
- **Script not found**: Verify file exists and PATH is correct
- **Script runs but errors**: Check script syntax and dependencies

## Important Notes

- Aliases are session-specific unless added to shell configuration files
- PATH changes are temporary unless added to `~/.bashrc` or similar
- The order of directories in PATH matters—first match wins
- Use absolute paths in cron jobs and scripts (PATH may differ)
- Aliases don't work in scripts (use functions or full commands)
- Always include `$PATH` when modifying PATH to preserve existing entries
- Be careful not to override important system commands with aliases

## Best Practices

### Alias Best Practices
- Use descriptive names that don't conflict with existing commands
- Document complex aliases with comments in `.bashrc`
- Test aliases thoroughly before adding to configuration
- Avoid aliases for destructive commands without confirmation flags
- Use functions instead of aliases when parameters are needed
- Keep aliases simple; use scripts for complex operations

### PATH Best Practices
- Always append or prepend to PATH; never replace entirely
- Place user directories after system directories for security
- Use absolute paths when modifying PATH
- Document custom PATH additions
- Avoid adding too many directories (slows command lookup)
- Verify PATH doesn't contain current directory (`.`) for security

### Shell Configuration
```bash
# Example ~/.bashrc structure

# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# User-specific aliases
alias backup='tar -cvzf'
alias ll='ls -alF'
alias update='sudo yum update -y'

# User-specific PATH additions
export PATH=$PATH:/home/ec2-user/CompanyA/bin
export PATH=$PATH:/opt/custom-tools/bin

# User-specific functions
function mkcd() {
    mkdir -p "$1" && cd "$1"
}

# Custom prompt (optional)
export PS1='\u@\h:\w\$ '
```

### Security Considerations
- Never add untrusted directories to PATH
- Avoid adding current directory (`.`) to PATH
- Check execute permissions on scripts
- Be cautious with aliases that use `sudo`
- Validate scripts before making them globally accessible
- Use full paths in privileged operations

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting (Command Host instance)
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **Bash Functions**: More powerful than aliases, accept parameters
- **Shell Scripting**: Automate complex tasks with bash scripts
- **Custom Prompt (PS1)**: Customize command prompt appearance
- **Shell Options**: Configure bash behavior with `set` and `shopt`
- **Command Completion**: Custom tab completion for commands
- **Shell History**: Manage and search command history
- **Input/Output Redirection**: Advanced redirection techniques
- **Process Substitution**: Use command output as file input
- **Parameter Expansion**: Advanced variable manipulation
- **Array Variables**: Work with arrays in bash
- **Signal Handling**: Trap and handle signals in scripts
- **Debugging**: Debug bash scripts with `set -x` and other tools

## Practice Exercises

To reinforce your learning:

1. **Create productivity aliases** for your most-used commands
2. **Build function** that creates and enters a directory in one command
3. **Customize PATH** to include multiple project directories
4. **Write backup script** that uses aliases and variables
5. **Create conditional alias** that behaves differently based on parameters
6. **Set up color-coded prompt** showing git branch and exit status
7. **Build command wrapper** that logs all commands to a file
8. **Create alias hierarchy** where aliases call other aliases

## Related Labs

- Introduction to Amazon EC2
- Introduction to Amazon Linux AMI
- Linux Command Line
- Managing Users and Groups
- Editing Files
- Working with the File System
- Working with Files
- Managing File Permissions
- Working with Commands
- Managing Processes
- Managing Services - Monitoring

## Resources

- [Bash Manual](https://www.gnu.org/software/bash/manual/)
- [Bash Alias Tutorial](https://linuxize.com/post/how-to-create-bash-aliases/)
- [Environment Variables Guide](https://www.digitalocean.com/community/tutorials/how-to-read-and-set-environmental-and-shell-variables-on-linux)
- [Advanced Bash Scripting Guide](https://tldp.org/LDP/abs/html/)
- [Bash Configuration Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓
