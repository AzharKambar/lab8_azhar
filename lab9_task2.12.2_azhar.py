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


# создаем объект random_character класса Character
random_character_id = random.randint(1, 826)
random_character = get_character_data(random_character_id)

# примененяем метод
random_character.display_info()

if random_character.is_alive():
    print(f"{random_character.name} is alive.")
else:
    print(f"{random_character.name} is not alive.")