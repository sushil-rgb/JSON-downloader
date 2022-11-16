import requests
import random
import json
import os


# Fetching random user-agents from the text file while making a request to the server:
def userAgents():
    with open("user-agents.txt") as f:
        agents = f.read().split("\n")
        return random.choice(agents)


class LoadJson:
    def __init__(self):
        self.headers = {"User-Agent": userAgents()}

    def download_file(self, api_url, file_name):
        req = requests.get(api_url, headers=self.headers)
        api_call = req.content

        try:
            with open(f"{file_name}.json", 'wb') as f:
                f.write(api_call)
            print(f"{file_name} | saved.")

        except requests.JSONDecodeError:
            print("Unauthorised access!")

    def read_json(self, file_name):
        with open(f"{os.getcwd()}\\{file_name}.json", 'r') as f:
            api_call = json.load(f)

        return api_call
