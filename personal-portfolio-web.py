from flask import Flask, request

app = Flask(__name__)

# -----------------------------
# Simple contact handler (no database yet)
# -----------------------------
messages = []

# -----------------------------
# HTML TEMPLATE
# -----------------------------
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Portfolio</title>
    <style>
        body {
            font-family: Arial;
            margin: 0;
            background: #0f172a;
            color: white;
        }

        .navbar {
            background: #1e293b;
            padding: 15px;
            text-align: center;
        }

        .navbar a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: bold;
        }

        .section {
            padding: 40px;
            text-align: center;
        }

        .card {
            background: #1e293b;
            padding: 20px;
            margin: 15px auto;
            width: 60%;
            border-radius: 10px;
        }

        input, textarea {
            width: 60%;
            padding: 10px;
            margin: 10px;
            border-radius: 5px;
            border: none;
        }

        button {
            padding: 10px 15px;
            background: #38bdf8;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }

        button:hover {
            background: #0ea5e9;
        }
    </style>
</head>
<body>

<div class="navbar">
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/projects">Projects</a>
    <a href="/skills">Skills</a>
    <a href="/contact">Contact</a>
</div>

<div class="section">
    {content}
</div>

</body>
</html>
"""

# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def home():
    content = """
    <h1>👋 Hi, I'm a Python Developer</h1>
    <p>Welcome to my personal portfolio built with Flask.</p>
    """
    return HTML.format(content=content)

@app.route("/about")
def about():
    content = """
    <h1>About Me</h1>
    <div class="card">
        <p>I build Python projects focused on data analysis, Flask web apps, and game systems.</p>
    </div>
    """
    return HTML.format(content=content)

@app.route("/projects")
def projects():
    content = """
    <h1>Projects</h1>

    <div class="card">
        <h3>📊 Data Analysis Repo</h3>
        <p>Weather, RPG stats, and game analytics using Pandas.</p>
    </div>

    <div class="card">
        <h3>🌦️ Weather App</h3>
        <p>Flask app using Open-Meteo API.</p>
    </div>

    <div class="card">
        <h3>🎮 RPG Dashboard</h3>
        <p>Game character analysis with PowerScore system.</p>
    </div>

    <div class="card">
        <h3>📝 Todo App</h3>
        <p>CRUD-based task manager built with Flask.</p>
    </div>
    """
    return HTML.format(content=content)

@app.route("/skills")
def skills():
    content = """
    <h1>Skills</h1>

    <div class="card">
        <p>🐍 Python</p>
        <p>📊 Pandas / NumPy</p>
        <p>🌐 Flask Web Development</p>
        <p>📈 Data Visualization</p>
        <p>🎮 Game Systems Logic</p>
    </div>
    """
    return HTML.format(content=content)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")
        messages.append((name, message))

    messages_html = ""
    for m in messages:
        messages_html += f"<p><b>{m[0]}:</b> {m[1]}</p>"

    content = f"""
    <h1>Contact Me</h1>

    <form method="POST">
        <input type="text" name="name" placeholder="Your name" required><br>
        <textarea name="message" placeholder="Your message" required></textarea><br>
        <button type="submit">Send</button>
    </form>

    <div class="card">
        <h3>Messages</h3>
        {messages_html}
    </div>
    """

    return HTML.format(content=content)

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
