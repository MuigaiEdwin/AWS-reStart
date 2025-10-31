import mysql.connector

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="restaurant"
)

# Create a cursor and execute a query
cursor = conn.cursor()
cursor.execute("SELECT * FROM menu_items")

# Fetch results
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()
