import discord
import os
from sys import argv


for arg in argv:
    if arg.startswith('-'):

        TOKEN = arg.replace("-", " ", 1)


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'xd':
        await message.channel.send("XD no beka")


    await message.channel.send("BYCZQ")
client.run(TOKEN)