import requests
import random
import json

cartoon_id = random.randint(1, 826)

#выполненяем GET-запрос к API
url = f"https://rickandmortyapi.com/api/character/{cartoon_id}"
rsp = requests.get(url)

#проверяем успешность запроса
if rsp.status_code == 200:
    #выводим ответ в формате JSON
    json_rsp = rsp.json()
    print(json_rsp)

    #отображаем ключи структуры JSON
    keys = json_rsp.keys()
    print(f"Keys: {keys}")

    #получаем список URL эпизодов
    url_ep = json_rsp.get("episode", [])

    # выводим список URL эпизодов
    print(f"URL эпизоды: {url_ep}")

    #создаем файл и добавляем в него URL каждого эпизода
    cartoon_file = f"episodes{cartoon_id}.txt"
    with open(cartoon_file, 'a', encoding='utf-8') as file:
        for ep_url in url_ep:
            file.write(f"{ep_url}\n")
    print(f"URL каждого эпизода добавлены в файл: {cartoon_file}")
else:
    print(f"Ошибка. Код состояния: {rsp.status_code}")