import requests
import json


def data_collection():
    url = "https://my.api.mockaroo.com/data_generator.json?key=19765d00"
    payload = {}
    headers = {
    }
    response = requests.request(
        "GET", url, headers=headers, data=json.dumps(payload))

    list1 = response.json()
    # print(list1)
    return list1
