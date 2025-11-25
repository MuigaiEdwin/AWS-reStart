# Managing Processes Lab

## Overview

This lab teaches you essential Linux process management and automation skills that are critical for system administration and monitoring. You'll learn how to view and analyze running processes, monitor system performance in real-time, and automate recurring tasks using cron jobs. These skills enable you to maintain system health, troubleshoot performance issues, and implement automated maintenance routines in production environments.

## Learning Objectives

By completing this lab, you will be able to:

- Create process listings using the ps command with filtering
- Use the top command to monitor system performance in real-time
- Understand process states (running, sleeping, stopped, zombie)
- Create and manage cron jobs for task automation
- Edit and validate crontab files for scheduled tasks
- Combine commands to create automated audit files
- Filter and format process information for logging

## Lab Duration

Approximately 45 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux EC2 instance
- Familiarity with Linux commands, file operations, and text editing
- Understanding of command piping and redirection
- Knowledge from previous labs on file permissions and text processing

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux with cron daemon
- **SSH Connection**: Secure remote access to instance
- **Process Management Tools**: ps, top, cron, crontab
- **Pre-existing Directory Structure**: CompanyA with SharedFolders directory

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

### Task 2: Create List of Processes

Generate a filtered process log file for auditing and monitoring purposes.

#### Verify Location

Confirm you're in the correct directory:
```bash
pwd
# Expected output: /home/ec2-user/companyA
# If not: cd companyA
```

#### Create Filtered Process Log

View all processes and filter out root user processes:
```bash
sudo ps -aux | grep -v root | sudo tee SharedFolders/processes.csv
```

**Command breakdown**:
- `sudo ps -aux`: List all processes with detailed information
  - `a`: Show processes for all users
  - `u`: Display user-oriented format
  - `x`: Include processes without controlling terminal
- `|`: Pipe output to next command
- `grep -v root`: Exclude lines containing "root"
  - `-v`: Invert match (exclude instead of include)
- `| sudo tee SharedFolders/processes.csv`: Write to file and display on screen

**Result**: Creates a CSV file containing all non-root processes.

#### Verify the Log File

Display the contents of the process log:
```bash
cat SharedFolders/processes.csv
```

**Expected output columns**:
- USER: Process owner
- PID: Process ID
- %CPU: CPU usage percentage
- %MEM: Memory usage percentage
- VSZ: Virtual memory size
- RSS: Resident set size (physical memory)
- TTY: Controlling terminal
- STAT: Process state
- START: Start time
- TIME: Cumulative CPU time
- COMMAND: Command that started the process

### Task 3: List Processes Using the top Command

Monitor system performance and active processes in real-time.

#### Run the top Command

Execute top to view live system statistics:
```bash
top
```

#### Understanding top Output

**Header Information**:
```
top - 14:23:45 up 2:15, 1 user, load average: 0.00, 0.01, 0.05
Tasks:  93 total,   1 running,  48 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.3 us,  0.2 sy,  0.0 ni, 99.5 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  1009152 total,   123456 free,   234567 used,   651129 buff/cache
KiB Swap:        0 total,        0 free,        0 used.   567890 avail Mem
```

**Line 1 - System Uptime**:
- Current time
- System uptime (hours:minutes)
- Number of logged-in users
- Load average (1, 5, 15 minute intervals)

**Line 2 - Tasks**:
- **Total**: Number of processes
- **Running**: Actively executing processes
- **Sleeping**: Waiting for resources or events
- **Stopped**: Paused processes
- **Zombie**: Terminated processes waiting for parent cleanup

**Line 3 - CPU Usage**:
- `us`: User space processes
- `sy`: System/kernel processes
- `ni`: Nice (priority-adjusted) processes
- `id`: Idle time
- `wa`: I/O wait time
- `hi`: Hardware interrupts
- `si`: Software interrupts
- `st`: Stolen time (virtualization)

**Lines 4-5 - Memory**:
- Physical RAM (KiB Mem)
- Swap space (KiB Swap)
- Total, free, used, and buffer/cache amounts

#### Process List Columns

- **PID**: Process ID
- **USER**: Process owner
- **PR**: Priority
- **NI**: Nice value
- **VIRT**: Virtual memory
- **RES**: Resident memory (physical RAM)
- **SHR**: Shared memory
- **S**: Process state (R=running, S=sleeping, Z=zombie)
- **%CPU**: CPU usage
- **%MEM**: Memory usage
- **TIME+**: Total CPU time
- **COMMAND**: Command name

#### Interactive top Commands

While top is running:
- **q**: Quit top
- **h**: Help
- **k**: Kill a process
- **r**: Renice a process
- **P**: Sort by CPU usage
- **M**: Sort by memory usage
- **T**: Sort by time
- **u**: Filter by user
- **Space**: Refresh display

#### Exit top

Press `q` and Enter to quit.

#### View top Help and Version

```bash
top -hv
```

### Task 4: Create a Cron Job

Automate recurring tasks using the cron daemon for scheduled execution.

#### Verify Location

```bash
pwd
# Expected output: /home/ec2-user/companyA
```

#### Understanding Cron

**Cron** is a time-based job scheduler that runs commands at specified intervals. The **crontab** (cron table) file contains the schedule and commands.

**Crontab Format**:
```
* * * * * command
│ │ │ │ │
│ │ │ │ └─── Day of week (0-7, Sunday=0 or 7)
│ │ │ └───── Month (1-12)
│ │ └─────── Day of month (1-31)
│ └───────── Hour (0-23)
└─────────── Minute (0-59)
```

**Special Characters**:
- `*`: Any value
- `,`: Value list separator (1,3,5)
- `-`: Range of values (1-5)
- `/`: Step values (*/5 = every 5)

#### Create Cron Job

Open crontab editor:
```bash
sudo crontab -e
```

This opens your default text editor (usually vi/vim).

#### Configure Cron Job

Press `i` to enter insert mode, then add these lines:

```bash
SHELL=/bin/bash
PATH=/usr/bin:/bin:/usr/local/bin
MAILTO=root
0 * * * * ls -la $(find .) | sed -e 's/..csv/#####.csv/g' > /home/ec2-user/companyA/SharedFolders/filteredAudit.csv
```

**Configuration breakdown**:

**Environment Variables**:
- `SHELL=/bin/bash`: Use bash shell to run commands
- `PATH=/usr/bin:/bin:/usr/local/bin`: Search path for executables
- `MAILTO=root`: Send output emails to root user

**Cron Schedule Line**:
- `0 * * * *`: Run at minute 0 of every hour (hourly)
- `ls -la $(find .)`: List all files recursively with details
- `| sed -e 's/..csv/#####.csv/g'`: Replace ".csv" with "#####.csv"
- `> /home/ec2-user/companyA/SharedFolders/filteredAudit.csv`: Write to file

**Result**: Creates an audit file every hour with CSV filenames masked for privacy.

#### Save and Exit

1. Press `ESC` to exit insert mode
2. Type `:wq` and press Enter to save and quit

#### Validate Cron Job

List all cron jobs to verify:
```bash
sudo crontab -l
```

Expected output shows your configured cron job:
```
SHELL=/bin/bash
PATH=/usr/bin:/bin:/usr/local/bin
MAILTO=root
0 * * * * ls -la $(find .) | sed -e 's/..csv/#####.csv/g' > /home/ec2-user/companyA/SharedFolders/filteredAudit.csv
```

Ensure the text matches exactly—cron is sensitive to syntax errors.

## Key Concepts Covered

### Process Management

A **process** is an instance of a running program. Every process has:
- **PID**: Unique process identifier
- **PPID**: Parent process ID
- **UID**: User ID of owner
- **State**: Current status (running, sleeping, etc.)
- **Priority**: Scheduling importance
- **Resources**: Memory and CPU allocation

### Process States

- **Running (R)**: Currently executing on CPU
- **Sleeping (S)**: Waiting for event or resource (interruptible)
- **Disk Sleep (D)**: Waiting for I/O (uninterruptible)
- **Stopped (T)**: Paused by signal (Ctrl+Z)
- **Zombie (Z)**: Terminated but parent hasn't acknowledged

### System Monitoring

**ps**: Snapshot of current processes
**top**: Real-time process monitoring
**htop**: Enhanced version of top (if installed)
**uptime**: System load and uptime
**free**: Memory usage
**vmstat**: Virtual memory statistics

### Cron Daemon

Background service that executes scheduled tasks. Runs continuously and checks crontab files every minute for jobs to execute.

### Crontab File

Text file containing cron job definitions. Each user can have their own crontab, plus system-wide crontabs exist in `/etc/cron.d/` and `/etc/crontab`.

## Essential Commands Reference

### Process Commands

| Command | Purpose |
|---------|---------|
| `ps aux` | List all processes |
| `ps -ef` | Full format process listing |
| `ps -u username` | Processes for specific user |
| `pgrep processname` | Find process ID by name |
| `pidof processname` | Get PID of running program |
| `kill PID` | Terminate process gracefully |
| `kill -9 PID` | Force kill process |
| `killall processname` | Kill all processes by name |
| `pkill processname` | Kill processes matching pattern |

### Monitoring Commands

| Command | Purpose |
|---------|---------|
| `top` | Real-time process viewer |
| `top -u username` | Show processes for user |
| `htop` | Interactive process viewer |
| `uptime` | System load averages |
| `free -h` | Memory usage (human-readable) |
| `vmstat 1` | Virtual memory stats every second |
| `iostat` | CPU and I/O statistics |
| `mpstat` | Multi-processor statistics |

### Cron Commands

| Command | Purpose |
|---------|---------|
| `crontab -e` | Edit user's crontab |
| `crontab -l` | List user's cron jobs |
| `crontab -r` | Remove user's crontab |
| `sudo crontab -e` | Edit root's crontab |
| `sudo crontab -l` | List root's cron jobs |
| `sudo crontab -u user -e` | Edit another user's crontab |

## Crontab Schedule Examples

### Common Schedules

```bash
# Every minute
* * * * * command

# Every hour at minute 0
0 * * * * command

# Every day at midnight
0 0 * * * command

# Every day at 3:30 AM
30 3 * * * command

# Every Monday at 9 AM
0 9 * * 1 command

# First day of month at midnight
0 0 1 * * command

# Every 15 minutes
*/15 * * * * command

# Every 6 hours
0 */6 * * * command

# Weekdays at 8 AM
0 8 * * 1-5 command

# Multiple times (8 AM, 12 PM, 6 PM)
0 8,12,18 * * * command
```

### Special Strings

```bash
@reboot command      # Run at system startup
@yearly command      # Run once a year (0 0 1 1 *)
@annually command    # Same as @yearly
@monthly command     # Run once a month (0 0 1 * *)
@weekly command      # Run once a week (0 0 * * 0)
@daily command       # Run once a day (0 0 * * *)
@midnight command    # Same as @daily
@hourly command      # Run once an hour (0 * * * *)
```

## Practical Examples

### Process Management

```bash
# Find all Apache processes
ps aux | grep httpd

# Kill all zombie processes (carefully!)
ps aux | grep 'Z' | awk '{print $2}' | xargs kill -9

# Show processes sorted by memory usage
ps aux --sort=-%mem | head -10

# Show process tree
ps auxf

# Monitor specific process
watch -n 1 'ps aux | grep myapp'
```

### System Monitoring

```bash
# Check system load
uptime

# Monitor memory continuously
watch -n 2 free -h

# Check CPU usage
mpstat 1 5  # 5 samples, 1 second apart

# Monitor disk I/O
iostat -x 2  # Extended stats every 2 seconds

# Check running processes count
ps aux | wc -l
```

### Cron Automation

```bash
# Backup database daily at 2 AM
0 2 * * * /usr/local/bin/backup-database.sh

# Clean temp files every Sunday at midnight
0 0 * * 0 rm -rf /tmp/*

# Check disk space every hour
0 * * * * df -h > /var/log/disk-usage.log

# Send report every weekday at 5 PM
0 17 * * 1-5 /usr/local/bin/daily-report.sh

# Restart service every 6 hours
0 */6 * * * systemctl restart myservice

# Log system stats every 10 minutes
*/10 * * * * date >> /var/log/uptime.log && uptime >> /var/log/uptime.log
```

## Troubleshooting Tips

### Process Issues
- **High CPU usage**: Use `top` to identify culprit, press `P` to sort by CPU
- **Process won't die**: Try `kill -9 PID` for force kill
- **Can't find process**: Use `pgrep` or `ps aux | grep process_name`
- **Too many processes**: Check for runaway scripts or fork bombs

### Cron Issues
- **Job not running**: Check cron service status: `systemctl status cron`
- **No email notification**: Verify MAILTO is set correctly
- **Path issues**: Use absolute paths for commands and files
- **Syntax errors**: Validate with `crontab -l` after editing
- **Timing confusion**: Remember cron uses 24-hour time
- **Debugging**: Check logs in `/var/log/cron` or `/var/log/syslog`

### Top Command Issues
- **Display corrupted**: Resize terminal window or press `Ctrl+L`
- **Can't interact**: Ensure terminal is focused, try pressing keys again
- **Want to kill process**: Press `k`, enter PID, then signal number (9 for force)

## Important Notes

- This lab builds on all previous Linux administration knowledge
- Cron jobs run with limited environment variables—use absolute paths
- System load averages represent number of processes waiting for CPU
- Zombie processes usually indicate parent process issues
- Root's crontab is separate from user crontabs
- Cron output is emailed to MAILTO address if command produces output
- Always test cron jobs manually before scheduling

## Best Practices

### Process Management
- Monitor system regularly to catch issues early
- Understand normal baseline before troubleshooting
- Use appropriate signals: SIGTERM (15) before SIGKILL (9)
- Clean up zombie processes by fixing parent processes
- Document resource-intensive processes
- Set process priorities with `nice` and `renice`

### System Monitoring
- Establish performance baselines for your systems
- Set up alerts for abnormal resource usage
- Monitor trends over time, not just current state
- Check load averages: values > CPU count indicate saturation
- Regular memory monitoring prevents OOM (Out of Memory) kills
- Use proper monitoring tools for production (Prometheus, Nagios, etc.)

### Cron Best Practices
- Use full paths for commands: `/usr/bin/python3` not `python3`
- Redirect output to files for logging: `>> /var/log/myjob.log 2>&1`
- Test commands manually before adding to crontab
- Comment your cron jobs for future reference
- Set appropriate email notifications
- Don't overlap long-running jobs—check previous run completed
- Use locking mechanisms to prevent simultaneous executions
- Keep cron scripts simple—complex logic goes in external scripts

### Example Well-Documented Crontab

```bash
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
MAILTO=admin@example.com

# Daily database backup at 2 AM
0 2 * * * /usr/local/bin/backup-db.sh >> /var/log/backup.log 2>&1

# Weekly log rotation on Sundays at midnight
0 0 * * 0 /usr/sbin/logrotate /etc/logrotate.conf

# Check disk space every 6 hours and alert if low
0 */6 * * * /usr/local/bin/check-disk-space.sh

# Generate hourly reports
0 * * * * /opt/myapp/bin/generate-report.sh
```

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting (Command Host instance)
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **systemd Timers**: Modern alternative to cron
- **Process Priorities**: nice and renice commands
- **Process Signals**: Understanding SIGHUP, SIGTERM, SIGKILL
- **Background Jobs**: Using `&`, `bg`, `fg`, `jobs`
- **Screen/Tmux**: Terminal multiplexers for persistent sessions
- **Monitoring Tools**: Nagios, Prometheus, Grafana, Zabbix
- **Resource Limits**: ulimit and /etc/security/limits.conf
- **Process Accounting**: Tracking process resource usage
- **Advanced Cron**: anacron for systems not always running
- **Systemd Services**: Creating and managing services
- **Load Balancing**: Distributing processes across CPUs
- **Container Monitoring**: Docker and Kubernetes process management

## Practice Exercises

To reinforce your learning:

1. **Create monitoring script** that logs CPU and memory usage hourly
2. **Set up backup job** that runs nightly and emails results
3. **Monitor web server** and alert if process dies
4. **Create cleanup job** to remove old log files weekly
5. **Build dashboard** combining multiple system metrics
6. **Implement alerting** for high CPU or memory usage
7. **Schedule maintenance** tasks during off-peak hours
8. **Create process audit** that tracks all user-launched processes

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

## Resources

- [ps Command Manual](https://linux.die.net/man/1/ps)
- [top Command Manual](https://linux.die.net/man/1/top)
- [cron Manual](https://linux.die.net/man/8/cron)
- [crontab Manual](https://linux.die.net/man/5/crontab)
- [Crontab Generator](https://crontab.guru/)
- [Linux Process Management](https://www.redhat.com/sysadmin/linux-process-management)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓
