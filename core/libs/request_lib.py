import requests
import json


def send_post_json(url, payload, timeout=None):
    # todo: implement timeout
    response = requests.post(url=url, json=payload)
    json_response = json.loads(response.json())
    return json_response
