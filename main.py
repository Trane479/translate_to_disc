import requests


#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20200411T160113Z.511f1ed91d9c74ef.bbc9b479034c6ba45d5d6bad777cd6fc277ea6d3'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'



def translate_it(filename, lang, to_path, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text:
    :param to_lang:
    :return:
    """
    with open(filename, 'rt') as f:
        text = f.read()
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-''{}'.format(lang, to_lang),
    }

    response = requests.get(URL, params=params)
    json_ = response.json()
    with open(to_path, 'wt') as f:
        f.write(''.join(json_['text']))

    return ''.join(json_['text'])


if __name__ == '__main__':
    print(translate_it('DE.txt', 'de', 'test.txt'))
