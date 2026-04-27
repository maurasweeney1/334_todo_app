import sqlite3
from flask import Flask, request, jsonify, render_template
from database import init_db, add_todo, get_all_todos, delete_todo, toggle_todo

# Initialize Flask app
app = Flask(__name__)

# Initialize the database when the app starts
init_db()

# GET / - Serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

# GET /todos - Return all todo tasks
@app.route('/todos', methods=['GET'])
def get_todos():
    date = request.args.get('date', '')
    todos = get_all_todos(date)
    # Convert list of tuples to list of dictionaries
    result = []
    for todo in todos:
        result.append({
            'id': todo[0],
            'title': todo[1],
            'done': todo[2]
        })
    return jsonify(result), 200

# POST /todos - Create a new todo task
@app.route('/todos', methods=['POST'])
def create_todo():
    # Get the title from the request body
    data = request.get_json()
    title = data['title']
    date = data.get('date', '')
    add_todo(title, date)
    return jsonify({'message': 'Todo created successfully'}), 201

# DELETE /todos/<id> - Delete a todo task
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo_route(todo_id):
    deleted = delete_todo(todo_id)
    if deleted == 0:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify({'message': 'Todo deleted successfully'}), 200

# PUT /todos/<id> - Toggle a todo task done/undone
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def toggle_todo_route(todo_id):
    updated = toggle_todo(todo_id)
    if updated == 0:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify({'message': 'Todo updated successfully'}), 200

# DELETE /todos/completed - Clear all completed tasks for a given date
@app.route('/todos/completed', methods=['DELETE'])
def clear_completed_route():
    date = request.args.get('date', '')
    deleted = clear_completed(date)
    return jsonify({'message': f'{deleted} completed task(s) cleared'}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)