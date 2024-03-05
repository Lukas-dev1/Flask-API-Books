import sqlite3

# Connect to SQLite database (this will create a new database file if it doesn't exist)
conn = sqlite3.connect('book_review_platform.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create table for books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        summary TEXT,
        genre TEXT
    )
''')

# Create table for reviews
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reviews (
        review_id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER,
        user_name TEXT NOT NULL,
        rating INTEGER CHECK (rating >= 1 AND rating <= 5) NOT NULL,
        review_text TEXT,
        FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
