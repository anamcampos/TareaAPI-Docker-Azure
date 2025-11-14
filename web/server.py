from flask import Flask, render_template_string
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:5000/api")

app = Flask(__name__)

@app.route("/")
def home():
    r = requests.get(API_URL)
    api_message = r.json()
    html = f"<h1>Web Funcionando</h1><p>Respuesta API: {api_message}</p>"
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
