import json

import requests

urls = 'http://openapi.turingapi.com/openapi/api/v2'
api_key = "6169e0899ecb40879793c816fdbdaa4c"
# 回复
def Turing(data):
    data_dict = {
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": data
            },
        },
        "userInfo": {
            "apiKey": api_key,
            "userId": "743228"
        }
    }
    result = requests.post(urls, json=data_dict)
    content = result.text
    # print(content)
    ans = json.loads(content)
    text = ans['results'][0]['values']['text']
    # print('Niubility:',text)  # 机器人取名就叫Niubility
    return text