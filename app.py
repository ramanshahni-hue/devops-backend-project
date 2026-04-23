from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 DevOps Backend is Running!"

@app.route('/users')
def users():
    return jsonify([
        {"id": 1, "name": "Aman"},
        {"id": 2, "name": "Raj"}
    ])

app.run()