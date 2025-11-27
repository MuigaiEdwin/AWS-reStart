# Bash Shell Scripts Lab

## Overview

Learn to automate boring tasks by writing your first bash script. You'll create a backup script that automatically creates timestamped archives—no more typing the same commands over and over.

## What You'll Learn

- Write a working bash script from scratch
- Use variables to make scripts flexible
- Automatically add timestamps to backup filenames
- Make scripts executable and run them
- Set up automation for daily backups (bonus)

## Duration

25 minutes

## What You'll Build

A script that backs up the CompanyA folder with the current date/time in the filename:
```
2025_11_27_14:30:45-backup-CompanyA.tar.gz
```

No more guessing which backup is which!

---

## Task 1: Connect to Your EC2 Instance

**Windows users:**
1. Download the `.ppk` file
2. Use PuTTY to connect

**Mac/Linux users:**
```bash
cd ~/Downloads
chmod 400 labsuser.pem
ssh -i labsuser.pem ec2-user@<public-ip>
```

---

## Task 2: Write Your Backup Script

### Step 1: Create the Script File

```bash
pwd  # Make sure you're in /home/ec2-user
touch backup.sh
chmod 755 backup.sh  # Make it executable
```

**What `chmod 755` means:**
- Owner can read, write, and execute (7)
- Everyone else can read and execute (5)

### Step 2: Write the Script

Open the file:
```bash
vi backup.sh
```

Press `i` to enter insert mode, then type this:

```bash
#!/bin/bash
DAY="$(date +%Y_%m_%d_%T_%H_%M)"
BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"
tar -csvpzf $BACKUP /home/$USER/CompanyA
```

Save and exit: Press `Esc`, then type `:wq` and press Enter.

### Understanding the Script

Let's break down each line:

**Line 1: The Shebang**
```bash
#!/bin/bash
```
Tells the system "run this script with bash." Always the first line.

**Line 2: Create Date Variable**
```bash
DAY="$(date +%Y_%m_%d_%T_%H_%M)"
```
- `date` command gets current date/time
- Format: `2025_11_27_14:30:45_14_30`
- Stored in variable called `DAY`
- Use it later with `$DAY`

**Line 3: Build Backup Filename**
```bash
BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"
```
- `$USER` = current username (ec2-user)
- `$DAY` = the date we just created
- Creates: `/home/ec2-user/backups/2025_11_27-backup-CompanyA.tar.gz`

**Line 4: Create the Backup**
```bash
tar -csvpzf $BACKUP /home/$USER/CompanyA
```
- Archives the CompanyA folder
- Uses the filename we built in `$BACKUP`
- Same tar command from before, but automated!

### Step 3: Run Your Script

```bash
./backup.sh
```

You'll see output showing each file being backed up:
```
tar: Removing leading `/' from member names
/home/ec2-user/CompanyA/
/home/ec2-user/CompanyA/Management/
/home/ec2-user/CompanyA/Management/Sections.csv
...
```

### Step 4: Verify It Worked

```bash
ls backups/
```

You should see something like:
```
2025_11_27_14:30:45_14_30-backup-CompanyA.tar.gz
```

**Success!** Your script created a backup with today's date in the filename.

---

## Why This Matters

**Before:** Manual backups
```bash
tar -cvzf backup1.tar.gz CompanyA  # Wait, which backup is this?
tar -cvzf backup2.tar.gz CompanyA  # What date was backup1?
```

**After:** Automated with timestamps
```bash
./backup.sh  # Done! Clear filename with date/time
```

Every backup has a unique, sortable name. No more confusion!

---

## Quick Reference

### Essential Script Components

```bash
#!/bin/bash                    # Shebang line (always first)
VARIABLE="value"               # Create variable
$VARIABLE                      # Use variable
$(command)                     # Run command and capture output
```

### Useful Date Formats

```bash
date +%Y        # Year: 2025
date +%m        # Month: 11
date +%d        # Day: 27
date +%H        # Hour: 14
date +%M        # Minute: 30
date +%Y-%m-%d  # Combined: 2025-11-27
```

### File Permissions

```bash
chmod 755 script.sh   # Owner: rwx, Others: r-x
chmod +x script.sh    # Just make executable
ls -l script.sh       # Check permissions
```

---

## Bonus: Automate with Cron

Want this to run automatically every day at 2 AM?

```bash
crontab -e
```

Add this line:
```bash
0 2 * * * /home/ec2-user/backup.sh
```

Now your backups happen automatically while you sleep!

---

## Common Issues & Fixes

**"Permission denied" when running script**
```bash
chmod +x backup.sh  # Make it executable
```

**"backups: No such file or directory"**
```bash
mkdir ~/backups  # Create the folder first
```

**Script runs but creates no file**
```bash
# Check if you have write permission
ls -ld ~/backups

# Make sure folder exists
mkdir -p ~/backups
```

**Wrong date format**
```bash
# Test date command separately first
date +%Y_%m_%d
```

---

## Try These Modifications

Once your script works, experiment:

### 1. Add a Success Message
```bash
#!/bin/bash
DAY="$(date +%Y_%m_%d)"
BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"
tar -csvpzf $BACKUP /home/$USER/CompanyA
echo "Backup complete! Saved to $BACKUP"
```

### 2. Delete Old Backups (Keep Last 7 Days)
```bash
#!/bin/bash
DAY="$(date +%Y_%m_%d)"
BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"
tar -csvpzf $BACKUP /home/$USER/CompanyA

# Delete backups older than 7 days
find /home/$USER/backups -name "*-backup-CompanyA.tar.gz" -mtime +7 -delete
echo "Backup complete! Old backups cleaned up."
```

### 3. Accept Folder Name as Parameter
```bash
#!/bin/bash
FOLDER=$1  # First parameter passed to script
DAY="$(date +%Y_%m_%d)"
BACKUP="/home/$USER/backups/$DAY-backup-$FOLDER.tar.gz"
tar -csvpzf $BACKUP /home/$USER/$FOLDER
echo "Backed up $FOLDER to $BACKUP"
```

Use it:
```bash
./backup.sh CompanyA
./backup.sh Documents
```

---

## Real-World Script Ideas

Now that you know the basics, try building:

1. **Log cleaner** - Delete logs older than 30 days
2. **System info** - Gather disk space, memory, CPU into one report
3. **File organizer** - Sort downloads by file type
4. **Git backup** - Commit and push changes automatically
5. **Health check** - Check if services are running, restart if needed

---

## Quick Tips

- **Test before automating** - Run manually first
- **Add comments** - Future you will thank you
- **Use meaningful variable names** - `BACKUP` not just `B`
- **Check exit codes** - `$?` tells you if last command worked
- **Quote variables** - Use `"$VARIABLE"` not `$VARIABLE`

---

## Related Labs

- The Bash Shell (aliases and PATH)
- Working with Files (tar commands)
- Managing Processes (cron jobs)

## Resources

- [Bash Scripting Tutorial](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)
- [Bash Guide for Beginners](https://tldp.org/LDP/Bash-Beginners-Guide/html/)
- [ShellCheck](https://www.shellcheck.net/) - Check your scripts for errors

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025