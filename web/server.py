from flask import Flask
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:5000/api")

app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get(API_URL).json()
    return f"<h1>Web funcionando</h1><p>Respuesta API: {r}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
