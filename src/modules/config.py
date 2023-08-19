from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')

PREFIX = config.get('BOT', 'prefix')
CHANNELS = config.get('BOT', 'channels').split()
RESOURCES_PATH = config.get('GAME', 'resources_path')
RESOURCES_FILE = config.get('GAME', 'resources_file')
CURRENCY = config.get('GAME', 'currency_name')
CURRENCY_COOLDOWN = config.get('GAME', 'currency_cooldown')
CURRENCY_RAND_LOW = config.get('GAME', 'currency_random_low')
CURRENCY_RAND_HIGH = config.get('GAME', 'currency_random_high')