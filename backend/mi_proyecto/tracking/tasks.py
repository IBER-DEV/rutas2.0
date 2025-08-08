from celery import shared_task
import requests

EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"

@shared_task
def send_expo_push(push_tokens, title, body, data=None):
    messages = []
    for token in push_tokens:
        messages.append({
            "to": token,
            "sound": "default",
            "title": title,
            "body": body,
            "data": data or {}
        })
    resp = requests.post(EXPO_PUSH_URL, json=messages)
    return resp.json()
