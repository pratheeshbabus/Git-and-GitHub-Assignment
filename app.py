
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Git and GitHub Assignment - To-Do Application"

@app.route("/api")
def api():
    return jsonify({
        "message": "Welcome to the To-Do API",
        "status": "success"
    })

if __name__ == "__main__":
    app.run(debug=True)
