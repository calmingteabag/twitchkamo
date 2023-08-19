import os
import json

from .config import RESOURCES_PATH, RESOURCES_FILE

class GameConfig:
    def __init__(self):

        self.resources = os.path.join(
            os.getcwd(), 
            RESOURCES_PATH, 
            RESOURCES_FILE
            )
        


    def is_json_empty(self):

        if (os.path.getsize(self.resources) != 2):
            return False
        
        return True
    
    def json_build(self):

        if not self.is_json_empty():
            print("Json already constructed and/or not empty. ")
            return

        with open(self.resources, 'r') as file:
            game_data = json.load(file)

        game_data["jogadores"] = {}

        with open(self.resources, 'w') as file:
            json.dump(game_data, file)

    def json_add_player(self):

        with open(self.resources, 'r') as file:
                game_data = json.load(file)

        game_data["jogadores"]["player"] = {
            "moedas" : 0,
            "tempo_1": '',
            "tempo_2": '',
        }

        with open(self.resources, 'w') as file:
                json.dump(game_data, file)

