import sqlite3

# Initialize the database and create the todos table
def init_db():
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# Add a new todo task
def add_todo(title):
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    # Insert new task, done defaults to 0 (not completed)
    cursor.execute('INSERT INTO todos (title, done) VALUES (?, 0)', (title,))
    conn.commit()
    conn.close()

# Get all todo tasks from the database
def get_all_todos():
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    conn.close()
    # Return the list of all tasks
    return todos

# Delete a todo task 

# Mark as complete/incomplete