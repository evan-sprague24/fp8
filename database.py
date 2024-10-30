import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()

# Create a table for storing feedback
cursor.execute('''
CREATE TABLE IF NOT EXISTS feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    feedback TEXT NOT NULL
)
''')

conn.commit()