# 🐍 Python Programming - Week 05

<div align="center">

```
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

### *A Comprehensive Journey Through Python Fundamentals*
*From Basic Syntax to Advanced Bioinformatics Applications*

</div>

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Installation & Setup](#-installation--setup)
- [Core Programming Concepts](#-core-programming-concepts)
- [Projects & Applications](#-projects--applications)
- [Skill Development](#-skill-development)
- [File Structure](#-file-structure)
- [Usage Examples](#-usage-examples)
- [Learning Outcomes](#-learning-outcomes)

---

## 🌟 Overview

Welcome to Week 05 of Python Programming! This repository represents a comprehensive collection of Python scripts, projects, and exercises designed to build a solid foundation in programming. Through hands-on practice with real-world applications, you'll master everything from basic syntax to complex algorithmic thinking.

This isn't just a collection of random scripts—it's a carefully curated learning path that takes you through the essential building blocks of Python programming. Each file serves a specific purpose in your journey from novice to proficient Python developer.

**What You'll Find Here:**
- 36+ Python scripts covering fundamental to advanced concepts
- Real-world bioinformatics applications working with insulin sequences
- Cryptographic implementations including Caesar cipher variations
- Data processing workflows using JSON and CSV formats
- Debugging exercises that sharpen your problem-solving skills
- File I/O operations demonstrating practical data management

---

## 🛠️ Installation & Setup

### Prerequisites

Before diving into the code, ensure you have the following installed on your system:

```bash
# Check your Python version
$ python3 --version
Python 3.11.0  # or higher

# Verify pip is installed
$ pip3 --version
pip 23.0.1
```

### Getting Started

```bash
# Clone or navigate to the repository
$ cd Week_05_Python_Programming/

# Check the directory structure
$ ls -la
total 36 files

# Make scripts executable (optional)
$ chmod +x *.py

# Run your first script
$ python3 Hello-world.py
Hello, World!
```

### Directory Setup

The project follows a clean, organized structure:

```bash
Week_05_Python_Programming/
├── files/                    # Data directory
│   └── insulin.json         # JSON data for molecular calculations
├── __pycache__/             # Python bytecode cache
│   └── jsonFileHandler.cpython-311.pyc
└── [36 Python scripts]      # Your learning modules
```

---

## 💻 Core Programming Concepts

### 1. **Data Types & Variables** 

Understanding data types is the foundation of programming. These scripts explore Python's built-in types and how to manipulate them effectively.

#### **String Operations** 📝
```bash
$ python3 string-datatype.py
```

Learn string manipulation, concatenation, slicing, and formatting. Strings are immutable sequences in Python, and mastering them is crucial for text processing, data parsing, and user interaction.

**Key Concepts:**
- String methods (`.upper()`, `.lower()`, `.strip()`, `.replace()`)
- String formatting (f-strings, `.format()`, %-formatting)
- String slicing and indexing
- Escape characters and raw strings

#### **Numeric Data** 🔢
```bash
$ python3 numeric-data.py
```

Explore integers, floats, and complex numbers. Understanding numeric types is essential for calculations, scientific computing, and data analysis.

**Key Concepts:**
- Integer operations and bit manipulation
- Float precision and rounding
- Type conversion between numeric types
- Mathematical operators and precedence

### 2. **Collections & Data Structures** 📦

Python's built-in collections are powerful tools for organizing and manipulating data efficiently.

#### **Working with Collections**
```bash
$ python3 collection.py
$ python3 my_collections.py
$ python3 composite-data.py
```

**Lists** - Ordered, mutable sequences perfect for storing collections of items:
```python
# Dynamic arrays that can grow and shrink
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')  # Add items
fruits.sort()          # Sort in place
```

**Tuples** - Immutable sequences ideal for fixed collections:
```python
# Cannot be modified after creation
coordinates = (10.5, 20.3)
rgb_color = (255, 128, 0)
```

**Dictionaries** - Key-value pairs for fast lookups:
```python
# Hash tables for efficient data retrieval
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
```

**Sets** - Unordered collections of unique elements:
```python
# Perfect for membership testing and eliminating duplicates
unique_ids = {101, 102, 103}
```

### 3. **Control Flow & Logic** 🔄

Control structures determine the flow of program execution, allowing for decision-making and repetition.

#### **Conditional Statements**
```bash
$ python3 conditionals.py
$ python3 categorize-values.py
```

Master the art of decision-making in code:
- **if/elif/else** chains for multiple conditions
- **Comparison operators** (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- **Logical operators** (`and`, `or`, `not`)
- **Ternary operators** for concise conditionals
- **Truthiness** and **falsiness** in Python

#### **Loops & Iteration**
```bash
$ python3 for-loop.py
$ python3 while-loopy.py
```

**For Loops** - Iterate over sequences with precision:
```python
# Perfect for known ranges and collections
for i in range(10):
    print(f"Iteration {i}")

for item in collection:
    process(item)
```

**While Loops** - Continue until a condition is met:
```python
# Ideal for unknown iteration counts
while condition_is_true:
    perform_action()
    update_condition()
```

**Loop Control:**
- `break` - Exit loop immediately
- `continue` - Skip to next iteration
- `else` clauses - Execute when loop completes normally

### 4. **Functions & Algorithms** ⚙️

Functions are reusable blocks of code that make programs modular, testable, and maintainable.

#### **Prime Number Algorithms**
```bash
$ python3 prime.py
$ python3 primenumber.py
```

Implement and optimize algorithms for finding prime numbers. Learn about:
- Algorithm design and optimization
- Time complexity analysis
- Mathematical problem-solving
- Function definition and calling
- Return values and parameters

**Prime Checking Logic:**
```python
def is_prime(n):
    """
    Check if a number is prime
    Time complexity: O(√n)
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

---

## 🧬 Projects & Applications

### **Bioinformatics: Insulin Analysis Suite**

This is the crown jewel of Week 05—a complete bioinformatics workflow that analyzes preproinsulin protein sequences. You'll work with real biological data to understand protein structure and properties.

#### **The Biology Behind the Code**

Insulin is a hormone critical for regulating blood glucose. It starts as **preproinsulin**, which undergoes enzymatic cleavage to produce mature insulin. Understanding this process through computational analysis is a fundamental skill in bioinformatics.

#### **Project Files**

```bash
# Original sequence data
$ cat preproinsulin-seq.txt

# Clean, processed sequence (no headers/newlines)
$ cat preproinsulin-seq-clean.txt

# Individual chain sequences
$ cat lsinsulin-seq-clean.txt  # Signal peptide (positions 1-24)
$ cat binsulin-seq-clean.txt   # B chain (positions 25-54)
$ cat cinsulin-seq-clean.txt   # C peptide (positions 55-89)
$ cat ainsulin-seq-clean.txt   # A chain (positions 90-110)
```

#### **Running the Analysis**

```bash
# Main analysis script
$ python3 analyze-insulin.py
Analyzing preproinsulin sequence...
Extracting chains...
Calculating molecular properties...
Results saved to results.txt

# String manipulation operations
$ python3 stringinsulin.py
Parsing sequence data...
Performing string operations...
Chain extraction complete.

# Calculate net charge
$ python3 net-charge.py
Calculating net molecular charge...
Counting charged amino acids...
Net charge: +2.5 at pH 7.0

# Calculate molecular weight from JSON
$ python3 calc_weight_json.py
Loading amino acid weights from JSON...
Calculating total molecular weight...
Molecular weight: 5808.0 Da
```

#### **What You're Learning**

- **Sequence parsing** - Reading and processing biological data
- **String slicing** - Extracting specific regions from sequences
- **File I/O** - Reading input files and writing results
- **JSON handling** - Working with structured data formats
- **Scientific computing** - Calculating molecular properties
- **Data validation** - Ensuring sequence integrity
- **Modular programming** - Breaking complex tasks into functions

#### **The Science**

**Preproinsulin Structure:**
- **Signal peptide (L-S)**: Amino acids 1-24 - Directs protein to endoplasmic reticulum
- **B chain**: Amino acids 25-54 - One of two chains in mature insulin
- **C peptide**: Amino acids 55-89 - Removed during processing
- **A chain**: Amino acids 90-110 - Second chain in mature insulin

**Molecular Calculations:**
- Each amino acid has a specific molecular weight
- Net charge depends on ionizable groups (pH-dependent)
- Isoelectric point (pI) is where net charge equals zero

---

### **Cryptography: Caesar Cipher Suite** 🔐

The Caesar cipher is a classic encryption technique where each letter is shifted by a fixed number of positions. This project teaches you encryption basics and debugging skills.

#### **Implementation**

```bash
# Basic Caesar cipher
$ python3 caesar.py
Enter message: HELLO WORLD
Enter shift: 3
Encrypted: KHOOR ZRUOG

# Debug challenges (increasing difficulty)
$ python3 debug-caesar-1.py  # Syntax errors
$ python3 debug-caesar-2.py  # Logic errors
$ python3 debug-caesar-3.py  # Runtime errors
$ python3 debug-caesar-4.py  # Complex bugs
```

#### **Concepts Covered**

- **Character encoding** - ASCII values and ord()/chr() functions
- **Modular arithmetic** - Wrapping around the alphabet
- **String building** - Constructing encrypted output
- **Input validation** - Handling edge cases
- **Debugging techniques** - Reading error messages and tracing code

**Algorithm Logic:**
```
Encryption: C = (P + K) mod 26
Decryption: P = (C - K) mod 26

Where:
P = plaintext letter position (0-25)
C = ciphertext letter position
K = key (shift amount)
```

---

### **Data Processing & File Operations** 📊

Modern programming heavily involves reading, processing, and writing data from various sources.

#### **JSON Operations**

```bash
$ python3 jsonFileHandler.py
# Module for JSON file operations
# Provides: read_json(), write_json(), update_json()

$ python3 calc_weight_json.py
Loading files/insulin.json...
Processing amino acid data...
Calculating molecular weights...
```

**JSON Structure Example:**
```json
{
  "amino_acids": {
    "A": {"name": "Alanine", "weight": 89.09},
    "C": {"name": "Cysteine", "weight": 121.16},
    "D": {"name": "Aspartic acid", "weight": 133.10}
  }
}
```

#### **CSV Processing**

```bash
$ python3 sys-admin.py
Reading car_fleet.csv...
Processing vehicle data...
Generating reports...
```

**Skills Developed:**
- Opening and closing files properly
- Reading data line-by-line vs. all-at-once
- Writing formatted output
- Exception handling for file operations
- Context managers (`with` statements)
- Path manipulation and file existence checks

---

## 🎯 Skill Development

### **Debugging Mastery** 🐛

Debugging is not just about fixing errors—it's about understanding how your code executes and developing a systematic approach to problem-solving.

```bash
$ python3 debugger.py
# Practice debugging techniques
# Learn to use print statements effectively
# Understand stack traces and error messages
```

#### **Debug Workflow:**

1. **Read the error message** - Python tells you what went wrong
2. **Identify the line** - Locate where the error occurred
3. **Understand the context** - What was the program trying to do?
4. **Form a hypothesis** - Why did this error happen?
5. **Test your fix** - Verify the solution works

#### **Common Error Types:**

- **SyntaxError** - Invalid Python syntax (missing colons, unmatched parentheses)
- **NameError** - Undefined variable or function
- **TypeError** - Operation on incompatible types
- **ValueError** - Correct type but inappropriate value
- **IndexError** - List index out of range
- **KeyError** - Dictionary key doesn't exist
- **FileNotFoundError** - Attempted to open non-existent file

---

## 📂 File Structure

### **Complete Directory Listing**

```
Week_05_Python_Programming/
│
├── 📁 files/
│   └── insulin.json                    # Amino acid molecular data
│
├── 📁 __pycache__/
│   └── jsonFileHandler.cpython-311.pyc # Compiled Python bytecode
│
├── 🐍 Core Learning Scripts
│   ├── Hello-world.py                  # Your first Python program
│   ├── string-datatype.py              # String operations & methods
│   ├── numeric-data.py                 # Integer, float, complex numbers
│   ├── collection.py                   # Lists, tuples, dicts, sets
│   ├── my_collections.py               # Custom collection implementations
│   ├── composite-data.py               # Nested data structures
│   ├── conditionals.py                 # If/elif/else logic
│   ├── categorize-values.py            # Classification algorithms
│   ├── for-loop.py                     # For loop iterations
│   ├── while-loopy.py                  # While loop examples
│   ├── prime.py                        # Prime number checker
│   └── primenumber.py                  # Prime algorithms
│
├── 🧬 Bioinformatics Suite
│   ├── preproinsulin-seq.txt           # Original sequence with headers
│   ├── preproinsulin-seq-clean.txt     # Cleaned sequence data
│   ├── lsinsulin-seq-clean.txt         # L-S signal peptide
│   ├── binsulin-seq-clean.txt          # B chain
│   ├── cinsulin-seq-clean.txt          # C peptide
│   ├── ainsulin-seq-clean.txt          # A chain
│   ├── analyze-insulin.py              # Main analysis pipeline
│   ├── stringinsulin.py                # Sequence string operations
│   ├── net-charge.py                   # Charge calculations
│   └── calc_weight_json.py             # Weight calculations from JSON
│
├── 🔐 Cryptography Project
│   ├── caesar.py                       # Caesar cipher implementation
│   ├── debug-caesar-1.py               # Debug challenge level 1
│   ├── debug-caesar-2.py               # Debug challenge level 2
│   ├── debug-caesar-3.py               # Debug challenge level 3
│   └── debug-caesar-4.py               # Debug challenge level 4
│
├── 📊 Data Processing
│   ├── jsonFileHandler.py              # JSON utility module
│   ├── car_fleet.csv                   # Sample CSV data
│   └── sys-admin.py                    # System administration script
│
├── 🐛 Debugging & Testing
│   ├── debugger.py                     # Debugging practice
│   ├── test.py                         # Test cases
│   └── results.txt                     # Output results file
│
└── 🌐 Additional Files
    └── devopslab.html                  # DevOps lab documentation
```

---

## 🚀 Usage Examples

### **Basic Execution**

```bash
# Navigate to the directory
$ cd Week_05_Python_Programming/

# Run a simple script
$ python3 Hello-world.py
Hello, World!

# Execute with verbose output
$ python3 -v numeric-data.py

# Run with debugging
$ python3 -m pdb conditionals.py

# Check syntax without executing
$ python3 -m py_compile prime.py
```

### **Working with Files**

```bash
# Read sequence data
$ python3 analyze-insulin.py
Processing: preproinsulin-seq-clean.txt
Extracting chains...
Writing results...

# Process JSON data
$ python3 calc_weight_json.py
Reading: files/insulin.json
Calculating molecular weights...
Total weight: 5808.0 Da

# Generate output
$ cat results.txt
Sequence Analysis Results
=========================
L-S Chain: 24 amino acids
B Chain: 30 amino acids
C Peptide: 35 amino acids
A Chain: 21 amino acids
```

### **Interactive Mode**

```bash
# Start Python interactive shell
$ python3
>>> import jsonFileHandler
>>> data = jsonFileHandler.read_json('files/insulin.json')
>>> print(data)
{'amino_acids': {...}}

# Import your modules
>>> from stringinsulin import extract_chain
>>> sequence = extract_chain('preproinsulin-seq-clean.txt', 1, 24)
>>> print(len(sequence))
24
```

---

## 🎓 Learning Outcomes

By completing this Week 05 curriculum, you will have developed proficiency in:

### **Technical Skills**

✅ **Python Fundamentals**
- Variable declaration and naming conventions
- Data type selection and conversion
- Operators and expressions
- Code commenting and documentation

✅ **Control Structures**
- Conditional logic implementation
- Loop design and optimization
- Function definition and invocation
- Error handling with try/except

✅ **Data Structures**
- List manipulation and comprehensions
- Dictionary operations and methods
- Tuple packing and unpacking
- Set operations and membership testing

✅ **File Operations**
- Reading from text files
- Writing formatted output
- JSON parsing and serialization
- CSV data processing
- File path manipulation

✅ **Algorithm Design**
- Problem decomposition
- Pseudocode development
- Time complexity awareness
- Code optimization strategies

### **Domain-Specific Skills**

🧬 **Bioinformatics**
- Protein sequence analysis
- Molecular weight calculations
- Charge state determination
- Biological data parsing

🔐 **Cryptography**
- Encryption algorithm implementation
- Character encoding techniques
- Security concepts introduction

📊 **Data Science**
- Data cleaning and preprocessing
- Structured data manipulation
- Result visualization preparation

### **Professional Development**

💼 **Software Engineering Practices**
- Code organization and modularity
- Naming conventions adherence
- Version control readiness
- Documentation habits

🐛 **Debugging Proficiency**
- Error message interpretation
- Systematic problem diagnosis
- Testing and validation
- Defensive programming

🤔 **Problem-Solving Mindset**
- Breaking down complex problems
- Identifying patterns and abstractions
- Applying learned concepts to new scenarios
- Self-directed learning and research

---

## 🔧 Command Line Mastery

### **Essential CLI Commands**

```bash
# List files with details
$ ls -lah
drwxr-xr-x  5 user group 4.0K Oct 27 10:30 .
drwxr-xr-x 15 user group 4.0K Oct 27 10:25 ..
-rw-r--r--  1 user group 1.2K Oct 27 10:30 Hello-world.py

# Find specific files
$ find . -name "*.py" -type f
./Hello-world.py
./analyze-insulin.py
./caesar.py
...

# Count lines of code
$ wc -l *.py
  15 Hello-world.py
  89 analyze-insulin.py
 145 caesar.py
...

# Search for patterns
$ grep -r "def " *.py
analyze-insulin.py:def extract_sequence():
caesar.py:def encrypt(text, shift):
prime.py:def is_prime(n):

# View file contents
$ cat preproinsulin-seq-clean.txt
MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN

# Monitor file changes
$ watch -n 1 'ls -lh results.txt'

# Redirect output to file
$ python3 analyze-insulin.py > output.log 2>&1

# Pipe commands
$ cat preproinsulin-seq-clean.txt | wc -c
110

# Make scripts executable
$ chmod +x analyze-insulin.py
$ ./analyze-insulin.py
```

### **Python-Specific Commands**

```bash
# Check installed packages
$ pip3 list

# Install requirements (if needed)
$ pip3 install -r requirements.txt

# Run with specific Python version
$ python3.11 analyze-insulin.py

# Generate bytecode
$ python3 -m compileall .

# Profile code performance
$ python3 -m cProfile analyze-insulin.py

# Run doctest
$ python3 -m doctest -v prime.py

# Format code
$ python3 -m black *.py

# Check code style
$ python3 -m pylint analyze-insulin.py
```

---

## 💡 Tips & Best Practices

### **Code Style**

```python
# Use descriptive variable names
sequence_length = len(dna_sequence)  # Good
n = len(s)                           # Avoid

# Write docstrings for functions
def calculate_weight(sequence):
    """
    Calculate molecular weight of protein sequence.
    
    Args:
        sequence (str): Amino acid sequence
        
    Returns:
        float: Total molecular weight in Daltons
    """
    pass

# Use constants for magic numbers
MAX_SEQUENCE_LENGTH = 1000
MIN_PRIME = 2
```

### **Common Pitfalls to Avoid**

❌ Modifying list while iterating
❌ Using mutable default arguments
❌ Forgetting to close files
❌ Ignoring edge cases
❌ Not handling exceptions

✅ Use list comprehensions wisely
✅ Utilize `with` statements for files
✅ Test edge cases thoroughly
✅ Write defensive code
✅ Comment complex logic

---

<div align="center">

## 🏆 You've Got This!

```
 _____                     _____                            _             _ 
|  |  | ___  ___  ___  ___|     | ___  _____  ___  ___  ___| |_ ___  ___ | |
|     || .'|| . ||_ -|| -_|   --|| . ||     || . || . ||_ -| . | . ||_ -||_|
|__|__||__,||  _||___||___|_____||___||_|_|_||  _||___||___|___|___||___||_|
              |_|                             |_|                            
```

### **Keep Coding. Keep Learning. Keep Growing.**

*"The only way to learn a new programming language is by writing programs in it."* - Dennis Ritchie

---

**Repository Stats:**
- 📝 36 Python Files
- 🧬 10 Bioinformatics Scripts
- 🔐 5 Cryptography Modules  
- 📊 Multiple Data Files
- 🐛 Extensive Debugging Practice

**Built with Python 3.11+ | October 2025**

</div>