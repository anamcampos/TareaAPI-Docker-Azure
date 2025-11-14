from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

@app.route("/api")
def hello():
    return jsonify({"message": "API funcionando correctamente!"})

@app.route("/db")
def test_db():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        conn.close()
        return {"db_time": result[0]}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
