import requests

# Определение нового элемента задачи
todo_sm = {
    "userId": 1,
    "title": "Завершить задание",
    "completed": False
}

# Отправка POST-запроса для создания нового элемента задачи
post_url = "https://jsonplaceholder.typicode.com/todos"
post_response = requests.post(post_url, json=todo_sm)

# Вывод содержимого ответа
print("Содержимое ответа POST:")
print(post_response.content)

# Проверка кода состояния
if post_response.status_code in range(400, 600):
    print(f"Ошибка: {post_response.status_code} - {post_response.reason}")

# Редактирование некоторых данных созданного элемента задачи (например, изменение статуса выполнения)
if post_response.status_code == 201:  # Предполагается, что код состояния 201 указывает на успешное создание
    created_todo = post_response.json()
    print(created_todo)

    # Редактирование некоторых данных
    created_todo["completed"] = True

    # Отправка PUT-запроса для обновления элемента задачи
    put_url = f"https://jsonplaceholder.typicode.com/todos/{created_todo['id']}"
    put_response = requests.put(put_url, json=created_todo)

    # Вывод содержимого ответа
    print("\nСодержимое ответа PUT:")
    print(put_response.content)

    # Проверка кода состояния
    if put_response.status_code in range(400, 600):
        print(f"Ошибка: {put_response.status_code} - {put_response.reason}")