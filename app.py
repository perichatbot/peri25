from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def get_bot_response(message):
    msg = message.lower()
    if "hello" in msg or "hi" in msg:
        return "Hi there! 👋"
    elif "how are you" in msg:
        return "I'm just a bot, but I'm doing great!"
    elif "bye" in msg:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I didn't understand that."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    bot_reply = get_bot_response(user_msg)
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
