from twitchio.ext import commands
from random import randint
from datetime import datetime

from .bot_config import PREFIX, CHANNELS

import json
import os

class KamoBot(commands.Bot):

    def __init__(self):
        self.resources = os.path.join(
            os.getcwd(), 
            os.getenv("RESOURCES_PATH"), 
            os.getenv("RESOURCES")
            )
        
        super().__init__(
            token=os.getenv("TOKEN"), 
            prefix=PREFIX, 
            initial_channels=CHANNELS
            
            )
        

    async def event_ready(self):

        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    # # Handlers
    async def event_message(self, message):

        if message.echo:
            return

        print(message)

        await self.handle_commands(message)

        if message.content == 'ping':
            await message.channel.send('pong')

        elif message.content == 'astro':
            await message.channel.send('boy')



    # Comandos

    @commands.command(name='test')
    async def test(self, ctx):
        
        print(self.resources)
        # print(os.sep)

        # file = self.directory + "src\modules\jogadores.json"
        # print(file)
  
        # full_path = os.path.join(self.directory, "sardinha")
        # print(full_path)



    @commands.command(name='jogar')
    async def jogar(self, ctx):
        new_player = ctx.author.name

        with open(self.resources, 'r') as file:
            game_data = json.load(file)

        if new_player not in game_data["jogadores"].keys():
            print("Adicionando jogador")
            

            time_now = datetime.now()
            time_stringfied = time_now.strftime("%Y-%m-%d %H:%M:%S.%f")

            game_data["jogadores"][new_player] = {
                        "moedas": 0,
                        "tempo_1": time_stringfied,
                        "tempo_2": time_stringfied
                }
            

            with open(self.resources, 'w') as file:
                json.dump(game_data, file)
                
            await ctx.send(f'Um novo jogador foi identificado. Seu nome é {ctx.author.name}.')
        
        await ctx.send(f'{ctx.author.name}, vc já está na lista de jogadores')

        

    @commands.command(name='moeda')
    async def moeda(self, ctx):

        player = ctx.author.name 

        with open(self.resources, 'r+') as file:
            game_data = json.load(file)

        if player not in game_data["jogadores"].keys():
            await ctx.send(f'{ctx.author.name}, vc não está na lista de jogadores. Use !jogar para iniciar')

        else:

            time_current = datetime.now()
            time_json = game_data["jogadores"][ctx.author.name]["tempo_1"]
            time_json_datetime = datetime.strptime(time_json, "%Y-%m-%d %H:%M:%S.%f")
            time_interval = time_current - time_json_datetime
            time_left = 900 - time_interval.seconds

            if game_data["jogadores"][player]["moedas"] == 0 or time_interval.seconds > 900:

                new_moedinhas = randint(0, 100)
                time_stringfied = time_current.strftime("%Y-%m-%d %H:%M:%S.%f")

                # updating and saving game data
                game_data["jogadores"][ctx.author.name]["moedas"] += new_moedinhas
                game_data["jogadores"][ctx.author.name]["tempo_1"] = time_stringfied

                with open(self.resources, 'w') as file:
                    json.dump(game_data, file)

                await ctx.send(f'O jogador {ctx.author.name} recebeu {new_moedinhas} moedas')
            
            else:
                await ctx.send(f'{ctx.author.name}, vc ja usou seu poder, espere mais {time_left} segundos')
   
                

    @commands.command(name='cofre')
    async def cofrinho(self, ctx):
        with open(self.resources, 'r+') as file:
            game_data = json.load(file)

        await ctx.send(f'{ctx.author.name}, vc tem {game_data["jogadores"][ctx.author.name]["moedas"]} moedas.')

    @commands.command(name='rank')
    async def rank(self, ctx):
        with open(self.resources, 'r+') as file:
            game_data = json.load(file)

            # preciso ler o json e organizar os jogadores por quantidade de moedas
        pass

    @commands.command(name='kamo')
    async def kamo(self, ctx):
        pass

    @commands.command(name='waifu')
    async def waifus(self, ctx):
        # print(ctx.author.channel.name)
        await ctx.send('Sends a waifu')

    @commands.command(name='randnum')
    async def randnun(self,ctx):

        num = randint(0, 1000)
        await ctx.send(str(num))

    