from flask import Flask, request
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage,
    ImageMessage,
)
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.exceptions import InvalidSignatureError

app = Flask(__name__)

# ==============================
# LINE BOT SETTINGS
# ==============================

CHANNEL_ACCESS_TOKEN = "YOUR_CHANNEL_ACCESS_TOKEN"
CHANNEL_SECRET = "YOUR_CHANNEL_SECRET"

configuration = Configuration(
    access_token=CHANNEL_ACCESS_TOKEN
)

handler = WebhookHandler(CHANNEL_SECRET)


# ==============================
# WEBHOOK CALLBACK
# ==============================

@app.route("/callback", methods=["POST"])
def callback():

    signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data(as_text=True)

    print("========== REQUEST ==========")
    print("Signature:", signature)
    print("Body:", body)

    try:
        handler.handle(body, signature)
        return "OK", 200

    except InvalidSignatureError:
        print("Invalid signature")
        return "Invalid signature", 400

    except Exception as e:
        import traceback
        traceback.print_exc()
        return "ERROR", 400


# ==============================
# MESSAGE COMMANDS
# ==============================

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):

    command = event.message.text.lower()

    with ApiClient(configuration) as api_client:

        line_bot_api = MessagingApi(api_client)


        # -----------------------
        # iMove Photo
        # -----------------------

        if command == "imove":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1mn4ihqgjXYkd0jJo_Q8dKaoayxFrDBLp",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1mn4ihqgjXYkd0jJo_Q8dKaoayxFrDBLp"
                        )
                    ],
                )
            )


        # -----------------------
        # iRules Photo
        # -----------------------

        elif command == "irules":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1oDYuVpQfQNkFBwe4-ttZDQqxlaQVGuBR",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1oDYuVpQfQNkFBwe4-ttZDQqxlaQVGuBR"
                        )
                    ],
                )
            )


        # -----------------------
        # iWolf Photo
        # -----------------------

        elif command == "iwolf":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1MYmclHmMMMfHhcoGOLr1EnHrP7ZkC3BL",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1MYmclHmMMMfHhcoGOLr1EnHrP7ZkC3BL"
                        )
                    ],
                )
            )


         # -----------------------
        # Wasteland Scorpid Photo (3 Photos)
        # -----------------------

        elif command == "wasteland scorpid":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1o7vQ2fOpm2uQMghbcviGdlE84mVHiUS1",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1o7vQ2fOpm2uQMghbcviGdlE84mVHiUS1"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1YPZva5UbhaDRhoyZe9LXwbFLd5czzPvp",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1YPZva5UbhaDRhoyZe9LXwbFLd5czzPvp"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1aOLi427ZI1akfJbcsvec5GIxD234IRw5",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1aOLi427ZI1akfJbcsvec5GIxD234IRw5"
                        )
                    ],
                )
            )


        # -----------------------
        # Frostfeather Flamen (3 Photos)
        # -----------------------

        elif command == "frostfeather flamen":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1n11hTe4LwnJ6A5UOSlQH-O5jhhsaC6OF",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1n11hTe4LwnJ6A5UOSlQH-O5jhhsaC6OF"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1nHaGw9T5jKkb1CnYb0WHMrykkRrM1Cg8",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1nHaGw9T5jKkb1CnYb0WHMrykkRrM1Cg8"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=12LjzkZJ3OH1n447ohipjYc6O_yKm9Gcy",
                            preview_image_url="https://drive.google.com/uc?export=view&id=12LjzkZJ3OH1n447ohipjYc6O_yKm9Gcy"
                        )
                    ],
                )
            )


        # -----------------------
        # Hellshade Reaper (3 Photos)
        # -----------------------

        elif command == "hellshade reaper":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1-vHCm9_syh4B-C11v_4sT0wkZ2cTshDO",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1-vHCm9_syh4B-C11v_4sT0wkZ2cTshDO"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1iL3hD6WBsz7dFv4q1RPz339ms80Sril0",
                            preview_image_url="Phttps://drive.google.com/uc?export=view&id=1iL3hD6WBsz7dFv4q1RPz339ms80Sril0"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1nBjYLU8LW8lb_HVmtZ3F4qICRWXKbxk6",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1nBjYLU8LW8lb_HVmtZ3F4qICRWXKbxk6"
                        )
                    ],
                )
            )


        # -----------------------
        # Surging Spirit (3 Photos)
        # -----------------------

        elif command == "surging spirit":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1X77I1yLuXMzUZvHbVlqoxO6ZpDbbGIFT",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1X77I1yLuXMzUZvHbVlqoxO6ZpDbbGIFT"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1cjFgrTkBidVKbwMrhsOzu3cFZg73kz5e",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1cjFgrTkBidVKbwMrhsOzu3cFZg73kz5e"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1gF-4mKXNf7DCChN0eHo4zDTTEvuW5d02",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1gF-4mKXNf7DCChN0eHo4zDTTEvuW5d02"
                        )
                    ],
                )
            )


        # -----------------------
        # Grimwing (3 Photos)
        # -----------------------

        elif command == "grimwing":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=15IJCMM3qa-CnuGA3_t0tcXSCcpWB_aop",
                            preview_image_url="https://drive.google.com/uc?export=view&id=15IJCMM3qa-CnuGA3_t0tcXSCcpWB_aop"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=13QiK8eL1aL7nbN64G2-9QL3vAVoRNn5L",
                            preview_image_url="https://drive.google.com/uc?export=view&id=13QiK8eL1aL7nbN64G2-9QL3vAVoRNn5L"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1uAFrAjkEceBqHOKjFFgMfRMBADld9eQi",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1uAFrAjkEceBqHOKjFFgMfRMBADld9eQi"
                        )
                    ],
                )
            )


        # -----------------------
        # Forest Ranger (3 Photos)
        # -----------------------

        elif command == "forest ranger":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1XclZr_ees5TGzyphPnntA4q6IMvz8cnF",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1XclZr_ees5TGzyphPnntA4q6IMvz8cnF"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1NGiAet9IWyzqd-gcLoZCyUAVsuWzZc5K",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1NGiAet9IWyzqd-gcLoZCyUAVsuWzZc5K"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1W09ZCZmb3HgpDRtuszGmXFJJqcOHaIcj",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1W09ZCZmb3HgpDRtuszGmXFJJqcOHaIcj"
                        )
                    ],
                )
            )


        # -----------------------
        # Blood Hunter (3 Photos)
        # -----------------------

        elif command == "blood hunter":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=18zyAT_QaBPU34aGYnFFsww14RkuRkBQY",
                            preview_image_url="https://drive.google.com/uc?export=view&id=18zyAT_QaBPU34aGYnFFsww14RkuRkBQY"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1czEVEcEZCeQ4uGUm5e7-uc1xvsxUVrY0",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1czEVEcEZCeQ4uGUm5e7-uc1xvsxUVrY0"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1aRDo9YSRex0tZH8CQAQUP7OQG8z8lLGJ",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1aRDo9YSRex0tZH8CQAQUP7OQG8z8lLGJ"
                        )
                    ],
                )
            )


        # -----------------------
        # Knight of Judgement (3 Photos)
        # -----------------------

        elif command == "knight of judgement":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1SSPZ9qBqCijQRd7W_aKj6asE7hrcF4vu",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1SSPZ9qBqCijQRd7W_aKj6asE7hrcF4vu"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1Fo8qUqqx31jmM-j23ynRv6GN86rBOzb_",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1Fo8qUqqx31jmM-j23ynRv6GN86rBOzb_"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1OEdWzEq9WhP7kUz9voFvbu6Tpg6IMsF5",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1OEdWzEq9WhP7kUz9voFvbu6Tpg6IMsF5"
                        )
                    ],
                )
            )


        # -----------------------
        # Boreal Lord (3 Photos)
        # -----------------------

        elif command == "boreal lord":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=15gLvi13h5oz5FjUqAbCIcPdlmBt4i0Ah",
                            preview_image_url="https://drive.google.com/uc?export=view&id=15gLvi13h5oz5FjUqAbCIcPdlmBt4i0Ah"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1ixIPw7janwKGMiahTMbpgK8WyG6ICtA1",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1ixIPw7janwKGMiahTMbpgK8WyG6ICtA1"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1eN6dzQoZ79WvlEz8BQ2JdSImdDUv_Nvp",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1eN6dzQoZ79WvlEz8BQ2JdSImdDUv_Nvp"
                        )
                    ],
                )
            )


        # -----------------------
        # Drakeslayer (3 Photos)
        # -----------------------

        elif command == "drakeslayer":

            line_bot_api.reply_message(
                ReplyMessageRequest(
                    reply_token=event.reply_token,
                    messages=[
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=15NyGTDsGoxvv8SpZRbAtnQXQ2f-mvuEk",
                            preview_image_url="https://drive.google.com/uc?export=view&id=15NyGTDsGoxvv8SpZRbAtnQXQ2f-mvuEk"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1ePv77ZCbAQNyE70IQSOMPfZk0cqa2pzI",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1ePv77ZCbAQNyE70IQSOMPfZk0cqa2pzI"
                        ),
                        ImageMessage(
                            original_content_url="https://drive.google.com/uc?export=view&id=1q05fyt4EqQmDx6hkBk0x5s5B01DGp7YZ",
                            preview_image_url="https://drive.google.com/uc?export=view&id=1q05fyt4EqQmDx6hkBk0x5s5B01DGp7YZ"
                        )
                    ],
                )
            )


        # Ignore other messages

        else:
            return



# ==============================
# START SERVER
# ==============================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )