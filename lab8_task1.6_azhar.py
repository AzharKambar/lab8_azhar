import requests

#замените chosen_id выбранным идентификатором задачи
chosen_id = 1

# изменяем значение в словаре, представляющем элемент задачи
upd_new["title"] = "ANOTHER NEW"

#выполняем PUT-запрос для обновления задачи
put_rsp = requests.put(f'https://jsonplaceholder.typicode.com/todos/{chosen_id}', json=upd_new)

# Печать содержимого ответа
print(put_rsp.json())

# Проверка кода состояния
if put_rsp.status_code >= 400:
    print(f"Ошибка: {put_rsp.status_code} - {put_rsp.text}")