import random

from locust import HttpUser, task, between


class DmgUser(HttpUser):
    wait_time = between(3, 5)

    @task
    def random_breed(self):
        # get breed list
        breed_list_response = self.client.get("https://dog.ceo/api/breeds/list/all")
        breed_list_json = breed_list_response.json()
        # select random breed
        breed_choice = random.choice(list(breed_list_json["message"].keys()))
        # get random breed response
        self.client.get(f"https://dog.ceo/api/breed/{breed_choice}/list")

    @task
    def list_breeds(self):
        self.client.get("/breeds/list/all")

    @task(2)
    def random_image(self):
        self.client.get("/breeds/image/random")
