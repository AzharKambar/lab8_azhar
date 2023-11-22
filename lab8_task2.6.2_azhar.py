#В Python двойные звездочки * в вызове функции используются для распаковки словаря.
# Если у вас есть словарь и вы используете * перед ним при вызове функции,
# он передает пары ключ-значение словаря в качестве аргументов ключевого слова в функцию.
#В контексте создания класса Episode метод _init_ класса ожидает несколько параметров, соответствующих атрибутам эпизода.
# Используя **json_response, мы передаем все пары ключ-значение из словаря json_response в качестве аргументов
# ключевого слова в конструктор класса Episode.
# Это краткий способ инициализации атрибутов класса без явного перечисления каждого из них.


from episode import Episode
import requests


# функция для получения данных эпизода и создания экземпляра эпизода
def get_episode_data(episode_id):
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = requests.get(url)

    if response.status_code == 200:
        json_rsp = response.json()
        return Episode(**json_rsp)
    else:
        print(f"ошибка. Код состояния: {response.status_code}")


# пример использования
fetch_episode = 1
episode_instance = get_episode_data(fetch_episode)

# доступ к атрибутам экземпляра Episode
print(f"ID эпизода: {episode_instance.id}")
print(f"Имя эпизода: {episode_instance.name}")