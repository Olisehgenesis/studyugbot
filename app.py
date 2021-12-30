
from flask import Flask
app = Flask(__name__)
from bot import *


@app.route('/{}'.format(secret), methods=["POST"])
def getdata():
    update = request.get_json()
    if "message" in update:
        chat_id = update["message"]["chat"]["id"]
        if "text" in update["message"]:
            text = update["message"]["text"]
            bot.sendMessage(chat_id, "From the web: you said '{}'".format(text))
        else:
            bot.sendMessage(chat_id, "From the web: sorry, I didn't understand that kind of message")
    return "OK"

if __name__=="__main__":
    app.run()