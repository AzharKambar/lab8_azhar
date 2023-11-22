class Episode:
    def _init_(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

    def display_info(self):
        print(f"Episode ID: {self.id}")
        print(f"Episode Name: {self.name}")
        print(f"Air Date: {self.air_date}")
        print(f"Episode Code: {self.episode}")
        print(f"Number of Characters: {len(self.characters)}")
        print(f"URL: {self.url}")
        print(f"Created: {self.created}")

    # проверяем, является ли данный персонаж частью эпизода
    def has_character(self, character_name):
        return character_name in self.characters


from episode import Episode
import requests


# функция для получения данных эпизода и создания экземпляра Episode
def get_episode_data(episode_id):
    url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        return Episode(**json_response)
    else:
        print(f"ошибка. Код состояния: {response.status_code}")


# список идентификаторов эпизодов для перебора
id_list = [1, 2, 3, 4, 5]

# список для хранения объектов Episode
ep_list = []

# перебор каждого идентификатора эпизода, получение данных и создание объектов Episode
for episode_id in id_list:
    episode_instance = get_episode_data(episode_id)

    if episode_instance:
        ep_list.append(episode_instance)

# используем методы, определенные в классе Episode
for episode_instance in ep_list:
    episode_instance.display_info()
    episode_instance.display_characters()