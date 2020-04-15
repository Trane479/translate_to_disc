import requests
from token_get import TOKEN


URL = 'https://cloud-api.yandex.net/v1/disk/resources/upload'


def write_to_disc(path):
    params = {
        'path': path,
        'overwrite': 'true'

    }
    headers = {
        'Authorization': TOKEN
    }
    response = requests.get(URL, params=params, headers=headers)
    json_ = response.json()
    print(json_)
    with open('test.txt') as f:
        text = f.read()
        requests.put(json_['href'], data=text.encode('utf-8'))


write_to_disc('test.txt')
