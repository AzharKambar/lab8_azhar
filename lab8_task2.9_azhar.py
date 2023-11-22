#ключ ‘origin’ относится к месту происхождения персонажа.
# В структуре данных для каждого персонажа возвращается информация о его происхождении,
# представленная объектом с различными атрибутами.

import requests

#выполняем GET-запрос к конечной точке персонажа
url = "https://rickandmortyapi.com/api/character/1"
response = requests.get(url)

# проверяем успешность запроса
if response.status_code == 200:
    # выводим ответ в формате JSON
    json_response = response.json()
    print(json_response)

    # изучение ключей в структуре JSON
    keys = json_response.keys()
    print(f"Ключи в структуре JSON: {keys}")

    #изучение структуры ключа 'origin'
    if 'origin' in keys:
        origin_keys = json_response['origin'].keys()
        print(f" 'origin': {origin_keys}")

else:
    print(f"ошибка. Код состояния: {response.status_code}")