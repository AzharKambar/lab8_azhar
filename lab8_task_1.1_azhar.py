import requests

post_id = 1
url = f'https://jsonplaceholder.typicode.com/todos/{post_id}'

# отправляем GET-запрос
rsp = requests.get(url)

# выводим содержимое ответа (JSON)
print(rsp.json())

# проверяем если код состояния находится в диапазоне 400–499, 500–599, то выводим ошибку
if rsp.status_code >= 400:
    print(f"Ошибка: {rsp.status_code} - {rsp.text}")