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

client.run(TOKEN)