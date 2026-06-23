from flask import Flask, request, redirect

app = Flask(__name__)

# In-memory task list (resets when server restarts)
tasks = []

# -----------------------------
# HTML UI (embedded)
# -----------------------------
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
            margin-top: 80px;
        }

        input {
            padding: 10px;
            width: 250px;
            border-radius: 5px;
            border: none;
        }

        button {
            padding: 10px 15px;
            border: none;
            background: #38bdf8;
            border-radius: 5px;
            cursor: pointer;
        }

        .task {
            background: #1e293b;
            margin: 10px auto;
            padding: 10px;
            width: 300px;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        a {
            color: red;
            text-decoration: none;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <h1>📝 Flask Todo App</h1>

    <form method="POST" action="/add">
        <input type="text" name="task" placeholder="Enter a task..." required>
        <button type="submit">Add</button>
    </form>

    <h2>Your Tasks</h2>

    {tasks}

</body>
</html>
"""

# -----------------------------
# Home route
# -----------------------------
@app.route("/")
def home():
    task_html = ""

    for i, task in enumerate(tasks):
        task_html += f"""
        <div class="task">
            <span>{task}</span>
            <a href="/delete/{i}">X</a>
        </div>
        """

    return HTML_PAGE.format(tasks=task_html)

# -----------------------------
# Add task
# -----------------------------
@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect("/")

# -----------------------------
# Delete task
# -----------------------------
@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
