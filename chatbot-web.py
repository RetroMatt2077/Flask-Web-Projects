from flask import Flask, request

app = Flask(__name__)

# -----------------------------
# Simple chatbot logic
# -----------------------------
def get_bot_response(user_input):
    user_input = user_input.lower()

    # Greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hey! 👋 I'm your Python chatbot. How can I help?"

    # Weather
    if "weather" in user_input:
        return "I can't check live weather yet, but I can build that for you next 🌦️"

    # Coding help
    if "python" in user_input:
        return "Python is awesome 🐍 — try using Flask for web apps or Pandas for data analysis."

    # Games
    if "game" in user_input:
        return "I see you're into games 🎮 — you should connect your RPG stats to a Flask dashboard!"

    # Name question
    if "your name" in user_input:
        return "I'm a simple Flask chatbot built by you 😎"

    # Default response
    return "Hmm 🤔 I’m not sure about that yet, but I’m learning!"

# -----------------------------
# HTML UI (single file)
# -----------------------------
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Chatbot</title>
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

        .chatbox {
            margin-top: 20px;
            background: #1e293b;
            padding: 20px;
            width: 400px;
            margin-left: auto;
            margin-right: auto;
            border-radius: 10px;
        }
    </style>
</head>
<body>

    <h1>🤖 Flask Chatbot</h1>

    <form method="POST" action="/chat">
        <input type="text" name="message" placeholder="Say something..." required>
        <button type="submit">Send</button>
    </form>

    {chat}

</body>
</html>
"""

# -----------------------------
# Home route
# -----------------------------
@app.route("/")
def home():
    return HTML_PAGE.format(chat="")

# -----------------------------
# Chat route
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form.get("message")
    bot_reply = get_bot_response(user_message)

    chat_html = f"""
    <div class="chatbox">
        <p><b>You:</b> {user_message}</p>
        <p><b>Bot:</b> {bot_reply}</p>
    </div>
    """

    return HTML_PAGE.format(chat=chat_html)

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
