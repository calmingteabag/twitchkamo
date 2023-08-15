import os
import json

from configparser import ConfigParser

class GameConfig:
    def __init__(self):
        self.resources = os.path.join(
            os.getcwd(), 
            os.getenv("RESOURCES_PATH"), 
            os.getenv("TEST_RESOURCES")
            )


    def is_json_empty(self):

        if (os.path.getsize(self.resources) != 2):
            return False
        
        return True
    
    def json_build(self):

        if self.is_json_empty():

            with open(self.resources, 'r') as file:
                game_data = json.load(file)

            game_data["jogadores"] = {}

            with open(self.resources, 'w') as file:
                json.dump(game_data, file)

    def json_add_player(self):

        with open(self.resources, 'r') as file:
                game_data = json.load(file)

        game_data["jogadores"]["player"] = {
            "moedas" :0,
            "tempo_1": 'aaaa',
            "tempo_2": 'bbbb',
        }

        with open(self.resources, 'w') as file:
                json.dump(game_data, file)

