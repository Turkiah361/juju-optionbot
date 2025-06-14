from flask import Flask, request
import requests

# Your Telegram Bot Token
TOKEN = "7922821938:AAGCQ-wQDaWLNYrvGRlNDuefArqt4DMhGA4"
URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

app = Flask(__name__)

def respond(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(URL, json=payload)

@app.route(f"/{TOKEN}", methods=["POST"])
def telegram_webhook():
    data = request.get_json()
    if "message" in data:
        chat_id = data["message"]["chat"]["id"]
        user_message = data["message"].get("text", "")

        # Handle different commands
        if user_message.lower() in ["/start", "hi", "hello"]:
            respond(chat_id, "Welcome to Juju'sOptionbot 📈! Send a ticker symbol (e.g., AAPL) to get a strategy.")
        elif user_message.isalpha() and len(user_message) <= 5:
            # You can add your AI strategy logic here
            respond(chat_id, f"Running AI analysis for {user_message.upper()}... (this is a placeholder)")
        else:
            respond(chat_id, "Sorry, I didn’t understand that. Send a ticker like TSLA or AAPL.")

    return {"ok": True}

if __name__ == "__main__":
    app.run(port=5002)
