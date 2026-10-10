
import os
import json
from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

mongo_client = MongoClient(os.getenv("MONGO_URI"))
database = mongo_client["todo_database"]
todo_collection = database["todo_items"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName", "").strip()
    item_description = request.form.get("itemDescription", "").strip()

    if not item_name or not item_description:
        return "Item name and description are required.", 400

    todo_collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return "To-Do item saved successfully to MongoDB!"


if __name__ == "__main__":
    app.run(debug=True)
