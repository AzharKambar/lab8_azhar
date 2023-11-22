#В этом примере мы генерируем случайный идентификатор персонажа, используя random.randint(1, 826), и
# затем создаем объект random_character класса Character с использованием этого случайного идентификатора.

from character import Character
import requests
import random


# функция для получения данных о персонаже и создания экземпляра Character
def get_character_data(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        return Character(**json_response)
    else:
        print(f"ошибка. Код состояния: {response.status_code}")


# генерация случайного идентификатора персонажа от 1 до 826
random_character_id = random.randint(1, 826)

# создаем объект random_character класса Character
random_character = get_character_data(random_character_id)

# выводим на экран доступ к атрибутам объекта Character
print(f"ID случайного персонажа: {random_character.id}")
print(f"Имя случайного персонажа: {random_character.name}")
