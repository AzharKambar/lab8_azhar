#1.2 и 1.3
class ToDo:
    def _init_(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# используем тот же post_id, что и ранее
post_id = 1

#создаем новый объект ToDo
todo_sm = ToDo(userId=1, id=post_id, title="Sample Title", completed=False)

 #осуществляем доступ к атрибутам объекта
print(f"User ID: {todo_sm.userId}")
print(f"ID: {todo_sm.id}")
print(f"Title: {todo_sm.title}")
print(f"Completed: {todo_sm.completed}")