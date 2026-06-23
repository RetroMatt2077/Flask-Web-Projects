from flask import Flask, request
import requests

app = Flask(__name__)

# -----------------------------
# HTML UI (embedded)
# -----------------------------
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Weather App</title>
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
            margin-top: 100px;
        }

        input {
            padding: 10px;
            width: 200px;
            border-radius: 5px;
            border: none;
        }

        button {
            padding: 10px 15px;
            border: none;
            background: #38bdf8;
            cursor: pointer;
            border-radius: 5px;
        }

        .card {
            margin-top: 20px;
            background: #1e293b;
            padding: 20px;
            width: 300px;
            margin-left: auto;
            margin-right: auto;
            border-radius: 10px;
        }
    </style>
</head>
<body>

    <h1>🌦️ Weather App</h1>

    <form method="POST" action="/weather">
        <input type="text" name="city" placeholder="Enter city..." required>
        <button type="submit">Get Weather</button>
    </form>

    {result}

</body>
</html>
"""

# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return HTML_PAGE.format(result="")

# -----------------------------
# Weather Route
# -----------------------------
@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")

    try:
        # Get coordinates
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        geo_data = requests.get(geo_url).json()

        if "results" not in geo_data:
            return HTML_PAGE.format(result="<h3>❌ City not found</h3>")

        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]

        # Get weather
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )

        weather_data = requests.get(weather_url).json()
        current = weather_data["current_weather"]

        result_html = f"""
        <div class="card">
            <h2>Weather in {city.title()}</h2>
            <p>🌡️ Temperature: {current['temperature']}°C</p>
            <p>💨 Wind Speed: {current['windspeed']} km/h</p>
            <p>🌍 Weather Code: {current['weathercode']}</p>
        </div>
        """

        return HTML_PAGE.format(result=result_html)

    except Exception as e:
        return HTML_PAGE.format(result=f"<h3>❌ Error: {str(e)}</h3>")

# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
