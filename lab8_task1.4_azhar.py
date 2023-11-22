import requests

#определяем словарь для нового элемента задачи
new_task = {
    "userId": todo_sm.userId,
    "title": todo_sm.title,
    "completed": todo_sm.completed
}

#отправляем POST-запрос
rsp = requests.post('https://jsonplaceholder.typicode.com/todos', json=new_task)

 #выводим на экран содержимое ответа
print(rsp.json())

#проверяем код состояния
if rsp.status_code >= 400:
    print(f"Ошибка: {rsp.status_code} - {rsp.text}")