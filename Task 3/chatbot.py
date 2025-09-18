# chatbot.py
import json
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from flask import Flask, render_template, request, jsonify

# Download NLTK resources
nltk.download("punkt")

# Load intents
with open("intents.json", "r") as f:
    intents = json.load(f)

# Prepare data
patterns = []
tags = []
responses = {}

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

# Vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(patterns)

# Confidence threshold
CONFIDENCE_THRESHOLD = 0.3

def predict_intent(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    idx = similarity.argmax()
    confidence = similarity[0][idx]

    if confidence < CONFIDENCE_THRESHOLD:
        return "default"

    return tags[idx]

def get_response(intent):
    return random.choice(responses[intent]) if intent in responses else random.choice(responses["default"])


# -----------------------
# Console chatbot
# -----------------------
def run_console():
    print("🤖 CodTech Chatbot: Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Bot: Goodbye! Take care.")
            break
        intent = predict_intent(user_input)
        response = get_response(intent)
        print("Bot:", response)


# -----------------------
# Flask Web App
# -----------------------
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message")
    intent = predict_intent(user_input)
    response = get_response(intent)
    return jsonify({"response": response})


if __name__ == "__main__":
    # Uncomment below line to run in console mode
    # run_console()

    # Run Flask app
    app.run(debug=True)
