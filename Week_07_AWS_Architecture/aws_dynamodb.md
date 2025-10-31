# Introduction to Amazon DynamoDB Lab

<div align="center">

![DynamoDB](https://img.shields.io/badge/Amazon%20DynamoDB-4053D6?style=for-the-badge&logo=Amazon%20DynamoDB&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![NoSQL](https://img.shields.io/badge/NoSQL-Database-green?style=for-the-badge)

**A hands-on lab exploring NoSQL database operations with Amazon DynamoDB**

[Overview](#overview) • [Prerequisites](#prerequisites) • [Lab Tasks](#lab-tasks) • [Key Concepts](#key-concepts) • [Resources](#resources)

</div>

---

## 📋 Overview

Amazon DynamoDB is a fast and flexible NoSQL database service that provides consistent, single-digit millisecond latency at any scale. This lab demonstrates core DynamoDB operations including table creation, data manipulation, querying, and cleanup.

### 🎯 Learning Objectives

By completing this lab, you will:

- ✅ Create an Amazon DynamoDB table with partition and sort keys
- ✅ Insert and manage data in a NoSQL database
- ✅ Query data using primary keys
- ✅ Scan tables with filters
- ✅ Modify existing items
- ✅ Delete DynamoDB tables

### ⏱️ Duration
**Approximately 35 minutes**

---

## 🚀 Prerequisites

- AWS Account with lab access
- Basic understanding of database concepts
- Familiarity with the AWS Management Console

---

## 📚 Lab Tasks

### Task 1: Create a DynamoDB Table

#### 🎯 Objective
Create a `Music` table with appropriate partition and sort keys.

#### 📝 Steps

1. **Navigate to DynamoDB Service**
   ```
   AWS Console → Services → Database → DynamoDB
   ```

2. **Create Table**
   - Click **Create table**
   - Configure the following:

   | Setting | Value | Type |
   |---------|-------|------|
   | **Table name** | `Music` | - |
   | **Partition key** | `Artist` | String |
   | **Sort key** | `Song` | String |

3. **Create with Default Settings**
   - Leave indexes and provisioned capacity as default
   - Click **Create table**
   - Wait for status to change to **Active** (~1 minute)

#### 📸 Screenshot
![Table Creation](screenshots/01-table-creation.png)

#### 🔑 Key Concepts

- **Partition Key (Primary Key)**: Used to distribute data across DynamoDB servers
- **Sort Key**: Combined with partition key to uniquely identify items
- **Composite Primary Key**: Artist + Song creates a unique identifier

---

### Task 2: Add Data to the Table

#### 🎯 Objective
Add three music items with varying attributes to demonstrate schema flexibility.

#### 📝 Steps

1. **Select the Music Table**
   - Click on the `Music` table name

2. **Create First Item: Pink Floyd**
   ```
   Actions → Create item
   ```
   
   | Attribute | Type | Value |
   |-----------|------|-------|
   | Artist | String | `Pink Floyd` |
   | Song | String | `Money` |
   | Album | String | `The Dark Side of the Moon` |
   | Year | Number | `1973` |

   - Click **Add new attribute** → **String** for Album
   - Click **Add new attribute** → **Number** for Year
   - Click **Create item**

3. **Create Second Item: John Lennon**
   
   | Attribute | Type | Value |
   |-----------|------|-------|
   | Artist | String | `John Lennon` |
   | Song | String | `Imagine` |
   | Album | String | `Imagine` |
   | Year | Number | `1971` |
   | Genre | String | `Soft rock` |

   > **Note**: This item includes a `Genre` attribute not present in the first item, demonstrating NoSQL flexibility.

4. **Create Third Item: Psy**
   
   | Attribute | Type | Value |
   |-----------|------|-------|
   | Artist | String | `Psy` |
   | Song | String | `Gangnam Style` |
   | Album | String | `Psy 6 (Six Rules), Part 1` |
   | Year | Number | `2011` |
   | LengthSeconds | Number | `219` |

   > **Note**: This item includes `LengthSeconds`, another unique attribute.

#### 📸 Screenshots
![Item Creation](screenshots/02-add-items.png)
![All Items](screenshots/03-items-list.png)

#### 💡 Schema Flexibility

Unlike traditional relational databases, DynamoDB allows each item to have different attributes without pre-defining a schema:

```
Item 1: Artist, Song, Album, Year
Item 2: Artist, Song, Album, Year, Genre
Item 3: Artist, Song, Album, Year, LengthSeconds
```

---

### Task 3: Modify an Existing Item

#### 🎯 Objective
Correct an error in the data by updating an existing item.

#### 📝 Steps

1. **Navigate to Items**
   ```
   DynamoDB Dashboard → Tables → Explore Items
   ```

2. **Select Music Table**
   - Click the **Music** button

3. **Update Psy's Record**
   - Click on **Psy**
   - Change `Year` from `2011` to `2012`
   - Click **Save changes**

#### 📸 Screenshot
![Item Update](screenshots/04-modify-item.png)

#### ✅ Verification
The item is now updated with the correct year.

---

### Task 4: Query the Table

#### 🎯 Objective
Learn the difference between Query and Scan operations.

#### 4.1 Query Operation (Efficient)

##### 📝 Steps

1. **Access Query Interface**
   ```
   Expand Scan/Query items → Choose Query
   ```

2. **Execute Query**
   
   | Field | Value |
   |-------|-------|
   | Artist (Partition key) | `Psy` |
   | Song (Sort key) | `Gangnam Style` |

3. Click **Run**

##### 📸 Screenshot
![Query Results](screenshots/05-query-results.png)

##### ⚡ Performance
- **Fast**: Uses indexed primary keys
- **Efficient**: Directly retrieves specific items
- **Best Practice**: Preferred method for data retrieval

#### 4.2 Scan Operation (Less Efficient)

##### 📝 Steps

1. **Switch to Scan**
   - Scroll up and choose **Scan**

2. **Add Filter**
   ```
   Expand Filters
   ```
   
   | Setting | Value |
   |---------|-------|
   | Attribute name | `Year` |
   | Type | Number |
   | Value | `1971` |

3. Click **Run**

##### 📸 Screenshot
![Scan Results](screenshots/06-scan-results.png)

##### 🐌 Performance Considerations
- **Slower**: Examines every item in the table
- **Resource Intensive**: Uses more read capacity
- **Use Case**: When you need to filter on non-key attributes

#### 📊 Query vs Scan Comparison

| Feature | Query | Scan |
|---------|-------|------|
| **Speed** | ⚡ Fast | 🐌 Slow |
| **Efficiency** | High | Low |
| **Index Usage** | Yes | No |
| **Best For** | Primary key lookups | Full table searches |
| **Cost** | Lower | Higher |

---

### Task 5: Delete the Table

#### 🎯 Objective
Clean up resources by deleting the Music table and all its data.

#### 📝 Steps

1. **Navigate to Table Settings**
   ```
   DynamoDB Dashboard → Tables → Update settings
   ```

2. **Select Music Table**
   - Ensure `Music` table is selected

3. **Delete Table**
   ```
   Actions → Delete table
   ```

4. **Confirm Deletion**
   - Type `delete` in the confirmation field
   - Click **Delete table**

#### 📸 Screenshot
![Table Deletion](screenshots/07-delete-table.png)

#### ⚠️ Warning
This action permanently deletes the table and all data. This cannot be undone.

---

## 🔑 Key Concepts Learned

### 1. **NoSQL Database Fundamentals**
- Schema-less design allows flexible attribute structures
- Each item can have different attributes
- No need to pre-define all columns

### 2. **DynamoDB Core Components**

```
┌─────────────────────────────────────┐
│           DynamoDB Table            │
├─────────────────────────────────────┤
│  Partition Key: Artist              │
│  Sort Key: Song                     │
├─────────────────────────────────────┤
│  Item 1: {Artist, Song, Album, ...} │
│  Item 2: {Artist, Song, Genre, ...} │
│  Item 3: {Artist, Song, Length, ...}│
└─────────────────────────────────────┘
```

### 3. **Key Terminology**

| Term | Definition | Example |
|------|------------|---------|
| **Table** | Collection of data | Music library |
| **Item** | Group of attributes (like a row) | One song record |
| **Attribute** | Fundamental data element (like a column) | Artist, Year, Genre |
| **Partition Key** | Primary identifier for data distribution | Artist |
| **Sort Key** | Secondary identifier for ordering | Song |

### 4. **Data Access Patterns**

#### Query (Recommended)
```
Query: "Get all songs by Pink Floyd"
→ Uses partition key index
→ Fast and efficient
```

#### Scan (Use Sparingly)
```
Scan: "Find all songs from 1971"
→ Reads entire table
→ Slower and more expensive
```

---

## 📁 Project Structure

```
dynamodb-lab/
├── README.md                          # This file
├── screenshots/
│   ├── 01-table-creation.png         # Table configuration
│   ├── 02-add-items.png              # Adding items
│   ├── 03-items-list.png             # All items view
│   ├── 04-modify-item.png            # Updating item
│   ├── 05-query-results.png          # Query operation
│   ├── 06-scan-results.png           # Scan operation
│   └── 07-delete-table.png           # Table deletion
├── data/
│   └── music-items.json              # Sample data
└── documentation/
    └── lab-notes.md                  # Additional notes
```

---

## 💾 Sample Data

### JSON Format

```json
{
  "Music": [
    {
      "Artist": "Pink Floyd",
      "Song": "Money",
      "Album": "The Dark Side of the Moon",
      "Year": 1973
    },
    {
      "Artist": "John Lennon",
      "Song": "Imagine",
      "Album": "Imagine",
      "Year": 1971,
      "Genre": "Soft rock"
    },
    {
      "Artist": "Psy",
      "Song": "Gangnam Style",
      "Album": "Psy 6 (Six Rules), Part 1",
      "Year": 2012,
      "LengthSeconds": 219
    }
  ]
}
```

---

## 🎓 Best Practices

### ✅ Do's
- ✔️ Use Query instead of Scan when possible
- ✔️ Design partition keys for even data distribution
- ✔️ Use sort keys for related items that need ordering
- ✔️ Take advantage of schema flexibility
- ✔️ Monitor read/write capacity units

### ❌ Don'ts
- ✖️ Don't use Scan for large tables in production
- ✖️ Don't create overly complex partition keys
- ✖️ Don't ignore data access patterns during design
- ✖️ Don't forget to delete unused tables (costs!)

---

## 🔧 Alternative Methods for Loading Data

While this lab uses the console, you can also load data using:

1. **AWS CLI**
   ```bash
   aws dynamodb put-item \
     --table-name Music \
     --item '{"Artist": {"S": "Artist Name"}, "Song": {"S": "Song Title"}}'
   ```

2. **AWS SDKs** (Python, JavaScript, Java, etc.)
   ```python
   import boto3
   
   dynamodb = boto3.resource('dynamodb')
   table = dynamodb.Table('Music')
   
   table.put_item(
       Item={
           'Artist': 'Pink Floyd',
           'Song': 'Money',
           'Year': 1973
       }
   )
   ```

3. **Third-Party Tools**
   - NoSQL Workbench for DynamoDB
   - DynamoDB Import/Export tools

---

## 🚀 Advanced Topics

### Global Secondary Index (GSI)
Create additional indexes for querying on non-key attributes:
```
GSI on Year → Query all songs from specific years
```

### Local Secondary Index (LSI)
Alternative sort keys for the same partition key:
```
LSI on Year → Sort songs by year for each artist
```

### DynamoDB Streams
Capture table modifications for:
- Real-time analytics
- Data replication
- Triggering Lambda functions

---

## 📊 Lab Results Summary

| Metric | Value |
|--------|-------|
| **Tables Created** | 1 (Music) |
| **Items Added** | 3 songs |
| **Attributes Used** | 6 different types |
| **Queries Executed** | 2 (Query + Scan) |
| **Items Modified** | 1 (Psy - Year update) |
| **Tables Deleted** | 1 (cleanup) |

---

## 🎯 Use Cases for DynamoDB

| Industry | Application |
|----------|-------------|
| **Gaming** | Player data, leaderboards, session history |
| **IoT** | Device data, sensor readings, telemetry |
| **Mobile** | User profiles, app state, offline sync |
| **Ad Tech** | Real-time bidding, user targeting, analytics |
| **E-commerce** | Shopping carts, product catalogs, orders |
| **Social Media** | User posts, comments, relationships |

---

## 📚 Additional Resources

### Official Documentation
- [Amazon DynamoDB Documentation](https://docs.aws.amazon.com/dynamodb/)
- [DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/)
- [DynamoDB API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/)

### Learning Resources
- [AWS DynamoDB Best Practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
- [NoSQL Workbench for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.html)
- [DynamoDB Pricing Calculator](https://aws.amazon.com/dynamodb/pricing/)

### Community
- [AWS DynamoDB Forum](https://forums.aws.amazon.com/forum.jspa?forumID=131)
- [Stack Overflow - DynamoDB Tag](https://stackoverflow.com/questions/tagged/amazon-dynamodb)

---

## 🏆 Conclusion

### What You Accomplished

✅ **Created** a NoSQL database table with composite primary key  
✅ **Inserted** multiple items with varying attributes  
✅ **Modified** existing data  
✅ **Queried** data efficiently using primary keys  
✅ **Scanned** table with filters  
✅ **Deleted** table and cleaned up resources  

### Key Takeaways

1. **Flexibility**: NoSQL databases don't require a fixed schema
2. **Performance**: Query operations are much faster than Scan
3. **Scalability**: DynamoDB automatically scales to handle load
4. **Simplicity**: Fully managed service eliminates infrastructure concerns

---

## 👨‍💻 Author

**Your Name**  
Date: November 1, 2025  
Course: AWS Cloud Computing / Database Management  

---

## 📜 License

This project is part of AWS educational lab materials. Please refer to AWS training terms for usage guidelines.

---

## 🤝 Contributing

If you find any issues or have suggestions for improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

<div align="center">

**⭐ If you found this lab helpful, please star this repository! ⭐**

Made with ❤️ for AWS learners

</div>