import discord
import os
from sys import argv

TOKEN = argv[1]

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)