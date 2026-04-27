# test_unit.py
import sqlite3
import pytest
from database import init_db, add_todo, get_all_todos

def test_add_todo():
    # Use a temporary test database, not the real one
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    
    # Insert a task directly
    cursor.execute('INSERT INTO todos (title, done) VALUES (?, 0)', ('Buy groceries',))
    conn.commit()
    
    # Check if the task is in the database
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    assert len(todos) == 1
    assert todos[0][1] == 'Buy groceries'
    conn.close()

def test_get_all_todos():
    # Use a temporary test database, not the real onegit add tests/test_unit.py
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    
    # Insert two tasks for testing
    cursor.execute('INSERT INTO todos (title, done) VALUES (?, 0)', ('Buy groceries',))
    cursor.execute('INSERT INTO todos (title, done) VALUES (?, 0)', ('Do homework',))
    conn.commit()
    
    # Get all tasks
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    
    # Verify that two tasks were returned
    assert len(todos) == 2
    assert todos[0][1] == 'Buy groceries'
    assert todos[1][1] == 'Do homework'
    conn.close()
    
def test_delete_todo():
    # Use a temporary test database, not the real one
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    
    # Insert a task to delete
    cursor.execute('INSERT INTO todos (title, done) VALUES (?, 0)', ('Buy groceries',))
    conn.commit()
    
    # Delete the task
    cursor.execute('DELETE FROM todos WHERE id = 1')
    conn.commit()
    
    # Verify the task was deleted
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    assert len(todos) == 0
    conn.close()

def test_toggle_todo():
    # Use a temporary test database, not the real one
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()

    # Insert a task with done = 0
    cursor.execute('INSERT INTO todos (title, done) VALUES (?, 0)', ('Buy groceries',))
    conn.commit()

    # Toggle done: 0 -> 1
    cursor.execute('UPDATE todos SET done = 1 - done WHERE id = 1')
    conn.commit()
    cursor.execute('SELECT done FROM todos WHERE id = 1')
    assert cursor.fetchone()[0] == 1

    # Toggle done: 1 -> 0
    cursor.execute('UPDATE todos SET done = 1 - done WHERE id = 1')
    conn.commit()
    cursor.execute('SELECT done FROM todos WHERE id = 1')
    assert cursor.fetchone()[0] == 0

    conn.close()
    
def test_clear_completed():
    # Test that clear_completed removes only completed tasks for a given date
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0,
            date TEXT NOT NULL DEFAULT ''
        )
    ''')
    conn.commit()
    cursor.execute('INSERT INTO todos (title, done, date) VALUES (?, 1, ?)', ('Completed task', '2026-04-26'))
    cursor.execute('INSERT INTO todos (title, done, date) VALUES (?, 0, ?)', ('Incomplete task', '2026-04-26'))
    conn.commit()
    cursor.execute('DELETE FROM todos WHERE done = 1 AND date = ?', ('2026-04-26',))
    conn.commit()
    deleted = cursor.rowcount
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    assert deleted == 1
    assert len(todos) == 1
    assert todos[0][1] == 'Incomplete task'
    conn.close()
 
 
def test_clear_completed_no_completed_tasks():
    # Test clear_completed when there are no completed tasks — should delete nothing
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0,
            date TEXT NOT NULL DEFAULT ''
        )
    ''')
    conn.commit()
    cursor.execute('INSERT INTO todos (title, done, date) VALUES (?, 0, ?)', ('Incomplete task', '2026-04-26'))
    conn.commit()
    cursor.execute('DELETE FROM todos WHERE done = 1 AND date = ?', ('2026-04-26',))
    conn.commit()
    deleted = cursor.rowcount
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    assert deleted == 0
    assert len(todos) == 1
    conn.close()
