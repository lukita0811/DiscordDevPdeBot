#Blibiotecas, comandos e libraries

import discord 
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = 'p!', intents = intents)

TOKEN = 'TOKEN AQUI'

#Falar para o console que o BOT está on
@bot.event
async def on_ready():
    print('Estou online e funcionando!')
    try: 
        synced = await bot.tree.sync()
        print(f'{len(synced)} comando(s) sincronizados.')
    except Exception as e:
        print(e)


#Quando alguém marcar o BOT dar uma mensagem
@bot.event 
async def on_message(message):
    if bot.user.mention in message.content:
        await message.channel.send('Olá meu amigo, você pode digitar "p!ajuda" para obter ajuda.')



#Comando de ajuda




#Comando de apresentação
@bot.tree.command(name='ola')
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Olá {interaction.user.mention}! Eu sou o PDEBOT.')
    

#Comando de falar por você
@bot.tree.command(name='falar')
@app_commands.describe(thing_to_say = 'Oque eu deveria falar por você?')
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f'{interaction.user.name} falou: {thing_to_say}')


bot.run(TOKEN)    
