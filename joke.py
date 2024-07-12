from abc import ABC, abstractmethod
import requests
import random

class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass

class A(Joke):
    def get_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data['value']
        else:
            return "Failed to fetch a joke"

class B(Joke):
    def get_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data['value']
        else:
            return "Failed to fetch a joke"

class C(Joke):
    def get_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data['value']
        else:
            return "Failed to fetch a joke"

joke_providers = [A(), B(), C()]
random_joke_provider = random.choice(joke_providers)
random_joke = random_joke_provider.get_random_joke()
print(f"Random joke: {random_joke}")
