from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "BFFCIB0HZLYRKNZNEZMOINGIRLHBHZDUUCJVDWKAUXAWNSQCBGHNRAXQVTQRHJLA"

API = f"https://botapi.rubika.ir/v3/{TOKEN}"

CHANNEL = "@mojno313_ira"

def send_message(chat_id, text):

    requests.post(
        f"{API}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text
        }
    )

@app.route("/", methods=["POST"])
def bot():

    data = request.json

    if "update" in data:

        update = data["update"]

        if update["type"] == "NewMessage":

            text = update["new_message"].get("text")
            chat_id = update["chat_id"]

            if text == "/start":

                send_message(
                    chat_id,
                    f"""سلام ❤️

لطفا جهت استفاده از ربات در کانال زیر عضو شوید:

{CHANNEL}
"""
                )

    return {"ok": True}

app.run(host="0.0.0.0", port=8000)
