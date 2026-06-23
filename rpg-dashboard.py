from flask import Flask

app = Flask(__name__)

# -----------------------------
# RPG DATA (same idea as your analysis project)
# -----------------------------
import numpy as np
import pandas as pd

np.random.seed(42)

names = [
    "Arin", "Lyra", "Kael", "Mira", "Doran",
    "Selene", "Rex", "Nova", "Vex", "Iris"
]

classes = ["Warrior", "Mage", "Archer", "Rogue", "Tank", "Healer"]

df = pd.DataFrame({
    "Name": names,
    "Class": np.random.choice(classes, size=len(names)),
    "Level": np.random.randint(1, 100, size=len(names)),
    "HP": np.random.randint(80, 500, size=len(names)),
    "Attack": np.random.randint(20, 150, size=len(names)),
    "Defense": np.random.randint(10, 120, size=len(names)),
    "Speed": np.random.randint(5, 100, size=len(names)),
    "Gold": np.random.randint(0, 10000, size=len(names))
})

# -----------------------------
# PowerScore system
# -----------------------------
df["PowerScore"] = (
    df["HP"] * 0.3 +
    df["Attack"] * 0.4 +
    df["Defense"] * 0.2 +
    df["Speed"] * 0.1
)

df = df.sort_values(by="PowerScore", ascending=False)

# -----------------------------
# HTML PAGE
# -----------------------------
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>RPG Dashboard</title>
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
            margin-top: 50px;
        }

        table {
            margin: auto;
            border-collapse: collapse;
            width: 80%;
            background: #1e293b;
        }

        th, td {
            padding: 12px;
            border: 1px solid #334155;
        }

        th {
            background: #38bdf8;
            color: black;
        }

        tr:hover {
            background: #334155;
        }

        h1 {
            margin-bottom: 20px;
        }

        .top {
            color: gold;
            font-weight: bold;
        }
    </style>
</head>
<body>

<h1>⚔️ RPG Character Dashboard</h1>

<table>
    <tr>
        <th>Rank</th>
        <th>Name</th>
        <th>Class</th>
        <th>Level</th>
        <th>HP</th>
        <th>Attack</th>
        <th>Defense</th>
        <th>Speed</th>
        <th>Gold</th>
        <th>PowerScore</th>
    </tr>

    {rows}
</table>

</body>
</html>
"""

# -----------------------------
# Build table rows
# -----------------------------
def build_rows():
    rows = ""
    for i, row in df.iterrows():
        rank_class = "top" if i == 0 else ""

        rows += f"""
        <tr class="{rank_class}">
            <td>{i + 1}</td>
            <td>{row['Name']}</td>
            <td>{row['Class']}</td>
            <td>{row['Level']}</td>
            <td>{row['HP']}</td>
            <td>{row['Attack']}</td>
            <td>{row['Defense']}</td>
            <td>{row['Speed']}</td>
            <td>{row['Gold']}</td>
            <td>{round(row['PowerScore'], 2)}</td>
        </tr>
        """
    return rows

# -----------------------------
# Route
# -----------------------------
@app.route("/")
def home():
    return HTML.format(rows=build_rows())

# -----------------------------
# Run app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
