Perfect 👍 — let’s go through all those **fact-finding exercises** one by one, clearly and concisely.

---

## 🐍 **Python Section**

1. **List vs Tuple**

   * **List:** Ordered, changeable (mutable), uses `[ ]`.
     👉 Example: `fruits = ["apple", "banana", "mango"]`
   * **Tuple:** Ordered, unchangeable (immutable), uses `( )`.
     👉 Example: `colors = ("red", "green", "blue")`

2. **Namespace**

   * A **namespace** is a container that holds variable names and their values to avoid naming conflicts.
     👉 Example: local variables, global variables, built-in functions each have their own namespace.

3. **Local vs Global Variable**

   * **Local:** Declared inside a function, accessible only there.
   * **Global:** Declared outside all functions, accessible everywhere in the file.

4. **IDE (Integrated Development Environment)**

   * Software used for writing, testing, and debugging code.
     👉 Examples: **VS Code**, **PyCharm**, **IDLE**, **Jupyter Notebook**.

5. **Modules**

   * Files that contain reusable Python code.
     👉 Examples: `math`, `os`, `datetime`, or a custom file like `my_module.py`.

6. **Array vs List**

   * **Array:** Stores elements of the same data type (needs the `array` module).
   * **List:** Can store mixed data types (built-in).

7. **Operators**

   * Symbols used to perform operations.
     👉 Examples: `+`, `-`, `*`, `/` (arithmetic), `==`, `!=` (comparison), `and`, `or` (logical).

---

## 🗄️ **Databases Section**

1. **Relational vs Non-Relational**

   * **Relational:** Structured, uses tables with rows & columns (e.g. MySQL, PostgreSQL).
   * **Non-Relational:** Flexible schema, uses documents or key-value pairs (e.g. DynamoDB, MongoDB).

2. **Indexes**

   * Special data structures that speed up query performance on columns.

3. **Primary Key vs Secondary Key**

   * **Primary Key:** Uniquely identifies each record.
   * **Secondary Key:** Used for faster searches, not necessarily unique.

4. **Inner vs Outer Join**

   * **Inner Join:** Returns matching rows from both tables.
   * **Outer Join:** Returns all rows, including non-matches, from one or both tables.

5. **DROP TABLE vs TRUNCATE TABLE**

   * **DROP:** Deletes the entire table structure and data.
   * **TRUNCATE:** Deletes only data, keeps the table structure.

6. **Data Types in SQL**

   * Common ones: `INT`, `VARCHAR`, `TEXT`, `DATE`, `FLOAT`, `BOOLEAN`.

7. **WHERE vs HAVING**

   * **WHERE:** Filters rows before grouping.
   * **HAVING:** Filters groups after `GROUP BY`.

---

## ☁️ **AWS Cloud Foundations Part 1**

1. **IaaS, PaaS, SaaS**

   * **IaaS:** Infrastructure as a Service (e.g., EC2).
   * **PaaS:** Platform as a Service (e.g., Elastic Beanstalk).
   * **SaaS:** Software as a Service (e.g., Gmail, Salesforce).

2. **Advantages of Cloud Computing**

   * Scalability, flexibility, cost-effectiveness, high availability, global reach.

3. **AWS Region**

   * A physical location worldwide containing multiple data centers (AZs).

4. **Availability Zone (AZ)**

   * One or more isolated data centers within a region.

5. **All AWS Regions**

   * Examples: `us-east-1`, `us-west-1`, `eu-west-1`, `ap-southeast-1`, `af-south-1`, etc.

6. **AWS Service Categories**

   * Compute, Storage, Database, Networking, Security, Analytics, AI/ML, Developer Tools.

7. **Object vs Block Storage**

   * **Object Storage:** Stores data as objects (e.g., S3).
   * **Block Storage:** Stores data in fixed-size blocks (e.g., EBS).

8. **Two Compute Services**

   * **Amazon EC2:** Virtual servers.
   * **AWS Lambda:** Serverless compute for running code on demand.

9. **Two Storage Services**

   * **Amazon S3:** Object storage for files.
   * **Amazon EBS:** Block storage for EC2 instances.

---

## ☁️ **AWS Cloud Foundations Part 2**

1. **AWS Shared Responsibility Model**

   * **AWS:** Secures the cloud infrastructure.
   * **Customer:** Secures data, access, and configurations **in the cloud**.

2. **IAM Role**

   * Temporary set of permissions that define what actions can be performed by a user, service, or application.

3. **IAM Policy**

   * A JSON document that specifies permissions for users, groups, or roles.

4. **Amazon Machine Image (AMI)**

   * A preconfigured template containing the OS, software, and settings used to launch EC2 instances.

5. **EC2 Instance Types**

   * **General Purpose (t3):** Balanced use.
   * **Compute Optimized (c5):** CPU-intensive tasks.
   * **Memory Optimized (r5):** Large memory workloads.
   * **Storage Optimized (i3):** High I/O workloads.
   * **Accelerated Computing (p3):** GPU workloads.

6. **Virtual Private Cloud (VPC)**

   * A logically isolated section of AWS where you can launch resources in a virtual network.

7. **Public vs Private Subnet**

   * **Public:** Accessible from the internet (has an Internet Gateway).
   * **Private:** No direct internet access; used for backend servers or databases.

---

Would you like me to make this into a **clean study PDF sheet** you can print or use for your AWS re/Start revision?
