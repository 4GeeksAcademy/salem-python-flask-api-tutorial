from flask import Flask, jsonify, request



app = Flask(__name__)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)  # Add the new todo to the list
    return jsonify(todos)  # Return the updated list as JSON

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Logic to delete the todo at the given position
    todos.pop(position)
    return jsonify(todos)  # Make sure to return the updated list of todos

# Step 1: Declare the global variable
todos = [
    { "label": "My first task", "done": False }
]

# Step 2: Define the route
@app.route('/todos', methods=['GET'])
def get_todos():
    # Step 3: Return the todos as JSON
    return jsonify(todos)

if __name__ == '__main__':
    app.run()



# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

