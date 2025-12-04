from flask import Flask, render_template, request
import random

app = Flask(__name__)

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How’s it going?"],
    "hi": ["Hello!", "Hi! What can I do for you?", "Hey there!"],
    "how are you": ["I'm doing great, thanks!", "Feeling chatty today!"],
    "your name": ["You can call me ChatBot!", "I'm ChatBot, your virtual assistant."],
    "who are you": ["I'm a simple rule-based chatbot.", "Just a chatbot created using Python!"],
    "bye": ["Goodbye!", "See you soon!", "Bye! Have a nice day!"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm not sure I understand. Can you rephrase?"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.form["msg"]
    return get_response(user_input)

if __name__ == "__main__":
    app.run(debug=True)
