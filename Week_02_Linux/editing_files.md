# Editing Files Lab

## Overview

This lab introduces you to essential Linux text editors—Vim and nano—which are fundamental tools for system administrators and developers working in command-line environments. You'll learn how to create, edit, and save files using both editors, understanding when to use each based on your needs and preferences. These skills are critical for configuration file management, scripting, and system administration tasks.

## Learning Objectives

By completing this lab, you will be able to:

- Use vimtutor to learn Vim basics through lessons 1-3
- Navigate and edit files in Vim using command and insert modes
- Create, modify, and save files with the Vim editor
- Use nano as an alternative text editor for simpler editing tasks
- Copy and edit content from system log files
- Understand the differences between modal and modeless editors

## Lab Duration

Approximately 1 hour

## Prerequisites

- Completion of previous AWS and Linux courseware labs
- SSH access to Amazon Linux EC2 instance
- Familiarity with basic Linux commands
- Understanding of file system navigation

## Lab Architecture

This lab uses the following AWS resources:

- **Amazon EC2 Instance**: Command Host running Amazon Linux
- **SSH Connection**: Secure remote access to instance
- **Text Editors**: Vim and nano pre-installed or installable via yum
- **System Files**: Access to `/var/log/secure` for practice editing

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

### Task 2: Run the Vim Tutorial

Learn Vim fundamentals through an interactive tutorial application.

#### Starting Vimtutor

Launch the Vim tutorial:
```bash
vimtutor
```

**Note**: If vimtutor doesn't work, install Vim first:
```bash
sudo yum install vim
```

#### Complete Lessons 1-3

Work through the following tutorial sections:

**Lesson 1: Basic Navigation and Editing**
- Moving the cursor with h, j, k, l keys
- Entering and exiting Vim
- Deleting characters and lines
- Undo functionality

**Lesson 2: Deletion Commands**
- Deleting words
- Deleting to end of line
- Using motion commands with operators

**Lesson 3: Text Manipulation**
- Put command (paste)
- Replace command
- Change operator

#### Exiting Vimtutor

When you've completed lessons 1-3, exit the tutorial:
```bash
:q!
```

Press Enter to return to your terminal.

### Task 3: Edit a File in Vim

Apply your Vim knowledge by creating and editing a real file.

#### Creating a New File

Open a new file named `helloworld` in Vim:
```bash
vim helloworld
```

This creates the file and opens the Vim editor.

#### Adding Content

1. Press `i` to enter **INSERT** mode (you'll see `-- INSERT --` at bottom left)
2. Type the following text:
   ```
   Hello World!
   This is my first file in Linux and I am editing it in Vim!
   ```
3. Press `ESC` to exit INSERT mode and return to COMMAND mode

#### Saving and Quitting

Save your changes and exit:
```bash
:wq
```

**Command breakdown**:
- `:` enters command-line mode
- `w` writes (saves) the file
- `q` quits Vim

#### Reopening and Adding More Content

Open the file again:
```bash
vim helloworld
# Or use up arrow to recall the last command
```

1. Press `i` to enter INSERT mode
2. Add this new line:
   ```
   I learned how to create a file, edit and save them too!
   ```
3. Press `ESC` to exit INSERT mode
4. Type `:q!` and press Enter to quit **without saving**

#### Verification Exercise

Reopen the file to verify what happened:
```bash
vim helloworld
```

**Question**: What do you notice? The third line is missing because you used `:q!` (quit without saving) instead of `:wq` (write and quit).

#### Additional Vim Commands Challenge

Try these useful Vim commands:

**Delete entire line**:
```bash
dd
```
Position cursor on any line in COMMAND mode, then press `dd`

**Undo last command**:
```bash
u
```
Press `u` in COMMAND mode to undo the deletion

**Save without quitting**:
```bash
:w
```
Saves changes but keeps Vim open for continued editing

### Task 4: Edit a File in Nano

Learn nano as an alternative, user-friendly text editor.

#### Creating a File in Nano

Open a new file named `cloudworld` in nano:
```bash
nano cloudworld
```

Unlike Vim, nano opens ready to type—no insert mode needed!

#### Adding Content

Simply start typing (no mode switching required):
```
We are using nano this time! We can simply start typing! No insert mode needed.
```

#### Saving in Nano

To save your changes:
1. Press `Ctrl+O` (WriteOut)
2. Press `Enter` to confirm the filename
3. You'll see "File Name to Write: cloudworld" at the bottom

#### Exiting Nano

To exit the editor:
```bash
Ctrl+X
```

#### Verification

Reopen the file to verify it saved correctly:
```bash
nano cloudworld
```

Confirm the content is saved, then exit with `Ctrl+X`.

## Key Concepts Covered

### Vim Editor
A powerful, modal text editor available on virtually all Unix-like systems. It has a steep learning curve but offers exceptional efficiency for experienced users.

**Vim Modes**:
- **COMMAND mode**: Default mode for navigation and commands (press ESC to enter)
- **INSERT mode**: For typing and editing text (press `i` to enter)
- **VISUAL mode**: For selecting text (press `v` to enter)
- **COMMAND-LINE mode**: For executing commands (press `:` to enter)

### Nano Editor
A simple, user-friendly text editor that's easier to learn than Vim. It's modeless—you can start typing immediately without mode switching. Ideal for quick edits and beginners.

### Modal vs. Modeless Editors
- **Modal (Vim)**: Different modes for different tasks; more efficient but requires learning
- **Modeless (nano)**: Single mode; easier to learn but potentially less efficient for complex edits

### File Editing Workflow
1. Open file with editor
2. Make changes
3. Save changes
4. Exit editor
5. Verify changes (best practice)

## Essential Commands Reference

### Vim Commands

| Command | Purpose |
|---------|---------|
| `vim filename` | Open file in Vim |
| `i` | Enter INSERT mode |
| `ESC` | Exit INSERT mode (return to COMMAND mode) |
| `:w` | Save (write) file |
| `:q` | Quit Vim |
| `:wq` or `:x` | Save and quit |
| `:q!` | Quit without saving (discard changes) |
| `dd` | Delete entire line |
| `u` | Undo last change |
| `Ctrl+r` | Redo |
| `yy` | Copy (yank) line |
| `p` | Paste below cursor |
| `/search` | Search for "search" |
| `n` | Next search result |

### Nano Commands

| Command | Purpose |
|---------|---------|
| `nano filename` | Open file in nano |
| `Ctrl+O` | Save file (WriteOut) |
| `Ctrl+X` | Exit nano |
| `Ctrl+K` | Cut line |
| `Ctrl+U` | Paste (Uncut) |
| `Ctrl+W` | Search |
| `Ctrl+\` | Search and replace |
| `Ctrl+G` | Display help |
| `Ctrl+C` | Show cursor position |

### Vim Navigation

| Key | Direction |
|-----|-----------|
| `h` | Left |
| `j` | Down |
| `k` | Up |
| `l` | Right |
| `0` | Beginning of line |
| `$` | End of line |
| `gg` | First line of file |
| `G` | Last line of file |

## When to Use Which Editor

### Use Vim When:
- Working on remote servers where GUI isn't available
- Editing large files that require efficient navigation
- Performing complex text manipulations
- You need powerful search and replace capabilities
- Working in environments where Vim is the standard

### Use Nano When:
- Making quick, simple edits
- You're a beginner learning Linux
- Editing configuration files with straightforward changes
- You prefer a simpler, more intuitive interface
- Time is limited and you need quick edits

## Troubleshooting Tips

### Vim Issues
- **Stuck in INSERT mode**: Press `ESC` to return to COMMAND mode
- **Can't type anything**: You're in COMMAND mode; press `i` to enter INSERT mode
- **Command not working**: Ensure you're in the correct mode (press `ESC` first)
- **Can't exit Vim**: Press `ESC`, then type `:q!` and press Enter
- **Changes not saved**: Use `:wq` not `:q!` to save before quitting

### Nano Issues
- **Ctrl commands not working**: Ensure Caps Lock is off
- **File won't save**: Check file permissions and disk space
- **Accidentally closed**: Reopen with `nano filename`; unsaved changes are lost

### General Issues
- **Editor not found**: Install with `sudo yum install vim` or `sudo yum install nano`
- **Permission denied**: Use `sudo` before the editor command for system files
- **File already open**: Close other instances or use `:e!` in Vim to force reload

## Important Notes

- This lab builds on knowledge from previous AWS and Linux courseware
- Vim has a steep learning curve but is worth learning for efficiency
- Nano is more beginner-friendly and sufficient for simple edits
- Always verify your edits by reopening the file
- Use `:q!` to discard changes; use `:wq` to save changes
- Bottom of screen shows available commands in nano
- Practice regularly to build muscle memory for Vim commands

## Best Practices

- **Save frequently**: Use `:w` in Vim or `Ctrl+O` in nano regularly
- **Verify changes**: Reopen files to confirm edits saved correctly
- **Use version control**: For important files, use Git or backups
- **Learn gradually**: Master basic Vim commands before advanced features
- **Choose the right tool**: Use Vim for efficiency, nano for simplicity
- **Practice vimtutor**: Complete all lessons for comprehensive Vim knowledge
- **Keep cheat sheets**: Reference command lists until memorized

## AWS Services Used

- **Amazon EC2**: Virtual machine hosting (Command Host instance)
- **AWS Management Console**: Service access and management

## Advanced Topics to Explore

After completing this lab, expand your knowledge:

- **Advanced Vim Features**: Macros, buffers, windows, and tabs
- **Vim Plugins**: Extend functionality with NERDTree, CtrlP, and more
- **Vim Configuration**: Customize `.vimrc` for personalized setup
- **Regular Expressions**: Powerful search and replace in Vim
- **Visual Block Mode**: Edit multiple lines simultaneously
- **Other Editors**: Emacs, vi (Vim's predecessor), micro, joe
- **IDE Integration**: Use Vim keybindings in modern IDEs
- **Remote Editing**: Edit files over SSH with local editors (SSHFS)
- **Diff and Merge**: Use vimdiff for file comparison
- **Scripting with Vim**: Automate editing tasks with Vimscript

## Practice Exercises

To reinforce your learning:

1. **Vim Challenge**: Edit `/etc/hosts` (with sudo) and add a comment line
2. **Nano Challenge**: Create a simple shell script and make it executable
3. **Speed Test**: Time how fast you can create and save a file in both editors
4. **Search Practice**: Use Vim to search log files for specific error messages
5. **Multi-line Edit**: Practice deleting and undoing multiple lines in Vim

## Related Labs

- Introduction to Amazon EC2
- Introduction to Amazon Linux AMI
- Linux Command Line
- Managing Users and Groups

## Resources

- [Vim Official Documentation](https://www.vim.org/docs.php)
- [Vim Cheat Sheet](https://vim.rtorr.com/)
- [Nano Official Guide](https://www.nano-editor.org/dist/latest/nano.html)
- [Interactive Vim Tutorial](https://www.openvim.com/)
- [Vim Adventures (Game)](https://vim-adventures.com/)
- [AWS EC2 User Guide](https://docs.aws.amazon.com/ec2/index.html)
- [Amazon Linux Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-linux-ami-basics.html)

---

**Lab Status**: Complete ✓

**Last Updated**: November 2025

**Related Labs**: Introduction to Amazon EC2, Introduction to Amazon Linux AMI, Linux Command Line, Managing Users and Groups