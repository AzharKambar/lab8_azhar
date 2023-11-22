import requests
import random
import json

#генерируем random персонажа
cartoon_id = random.randint(1, 826)

#выполняем GET-запроса к API
url = f"https://rickandmortyapi.com/api/character/{cartoon_id}"
rsp = requests.get(url)

#проверяем успешность запроса (код состояния 200)
if rsp.status_code == 200:
    #выводим ответ в формате JSON
    json_rsp = rsp.json()
    print(json_rsp)

    #выводим ключи структуры JSON
    keys = json_rsp.keys()
    print(f"Keys of JSON: {keys}")

    #создаем файл и сохраняем в него JSON-ответ
   cartoon_file = f"info_character_{cartoon_id}.json"
    with open(cartoon_file, 'w', encoding='utf-8') as file:
        json.dump(json_rsp, file, ensure_ascii=False, indent=4)
    print(f"Сохранено: {cartoon_file}")
else:
    print(f"Ошибка.Код состояния: {rsp.status_code}")