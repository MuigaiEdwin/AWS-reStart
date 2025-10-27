# 🐍 Week 05 - Python Programming Journey

> *From "Hello World" to Bioinformatics - A hands-on exploration of Python fundamentals*

<div align="center">

```mermaid
graph LR
    A[📚 Learn] --> B[💻 Code]
    B --> C[🐛 Debug]
    C --> D[🚀 Deploy]
    D --> E[🎉 Master]
    style A fill:#ff6b6b
    style B fill:#4ecdc4
    style C fill:#ffe66d
    style D fill:#a8e6cf
    style E fill:#c7ceea
```

</div>

---

## 🎯 Repository Overview

```mermaid
mindmap
  root((Week 05))
    🧬 Insulin Analysis
      Sequence Parser
      Weight Calculator
      Chain Extractor
    🔤 Core Python
      Data Types
      Control Flow
      Collections
    🔐 Cryptography
      Caesar Cipher
      Debug Challenges
    📦 Data Handling
      JSON
      CSV
      File I/O
```

---

## 🧬 Insulin Analysis Pipeline

```mermaid
flowchart TD
    A[📄 preproinsulin-seq.txt] -->|Clean| B[🧹 preproinsulin-seq-clean.txt]
    B -->|Extract| C[L-S Chain<br/>Positions 1-24]
    B -->|Extract| D[B Chain<br/>Positions 25-54]
    B -->|Extract| E[C Peptide<br/>Positions 55-89]
    B -->|Extract| F[A Chain<br/>Positions 90-110]
    C --> G[📊 analyze-insulin.py]
    D --> G
    E --> G
    F --> G
    G --> H[⚖️ Calculate Weights]
    G --> I[⚡ Calculate Charges]
    H --> J[✅ results.txt]
    I --> J
    
    style A fill:#e1f5ff
    style B fill:#b3e5fc
    style G fill:#4fc3f7
    style J fill:#0288d1
```

---

## 🎮 Project Structure

<table>
<tr>
<td width="50%">

### 🔤 **Fundamentals**
```
📝 Hello-world.py
🔤 string-datatype.py
🔢 numeric-data.py
📦 collection.py
🎯 composite-data.py
```

</td>
<td width="50%">

### 🔄 **Control Flow**
```
➿ for-loop.py
🔁 while-loopy.py
❓ conditionals.py
✅ categorize-values.py
🔢 prime.py
```

</td>
</tr>
<tr>
<td>

### 🔐 **Cryptography**
```
🔒 caesar.py
🐛 debug-caesar-1.py
🐛 debug-caesar-2.py
🐛 debug-caesar-3.py
🐛 debug-caesar-4.py
```

</td>
<td>

### 📊 **Data Processing**
```
📋 jsonFileHandler.py
⚖️ calc_weight_json.py
🚗 car_fleet.csv
💾 sys-admin.py
```

</td>
</tr>
</table>

---

## 🚀 Quick Start Guide

```mermaid
flowchart LR
    A[🎬 Start] --> B{Choose Path}
    B -->|Beginner| C[Hello-world.py]
    B -->|Intermediate| D[analyze-insulin.py]
    B -->|Advanced| E[caesar.py]
    C --> F[✨ Learn Basics]
    D --> G[🧬 Bioinformatics]
    E --> H[🔐 Cryptography]
    
    style A fill:#ff6b6b
    style B fill:#4ecdc4
    style F fill:#95e1d3
    style G fill:#f38181
    style H fill:#aa96da
```

**Run any script:**
```bash
python3 <filename>.py
```

---

## 💡 Learning Progression

```mermaid
graph TB
    A[Week 05 Start] --> B[📚 Data Types]
    B --> C[🔄 Control Structures]
    C --> D[📦 Collections]
    D --> E[📂 File I/O]
    E --> F[🧬 Real Projects]
    F --> G[🎓 Python Master]
    
    B -.-> B1[Strings, Numbers]
    C -.-> C1[Loops, Conditionals]
    D -.-> D1[Lists, Dicts]
    E -.-> E1[JSON, CSV]
    F -.-> F1[Insulin Analysis]
    
    style A fill:#667eea
    style G fill:#764ba2
    style F fill:#f093fb
```

---

## 🎯 Skills Matrix

<div align="center">

| Skill | Files | Level |
|-------|-------|-------|
| 🐍 **Python Basics** | Hello-world.py → numeric-data.py | ⭐⭐⭐⭐⭐ |
| 🔄 **Loops & Logic** | for-loop.py, while-loopy.py | ⭐⭐⭐⭐ |
| 📦 **Data Structures** | collection.py, my_collections.py | ⭐⭐⭐⭐ |
| 📂 **File Handling** | jsonFileHandler.py | ⭐⭐⭐⭐ |
| 🧬 **Bioinformatics** | analyze-insulin.py, net-charge.py | ⭐⭐⭐⭐⭐ |
| 🔐 **Cryptography** | caesar.py, debug-caesar-*.py | ⭐⭐⭐ |

</div>

---

## 🧪 Caesar Cipher Debug Challenge

```mermaid
journey
    title Debug Journey
    section Level 1
      Start: 5: Beginner
      Find bug: 3: Beginner
      Fix bug: 4: Beginner
    section Level 2
      New challenge: 4: Intermediate
      Debug: 3: Intermediate
      Success: 5: Intermediate
    section Level 3
      Complex bug: 2: Advanced
      Deep dive: 3: Advanced
      Victory: 5: Advanced
    section Level 4
      Master level: 3: Expert
      Final fix: 4: Expert
      Champion: 5: Expert
```

---

## 🎨 What Makes This Special?

<div align="center">

```mermaid
quadrantChart
    title Skills Development Map
    x-axis Low Complexity --> High Complexity
    y-axis Low Impact --> High Impact
    quadrant-1 Advanced Projects
    quadrant-2 Core Skills
    quadrant-3 Basics
    quadrant-4 Practice Zone
    
    Hello World: [0.15, 0.3]
    Data Types: [0.3, 0.5]
    Control Flow: [0.45, 0.6]
    File I/O: [0.6, 0.7]
    Insulin Analysis: [0.85, 0.9]
    Caesar Cipher: [0.7, 0.65]
    JSON Handling: [0.55, 0.75]
```

</div>

---

## 📦 Files Overview

```
Week_05_Python_Programming/
│
├── 🧬 Insulin Project
│   ├── preproinsulin-seq.txt
│   ├── analyze-insulin.py
│   └── [chain files]
│
├── 🎓 Learning Modules
│   ├── Hello-world.py
│   ├── Data types & structures
│   └── Control flow scripts
│
├── 🔐 Cipher Challenge
│   └── caesar.py + 4 debug levels
│
└── 📊 Data Operations
    ├── files/insulin.json
    └── JSON/CSV handlers
```

---

<div align="center">

## 🎓 Ready to Code?

```mermaid
graph LR
    A[🌟 Pick a Script] --> B[💻 Run It]
    B --> C[🔧 Modify It]
    C --> D[🚀 Master It]
    
    style A fill:#667eea
    style B fill:#764ba2
    style C fill:#f093fb
    style D fill:#4facfe
```

### 🏆 **Challenge Yourself. Learn by Doing. Build Something Amazing!**

---

**Built with ❤️ using Python 3.11+**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Code](https://img.shields.io/badge/Code-With%20❤️-red.svg)](https://github.com)
[![Learning](https://img.shields.io/badge/Status-Learning-green.svg)](https://github.com)

</div>