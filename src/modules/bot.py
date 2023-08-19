from twitchio.ext import commands
from random import randint
from datetime import datetime

from .config import (
    PREFIX, 
    CHANNELS, 
    RESOURCES_PATH, 
    RESOURCES_FILE,
    CURRENCY,
    CURRENCY_COOLDOWN,
    CURRENCY_RAND_LOW,
    CURRENCY_RAND_HIGH
    )

import json
import os

class KamoBot(commands.Bot):

    def __init__(self):
        self.resources = os.path.join(
            os.getcwd(), 
            RESOURCES_PATH, 
            RESOURCES_FILE,
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

        await self.handle_commands(message)

        if message.content == 'ping':
            await message.channel.send('pong')

        elif message.content == 'astro':
            await message.channel.send('boy')



    # Comandos

    @commands.command(name='test')
    async def test(self, ctx):
        
        print(self.resources)

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
                        "cooldown_moeda": time_stringfied,
                        "cooldown_aposta": time_stringfied
                }
            

            with open(self.resources, 'w') as file:
                json.dump(game_data, file)
                
            await ctx.send(f'Um novo jogador foi identificado. Seu nome é {ctx.author.name}.')
        
        else:

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
            time_json = game_data["jogadores"][ctx.author.name]["cooldown_moeda"]
            time_json_datetime = datetime.strptime(time_json, "%Y-%m-%d %H:%M:%S.%f")
            time_interval = time_current - time_json_datetime
            time_left = int(CURRENCY_COOLDOWN) - time_interval.seconds

            if game_data["jogadores"][player]["moedas"] == 0 or time_interval.seconds > int(CURRENCY_COOLDOWN):

                new_moedinhas = randint(int(CURRENCY_RAND_LOW), int(CURRENCY_RAND_HIGH))
                time_stringfied = time_current.strftime("%Y-%m-%d %H:%M:%S.%f")

                # updating and saving game data
                game_data["jogadores"][ctx.author.name]["moedas"] += new_moedinhas
                game_data["jogadores"][ctx.author.name]["cooldown_moeda"] = time_stringfied

                with open(self.resources, 'w') as file:
                    json.dump(game_data, file)

                await ctx.send(f'O jogador {ctx.author.name} recebeu {new_moedinhas} {CURRENCY}')
            
            else:
                await ctx.send(f'{ctx.author.name}, vc ja usou seu poder, espere mais {time_left} segundos')
   
                

    @commands.command(name='cofre')
    async def cofrinho(self, ctx):
        with open(self.resources, 'r+') as file:
            game_data = json.load(file)
            moedas_qty = game_data["jogadores"][ctx.author.name]["moedas"]

        await ctx.reply(f'{ctx.author.name}, vc tem {moedas_qty} {CURRENCY}.')

    @commands.command(name='rank')
    async def rank(self, ctx):
        with open(self.resources, 'r+') as file:
            game_data = json.load(file)

            # preciso ler o json e organizar os jogadores por user_qty de moedas
        pass

    @commands.command(name='aposta')
    async def aposta(self, ctx, type=None, user_qty=None):
        TIPOS = ['loterica', 'bet365', 'farialimer', 'agiota']
        BET_LIST = {
            'loterica' : {
            },
            'bet365': {},
            'farialimer':{},
            'agiota' :{}
        }
        # loterica retorna valor pequenoi com maior chance de ganhar
        # agiota, retorna valor alto, com menor chance de ganhar

        # Checks
        if type is None or user_qty is None:
            await ctx.reply(f'{ctx.author.name}, Não consigo realizar a aposta. Use !aposta <type> <user_qty>')
        elif type not in BET_LIST.keys():
            await ctx.reply(f'Não entendi que aposta você quer fazer, {ctx.author.name}.')

            return
        
        int_qty = int(user_qty)
        with open(self.resources, 'r+') as file:
            game_data = json.load(file)

        
        if int_qty <= 0:
            await ctx.reply(f'Aposte valores positivos, {ctx.author.name}.')
        elif int_qty > game_data["jogadores"][ctx.author.name]["moedas"]:
            await ctx.reply(f'{ctx.author.name}, você não tem moedas suficientes para essa aposta. Escolha um valor menor.')

            return

        # Gambling execution
        await ctx.reply(f'Aposto miseravi {ctx.author.name}.')
        


    
        # await ctx.send('test')

    @commands.command(name='waifu')
    async def waifus(self, ctx):
        # print(ctx.author.channel.name)
        await ctx.send('Sends a waifu')


    