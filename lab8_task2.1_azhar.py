#2.1 и 2.2
import requests
import random

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

    #отображение ключей структуры JSON
    keys = json_rsp.keys()
    print(f"\nКлючи структуры JSON: {keys}")
else:
    print(f"Ошибка. Код состояния: {rsp.status_code}")