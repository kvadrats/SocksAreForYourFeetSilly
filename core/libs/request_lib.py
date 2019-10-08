import requests


def send_post_json(url, payload, timeout=None):
    # todo: implement timeout
    response = requests.post(url=url, json=payload)
    json_response = response.json()
    return json_response


def send_get_json(url, params=None):
    response = requests.get(url, params)
    json_response = response.json()
    return json_response
