import requests

# выполненяем GET-запрос к API эпизода с идентификатором 1
url = "https://rickandmortyapi.com/api/episode/1"
rsp = requests.get(url)

# проверяем успешность запроса
if rsp.status_code == 200:
    # выводим ответ в формате JSON
    json_rsp = rsp.json()

    # отображаем структуры JSON
    print("JSON Structure:")
    for key, value in json_rsp.items():
        print(f"{key}: {type(value)}")
else:
    print(f"Ошибка. Код состояния: {rsp.status_code}")