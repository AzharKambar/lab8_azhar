class Character:
    def _init_(self, id, name, status, species, type, gender, origin, location, image, episode, url, created):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

    def display_info(self):
        print(f"Character ID: {self.id}")
        print(f"Character Name: {self.name}")
        print(f"Status: {self.status}")
        print(f"Species: {self.species}")
        print(f"Gender: {self.gender}")
        print(f"Origin: {self.origin['name']}")
        print(f"Location: {self.location['name']}")
        print(f"Image URL: {self.image}")
        print(f"Episode(s): {', '.join(self.episode)}")
        print(f"URL: {self.url}")
        print(f"Created: {self.created}")

    def is_alive(self):
        return self.status.lower() == 'alive'
