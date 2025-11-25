# Working with Commands Lab

## Overview

This lab teaches you powerful Linux text processing and data manipulation commands that are essential for system administration, log analysis, and data processing tasks. You'll learn how to redirect output, sort data, extract specific fields, search for patterns, and perform text substitutions—skills that enable efficient automation and data processing in production environments. These commands form the foundation of shell scripting and command-line productivity.

## Learning Objectives

By completing this lab, you will be able to:

- Use the tee command to direct output to both screen and file simultaneously
- Sort data within CSV files using the sort command
- Extract specific fields from delimited files with the cut command
- Perform text substitution using the sed (stream editor) command
- Chain commands together using the pipe (|) operator
- Create and manipulate CSV files from the command line
- Combine multiple commands for complex data processing tasks

## Lab Duration

Approximately 30 minutes

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux EC2 instance
- Familiarity with basic Linux commands and file operations
- Understanding of file creation and text editing

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux
- **SSH Connection**: Secure remote access to instance
- **Command-line Tools**: tee, sort, cut, sed, grep, cat (standard Unix utilities)

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

### Task 2: Use the tee Command

Learn how to duplicate output to both the terminal and a file.

#### Verify Location

```bash
pwd
# Expected output: /home/ec2-user
```

#### Use tee to Capture Output

Execute hostname and write to both screen and file:
```bash
hostname | tee file1.txt
```

Expected output:
```
ip-10-0-10-81.us-west-2.compute.internal
```

**Command breakdown**:
- `hostname`: Displays the system's hostname
- `|`: Pipe operator (sends output of first command to second)
- `tee file1.txt`: Writes to both terminal and file1.txt

**Result**: The hostname appears on screen AND is written to file1.txt.

#### Verify File Creation

```bash
ls
# Output: companyA  file1.txt
```

#### Understanding tee

The `tee` command reads from standard input and writes to:
1. Standard output (your terminal screen)
2. One or more files

This is extremely useful for:
- Logging command output while monitoring in real-time
- Debugging scripts while saving output
- Creating audit trails of command execution

### Task 3: Use the sort Command and Pipe Operator

Learn to sort data and chain commands together.

#### Verify Location

```bash
pwd
# Expected output: /home/ec2-user
```

#### Create Test CSV File

Create a CSV file with factory and store data:
```bash
cat > test.csv
```

Type the following lines, pressing Enter after each:
```
Factory, 1, Paris
Store, 2, Dubai
Factory, 3, Brasilia
Store, 4, Algiers
Factory, 5, Tokyo
```

Press `Ctrl+D` to finish and save the file.

#### Verify File Creation

```bash
ls
# Should now show test.csv
```

#### Sort the CSV File

Sort the contents alphabetically and numerically:
```bash
sort test.csv
```

Expected output:
```
Factory, 1, Paris
Factory, 3, Brasilia
Factory, 5, Tokyo
Store, 2, Dubai
Store, 4, Algiers
```

**How sort works**:
- Default sorting is alphabetical (Factory before Store)
- Within each category, sorts by the next field numerically
- Sorts entire lines, not individual fields

#### Search Using Pipe Operator

Find the Paris factory using command chaining:
```bash
grep Paris test.csv
```

Expected output:
```
Factory, 1, Paris
```

**Command breakdown**:
- `grep`: Searches for patterns in text
- `Paris`: The pattern to search for
- `test.csv`: File to search in

**Alternative with pipe**:
```bash
cat test.csv | grep Paris
```

This reads the file, then pipes the content to grep for searching.

### Task 4: Use the cut Command

Extract specific fields from delimited files.

#### Verify Location

```bash
pwd
# Expected output: /home/ec2-user
```

#### Create Cities CSV File

Create a new CSV file with city and state data:
```bash
cat > cities.csv
```

Type the following lines, pressing Enter after each:
```
Dallas, Texas
Seattle, Washington
Los Angeles, California
Atlanta, Georgia
New York, New York
```

Press `Ctrl+D` to finish and save the file.

#### Extract First Field

Use cut to extract only city names:
```bash
cut -d ',' -f 1 cities.csv
```

Expected output:
```
Dallas
Seattle
Los Angeles
Atlanta
New York
```

**Command breakdown**:
- `cut`: Extracts sections from each line
- `-d ','`: Delimiter is comma (separates fields)
- `-f 1`: Extract field 1 (first field)
- `cities.csv`: Input file

#### Additional cut Examples

Extract the second field (states):
```bash
cut -d ',' -f 2 cities.csv
```

Output:
```
 Texas
 Washington
 California
 Georgia
 New York
```

Note the leading space—this is part of the data after the comma.

Extract multiple fields:
```bash
cut -d ',' -f 1,2 cities.csv
```

This displays both city and state.

### Additional Challenge: Use the sed Command

Perform text substitution using the stream editor.

#### Understanding sed Syntax

Basic sed replacement syntax:
```bash
sed 's/pattern/replacement/' filename
```

- `s`: Substitute command
- `pattern`: Text to find
- `replacement`: Text to replace with
- `/`: Delimiter (can be other characters too)

#### Replace Commas with Periods

Replace the first comma in each line with a period in cities.csv:
```bash
sed 's/,/./' cities.csv
```

Expected output:
```
Dallas. Texas
Seattle. Washington
Los Angeles. California
Atlanta. Georgia
New York. New York
```

#### Process Multiple Files with Chaining

Use command chaining to process both files:
```bash
sed 's/,/./' cities.csv && sed 's/,/./' test.csv
```

Or combine outputs:
```bash
cat cities.csv test.csv | sed 's/,/./'
```

Expected combined output:
```
Dallas. Texas
Seattle. Washington
Los Angeles. California
Atlanta. Georgia
New York. New York
Factory. 1, Paris
Store. 2, Dubai
Factory. 3, Brasilia
Store. 4, Algiers
Factory. 5, Tokyo
```

**Note**: `sed 's/,/./'` only replaces the FIRST comma on each line. To replace all commas, use `sed 's/,/./g'` (global flag).

## Key Concepts Covered

### Standard Input/Output Streams

Linux uses three standard streams:
- **stdin (0)**: Standard input (keyboard)
- **stdout (1)**: Standard output (terminal screen)
- **stderr (2)**: Standard error (error messages)

### Pipe Operator (|)

Connects the output of one command to the input of another, enabling powerful command chaining:
```bash
command1 | command2 | command3
```

Each command processes data and passes results to the next.

### Redirection Operators

- `>`: Redirect output to file (overwrite)
- `>>`: Redirect output to file (append)
- `<`: Redirect input from file
- `2>`: Redirect error messages
- `&>`: Redirect both output and errors

### Text Processing Commands

**tee**: Duplicates output to file and screen
**sort**: Arranges lines in order
**cut**: Extracts fields from delimited text
**sed**: Stream editor for text transformation
**grep**: Searches for patterns in text

### Delimiters

Characters that separate fields in structured text:
- Comma (`,`): CSV files
- Tab (`\t`): TSV files
- Colon (`:`): `/etc/passwd` file
- Space: Many log files

## Essential Commands Reference

### tee Command

| Command | Purpose |
|---------|---------|
| `command \| tee file.txt` | Write to screen and file |
| `command \| tee -a file.txt` | Append to file |
| `command \| tee file1 file2` | Write to multiple files |
| `command \| tee file.txt \| command2` | Continue piping after tee |

### sort Command

| Command | Purpose |
|---------|---------|
| `sort file.txt` | Sort alphabetically |
| `sort -r file.txt` | Sort in reverse order |
| `sort -n file.txt` | Sort numerically |
| `sort -k2 file.txt` | Sort by field 2 |
| `sort -u file.txt` | Sort and remove duplicates |
| `sort -t',' -k2 file.csv` | Sort CSV by column 2 |

### cut Command

| Command | Purpose |
|---------|---------|
| `cut -d',' -f1 file.csv` | Extract field 1 (comma-delimited) |
| `cut -d':' -f1,3 file.txt` | Extract fields 1 and 3 |
| `cut -c1-5 file.txt` | Extract characters 1-5 |
| `cut -d' ' -f2- file.txt` | Extract field 2 onwards |

### sed Command

| Command | Purpose |
|---------|---------|
| `sed 's/old/new/' file.txt` | Replace first occurrence per line |
| `sed 's/old/new/g' file.txt` | Replace all occurrences |
| `sed 's/old/new/2' file.txt` | Replace second occurrence per line |
| `sed '/pattern/d' file.txt` | Delete lines matching pattern |
| `sed -i 's/old/new/g' file.txt` | Edit file in-place |
| `sed -n '1,5p' file.txt` | Print lines 1-5 |

### grep Command

| Command | Purpose |
|---------|---------|
| `grep pattern file.txt` | Search for pattern |
| `grep -i pattern file.txt` | Case-insensitive search |
| `grep -v pattern file.txt` | Invert match (exclude pattern) |
| `grep -r pattern directory/` | Recursive search |
| `grep -n pattern file.txt` | Show line numbers |
| `grep -c pattern file.txt` | Count matches |

## Practical Examples

### Log Analysis
```bash
# Find errors in log file
grep ERROR /var/log/application.log

# Count error occurrences
grep -c ERROR /var/log/application.log

# Extract timestamps from errors
grep ERROR /var/log/application.log | cut -d' ' -f1-2

# Sort errors by frequency
grep ERROR /var/log/application.log | sort | uniq -c | sort -rn
```

### CSV Processing
```bash
# Extract email addresses (field 3)
cut -d',' -f3 users.csv

# Sort by last name (field 2)
sort -t',' -k2 users.csv

# Remove duplicate entries
sort -u users.csv

# Replace delimiter
sed 's/,/|/g' users.csv
```

### Data Cleaning
```bash
# Remove leading/trailing spaces
sed 's/^ *//; s/ *$//' file.txt

# Convert to lowercase
sed 's/.*/\L&/' file.txt

# Remove blank lines
sed '/^$/d' file.txt

# Remove comments (lines starting with #)
sed '/^#/d' config.txt
```

### Command Chaining
```bash
# Complex data processing pipeline
cat data.csv | \
  grep -v "^#" | \           # Remove comments
  cut -d',' -f1,3 | \        # Extract fields 1 and 3
  sort -u | \                # Remove duplicates
  sed 's/,/ - /' | \         # Change delimiter
  tee output.txt             # Save and display
```

## Troubleshooting Tips

- **sed not changing file**: Use `-i` flag for in-place editing or redirect output
- **cut showing wrong field**: Check delimiter with `-d` option
- **sort not working correctly**: Use `-n` for numeric sort
- **Pipe not working**: Verify each command works independently first
- **Special characters in sed**: Escape with backslash or use different delimiter
- **tee permission denied**: Add `sudo` if writing to protected location

## Important Notes

- This lab builds on all previous courseware knowledge
- Commands shown do not modify original files unless using `-i` flag
- Pipe operator connects commands sequentially
- `Ctrl+D` signals end-of-file when creating files with cat
- sed uses regular expressions for pattern matching
- Always test commands on sample data before production use

## Best Practices

### Data Processing
- **Test First**: Try commands on small datasets before large files
- **Backup Data**: Copy files before in-place editing with sed `-i`
- **Verify Output**: Check results before overwriting files
- **Use Pipelines**: Chain commands for efficiency
- **Document Transformations**: Comment complex sed expressions

### Script Development
```bash
#!/bin/bash
# Process sales data CSV

# Extract sales over $1000
cat sales.csv | \
  grep -v "^#" | \              # Remove comments
  cut -d',' -f2,3 | \           # Get date and amount
  awk -F',' '$2 > 1000' | \     # Filter amounts > 1000
  sort -t',' -k2 -rn | \        # Sort by amount descending
  tee high_sales.csv            # Save and display
```

### Performance Considerations
- Use `grep` before other commands to reduce data early
- Avoid unnecessary pipes—some commands can do multiple tasks
- For large files, consider `awk` instead of multiple pipes
- Use `head` or `tail` to test on file subsets

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting (Command Host instance)
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **awk**: Powerful text processing language
- **Regular Expressions**: Advanced pattern matching
- **xargs**: Build command lines from input
- **tr**: Translate or delete characters
- **paste**: Merge files side-by-side
- **join**: Merge files by common field
- **uniq**: Report or filter repeated lines
- **wc**: Word, line, character counts
- **diff**: Compare files line by line
- **comm**: Compare sorted files
- **Column**: Format output in columns
- **jq**: Process JSON from command line
- **csvkit**: Advanced CSV processing tools

## Practice Exercises

To reinforce your learning:

1. **Log Analysis**: Extract all IP addresses from Apache access logs
2. **CSV Manipulation**: Sort employee data by salary, extract highest paid
3. **Text Cleanup**: Remove duplicates from contact list
4. **Data Transformation**: Convert tab-delimited to comma-delimited
5. **Report Generation**: Count occurrences of each error type in logs
6. **Batch Renaming**: Use sed to generate mv commands for file renaming
7. **Configuration Migration**: Replace old server names with new ones in config files

## Related Labs

- Introduction to Amazon EC2
- Introduction to Amazon Linux AMI
- Linux Command Line
- Managing Users and Groups
- Editing Files
- Working with the File System
- Working with Files
- Managing File Permissions

## Resources

- [GNU Coreutils Manual](https://www.gnu.org/software/coreutils/manual/)
- [sed Manual](https://www.gnu.org/software/sed/manual/)
- [grep Manual](https://www.gnu.org/software/grep/manual/)
- [Regular Expression Tutorial](https://www.regular-expressions.info/)
- [Linux Pipeline Examples](https://www.geeksforgeeks.org/piping-in-unix-or-linux/)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025

**Related Labs**: Introduction to Amazon EC2, Introduction to Amazon Linux AMI, Linux Command Line, Managing Users and Groups, Editing Files, Working with the File System, Working with Files, Managing File Permissions