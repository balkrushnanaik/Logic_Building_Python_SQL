import sqlite3

# Create or connect to a database
connection = sqlite3.connect('example.db')

# Create a cursor object
cursor = connection.cursor()

# Create a sample table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

# Insert sample data
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('John Doe', 'john@example.com'))
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", ('Jane Smith', 'jane@example.com'))

# Commit the changes
connection.commit()

# Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Display results
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
