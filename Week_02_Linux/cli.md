# Linux Command Line Lab

## Overview

This lab builds on foundational Linux knowledge to enhance your command-line skills and productivity. You'll learn essential system commands for gathering information about your environment, discover workflow optimization techniques, and master bash history search functionality. These skills are critical for efficient system administration and troubleshooting in cloud environments.

## Learning Objectives

By completing this lab, you will be able to:

- Run system information commands to gather knowledge about the current system and session
- Use command-line shortcuts and auto-completion to improve efficiency
- Search and retrieve previous bash commands from history
- Edit and rerun commands using bash history features
- Leverage command history to optimize workflow

## Lab Duration

Approximately 30 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware
- SSH access to Amazon Linux EC2 instance
- Familiarity with basic terminal navigation
- Knowledge of SSH key pair configuration

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux
- **SSH Connection**: Secure remote access to instance
- **Bash Shell**: Command interpreter for executing commands

## Tasks Overview

### Task 1: Connect to Amazon Linux EC2 Instance via SSH

Establish a secure connection to your command host instance following the same procedures from the previous lab.

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

### Task 2: Run Familiar Commands

Discover essential system information commands to understand your environment.

#### Command Auto-completion

- Type `whoa` and press **Tab** to auto-complete to `whoami`
- Auto-completion increases efficiency and reduces typos

#### System Information Commands

Run these commands to gather information about your system:

```bash
# Display current username
whoami

# Show shortened hostname
hostname -s

# Display system uptime in readable format
uptime -p

# Show logged-in users and session details
who -H -a

# Display date and time for different timezones
TZ=America/New_York date
TZ=America/Los_Angeles date

# Show user ID and group information
id ec2-user
```

#### Command Explanations

**whoami**: Returns the login name of the current user (e.g., `ec2-user`)

**hostname -s**: Displays the shortened hostname (e.g., `ip-10.x.x.x`); useful for identifying which instance you're working on

**uptime -p**: Shows how long the system has been running in human-readable format (e.g., "up 2 hours, 15 minutes")

**who -H -a**: Lists all logged-in users with additional information:
- **Name**: Username
- **Line**: Terminal line information
- **Time**: When the user logged in
- **Idle**: How long the user has been inactive
- **PID**: Process identifier
- **Comment**: Additional session information

**TZ (Timezone) Commands**: Set timezone environment variable before executing date command to see time in different locations worldwide

**id**: Returns:
- User ID (uid)
- Group ID (gid)
- All groups the user belongs to

#### Calendar Commands

Explore different calendar view formats:

```bash
# Display current month in Julian date format (1-366)
cal -j

# Display calendar with Sunday as first day
cal -s

# Display calendar with Monday as first day
cal -m
```

**Julian Date Format**: Consecutive numbering (1-366) for all days in a year, useful in certain industries. Check the cal man page for additional options: `man cal`

### Task 3: Improve Workflow Through History and Search

Optimize productivity by leveraging bash command history features.

#### Viewing Command History

View all previously entered commands:

```bash
history
```

This displays a numbered list of all commands you've executed in the current session, with commands from Task 2 visible.

#### Reverse History Search

Perform reverse search through command history:

1. Press **Ctrl+R** to open reverse history search prompt
2. Type search term (e.g., `TZ` to find timezone commands)
3. Press **Tab** to auto-complete and prepare for editing
4. Use **Arrow Keys** to edit the command inline
5. Press **Enter** to execute the edited command

**Example**: Searching for `TZ` will locate the previous timezone date commands, allowing you to modify the timezone or other parameters before re-executing.

#### Rerunning Previous Commands

Execute the most recent command using the bang operator:

```bash
# Run the last command again
!!

# Example workflow:
date          # First execution
!!            # Runs date again
```

**Use Cases for !!**:
- Rerun a command that produced useful output
- Execute a failed command with modifications
- Quickly repeat operations without retyping

## Key Concepts Covered

### Command Auto-completion
Built-in shell feature that completes partial commands or filenames by pressing **Tab**, reducing typing errors and improving efficiency.

### Bash History
The shell maintains a history of all entered commands, typically stored in `~/.bash_history`. This allows you to review, search, and reuse previous commands.

### Environment Variables
Variables like `TZ` (timezone) that modify command behavior. Set with `VARIABLE=value` syntax before running a command.

### Process Identifier (PID)
Unique number assigned by the operating system to each running process for tracking and management.

### Julian Calendar
Alternative date format using consecutive numbering (1-366) instead of month/day, common in aviation, meteorology, and military operations.

## Essential Commands Reference

| Command | Purpose |
|---------|---------|
| `whoami` | Display current username |
| `hostname -s` | Show shortened system hostname |
| `uptime -p` | Display system uptime in readable format |
| `who -H -a` | List logged-in users with details |
| `date` | Show current date and time |
| `id` | Display user and group IDs |
| `cal` | Display calendar |
| `history` | Show command history |
| `Ctrl+R` | Reverse search command history |
| `!!` | Repeat last command |

## Workflow Optimization Tips

### Efficiency Techniques

- **Use Tab Completion**: Press Tab while typing commands or filenames to auto-complete
- **Search History**: Use Ctrl+R to find and modify previous commands quickly
- **Rerun Commands**: Use `!!` to execute the last command without retyping
- **Command Aliases**: Create shortcuts for frequently used commands (advanced topic)

### Best Practices

- Review `history` output periodically to understand your workflow
- Use reverse search to find similar commands from different time periods
- Edit retrieved commands before execution to avoid unintended actions
- Clear sensitive commands from history if needed: `history -c`

## Troubleshooting Tips

- **Tab Not Working**: Shell must support tab completion; most bash shells do
- **Ctrl+R Not Responding**: Terminal may be in different mode; try pressing Escape first
- **History Empty**: First command in new session won't have history from previous sessions
- **Timezone Errors**: Ensure timezone string is valid (e.g., `America/New_York`)
- **Command Not Found**: Verify command spelling or check if it's installed with `which` or `type`

## Important Notes

- This lab builds on knowledge from previous courseware
- AWS service access is restricted to lab requirements
- Command history is session-specific (lost after logout)
- History size is typically limited; oldest entries may be removed
- Some commands have many options; check man pages for full documentation

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **Bash Scripting**: Automate command sequences in shell scripts
- **Piping and Redirection**: Combine commands for powerful data processing
- **Regular Expressions**: Advanced pattern matching and text processing
- **Aliases and Functions**: Create custom commands and shortcuts
- **Environment Configuration**: Customize shell behavior in `.bashrc` or `.bash_profile`
- **Process Management**: Control running processes with `ps`, `top`, `kill`
- **File Permissions**: Master `chmod`, `chown`, and access control
- **System Logging**: Analyze logs with `grep`, `tail`, `less`

## Command Examples from Lab

```bash
# Information Gathering
whoami                          # Current user
hostname -s                     # System hostname
uptime -p                       # System uptime
who -H -a                       # Active user sessions
id ec2-user                     # User and group IDs

# Timezone and Date
TZ=America/New_York date       # New York time
TZ=America/Los_Angeles date    # Los Angeles time

# Calendar Views
cal -j                         # Julian calendar format
cal -s                         # Sunday as first day
cal -m                         # Monday as first day

# History and Searching
history                        # Display command history
Ctrl+R                        # Reverse history search
!!                            # Rerun last command
```

## Resources

- [Bash Reference Manual](https://www.gnu.org/software/bash/manual/)
- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/)
- [Linux Man Pages Online](https://man7.org/linux/man-pages/)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025

**Related Labs**: Introduction to Amazon EC2, Introduction to Amazon Linux AMI