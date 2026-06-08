import sqlite3

# Connect Database
conn = sqlite3.connect("students.db")

# Create Cursor
cursor = conn.cursor()

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    roll_number TEXT,
    address TEXT,
    phone_number TEXT
)
""")

print("Table created successfully")

# Save Changes
conn.commit()

# Close Connection
conn.close()