import requests

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
API_KEY = 'trnsl.1.1.20190823T175639Z.1446a0abff49e275.33258ac05a45b09918fd4a78e2ea3b24b7a40650'


def translate_it(text, from_lang='en', to_lang='ru'):
    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(from_lang, to_lang),
    }

    response = requests.get(URL, params=params)
    return response.json()


if __name__ == "__main__":
    print(''.join(translate_it('homework')['text']))
