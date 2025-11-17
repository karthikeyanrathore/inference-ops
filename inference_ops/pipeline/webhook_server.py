#!/usr/bin/env python3
# OpenAI webhook: https://platform.openai.com/docs/guides/webhooks
from flask import Flask
from flask import request, make_response
import os
import openai
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(webhook_secret=os.environ["OPENAI_WEBHOOK_SECRET"])

@app.route("/openai/webhook", methods=["POST"])
def webhook_openai():
    webhook_unwrap = client.webhooks.unwrap
    try:
        event = webhook_unwrap(request.data, request.headers)
        # _create_task(event)
        if event.type == "response.completed":
            # _noitfy_dashbord()
            response_id = event.data.id
            response = client.responses.retrieve(response_id)
            print(f"response output: {response}")
        else:
            # handle failure
            # notify dashboard
            pass
        return make_response({"message": "success"}, 200)
    except openai.InvalidWebhookSignatureError as error:
        print("invalid signature", e)
        return make_response({"error": "invalid signature"}, 400)

if __name__ == "__main__":
    app.run(debug=True, port=9809)