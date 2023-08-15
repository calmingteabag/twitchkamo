from src.modules.bot import KamoBot
from src.modules.game_config import GameConfig

from dotenv import load_dotenv

load_dotenv()

game = GameConfig()
game.is_json_empty()
game.json_build()
game.json_add_player()

bot = KamoBot()
bot.run()