import sqlite3
from flask import Flask, request, jsonify, render_template
from database import init_db, add_todo, get_all_todos

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
    todos = get_all_todos()
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
    add_todo(title)
    return jsonify({'message': 'Todo created successfully'}), 201

# DELETE /todos/<id> - Delete a todo task

# PUT /todos/<id> - Mark a todo task as done

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5001)