import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Fetch credentials
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

# ✅ Create a table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50),
    graduation_date DATETIME
)
""")

# ✅ Insert a sample row
cursor.execute("""
INSERT INTO Students (name, city, graduation_date)
VALUES ('Edwin Muigai', 'Murang’a', NOW())
""")
db.commit()

# ✅ Fetch data
cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
    print(row)

db.close()
