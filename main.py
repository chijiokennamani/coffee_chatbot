from flask import Flask, request, jsonify, send_from_directory
from coffee_chatbot import get_reply

app = Flask(__name__, static_folder=".", static_url_path="")

@app.route("/", methods=["GET"])
def home():
    # Serves index.html from the same folder as app.py
    return send_from_directory(".", "index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    msg = request.json.get("message", "")
    return jsonify({"reply": get_reply(msg)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
