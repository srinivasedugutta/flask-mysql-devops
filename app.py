from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

@app.route("/")
def home():
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    cursor.execute("SELECT NOW();")
    result = cursor.fetchone()
    cursor.close()
    db.close()

    return jsonify({
        "message": "Flask + MySQL running in real DevOps pipeline 🚀",
        "db_time": str(result[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

