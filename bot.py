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

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == 'dm':
        await message.member.create_dm()
        await message.dm_channel.send(
        f'Hi, welcome to my Discord server!')
        return


    await message.channel.send(Byczq)
client.run(TOKEN)