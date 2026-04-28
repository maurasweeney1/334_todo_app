import sqlite3


# Initialize the database and create the todos table
def init_db():
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0,
            date TEXT NOT NULL DEFAULT ''
        )
    ''')
    try:
        cursor.execute(
            "ALTER TABLE todos ADD COLUMN date TEXT NOT NULL DEFAULT ''"
        )
    except sqlite3.OperationalError:
        pass
    conn.commit()
    conn.close()


# Add a new todo task
def add_todo(title, date):
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    # Insert new task, done defaults to 0 (not completed)
    cursor.execute(
        'INSERT INTO todos (title, done, date) VALUES (?, 0, ?)',
        (title, date)
    )
    conn.commit()
    conn.close()


# Get all todo tasks from the database
def get_all_todos(date):
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todos WHERE date = ?', (date,))
    todos = cursor.fetchall()
    conn.close()
    # Return the list of all tasks
    return todos


# Delete a todo task
def delete_todo(todo_id):
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted


# Mark as complete/incomplete
def toggle_todo(todo_id):
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute(
        'UPDATE todos SET done = 1 - done WHERE id = ?', (todo_id,)
    )
    conn.commit()
    updated = cursor.rowcount
    conn.close()
    return updated


# Clear all completed todo tasks for a given date
def clear_completed(date):
    conn = sqlite3.connect('todos.db')
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM todos WHERE done = 1 AND date = ?', (date,)
    )
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted
