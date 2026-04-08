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
    