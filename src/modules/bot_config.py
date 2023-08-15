from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini', encoding='utf-8')

PREFIX = config.get('BOT', 'prefix')
CHANNELS = config.get('BOT', 'channels').split()