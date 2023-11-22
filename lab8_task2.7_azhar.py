from episode import Episode
import requests


# функция для получения данных эпизода и создания экземпляра Episode
def get_episode_data(episode_id):
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = requests.get(url)

    if response.status_code == 200:
        json_rsp = response.json()
        return Episode(**json_rsp)
    else:
        print(f"Ошибка. Код состояния: {response.status_code}")


# список идентификаторов эпизодов для перебора
id_list = [1, 2, 3, 4, 5]

# список для хранения объектов Episode
ep_list = []

# перебор каждого идентификатора эпизода, получение данных и создание объектов Episode
for episode_id in id_list:
    episode_instance = get_episode_data(episode_id)

    if episode_instance:
        ep_list.append(episode_instance)

# получаем доступ к атрибутам каждого экземпляра Episode в ep_list
for episode_instance in ep_list:
    print(f"ID: {episode_instance.id}, Name: {episode_instance.name}")