import os
from dotenv import load_dotenv

from flask import Flask, request
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration, ApiClient, MessagingApi,
    ReplyMessageRequest, TextMessage, ImageMessage
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent

load_dotenv()

# ===== REPLACE WITH YOUR TOKENS =====
CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")

app = Flask(__name__)
configuration = Configuration(access_token=CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# Add bosses here. Each command can have 1..n images.
PHOTOS = {
    "imove":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/iMove.jpeg"
    ],
    "irules":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/iRules.jpg"
    ],
    "iwolf":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/iWolf.jpeg"
    ],
    "wasteland scorpid":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Wasteland%20Scorpid%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Wasteland%20Scorpid%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Wasteland%20Scorpid%203.jpeg"
    ],
    "frostfeather flamen":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Frostfeather%20Flamen%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Frostfeather%20Flamen%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Frostfeather%20Flamen%203.jpeg"        
    ],
    "hellshade reaper":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Hellshade%20Reaper%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Hellshade%20Reaper%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Hellshade%20Reaper%203.jpeg"
    ],
    "surging spirit":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Surging%20Spirit%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Surging%20Spirit%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Surging%20Spirit%203.jpeg"
    ],
    "grimwing":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Grimwing%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Grimwing%20%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Grimwing%20%203.jpeg"
    ],
    "forest ranger":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Forest%20Ranger%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Forest%20Ranger%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Forest%20Ranger%203.jpeg"
    ],
    "blood hunter":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Bloodhunter%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Bloodhunter%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Bloodhunter%203.jpeg"
    ],
    "knight of judgement":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Knight%20of%20Judgement%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Knight%20of%20Judgement%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Knight%20of%20Judgement%203.jpeg"
    ],
    "boreal lord":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Boreal%20Lord%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Boreal%20Lord%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Boreal%20Lord%203.jpeg"
    ],
    "drakeslayer":[
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Drakeslayer%201.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Drakeslayer%202.jpeg",
        "https://raw.githubusercontent.com/ryonquah/BA-Games-LineBot/main/images/Drakeslayer%203.jpeg"
    ]
}

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature","")
    body = request.get_data(as_text=True)
    print(body)
    try:
        handler.handle(body, signature)
        return "OK"
    except InvalidSignatureError:
        return "Bad signature",400

@handler.add(MessageEvent, message=TextMessageContent)
def handle(event):
    cmd = event.message.text.lower().strip()
    with ApiClient(configuration) as api:
        bot = MessagingApi(api)
        if cmd=="help":
            txt="Available commands:\n\n"+"\n".join(PHOTOS.keys())
            bot.reply_message(ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=txt)]
            ))
            return
        if cmd in PHOTOS and PHOTOS[cmd]:
            msgs=[ImageMessage(original_content_url=u,preview_image_url=u) for u in PHOTOS[cmd]]
            bot.reply_message(ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=msgs
            ))

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
