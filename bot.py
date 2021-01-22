import discord
import os
from sys import argv

for arg in argv:
    if arg.startswith('-'):

        TOKEN = arg.replace("-", " ", 1)

client = discord.Client()

logging_channel = None

def log(author, message):
    if logging_channel is not None:
        logging_channel.send(f'[{author}] {message}')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Obecnie prace trwają..."))

@client.event
async def on_message(message:discord.message):
    if message.author == client.user:
        log(f'[{message.author}] ')
        return

    if message.author.server_permissions.administrator:
        if message.content == 'Logging channel':
            logging_channel = message.channel
            log("Bot", "Kanał ustawiony pomyślnie")





client.run(TOKEN)