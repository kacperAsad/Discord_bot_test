import discord
import os
from sys import argv

print("WYPISYWANIE ARGUMENTÓW")
for arg in argv:
    print(arg)
print("ZAKOŃCZONO")


# for arg in argv:
#     if arg.startswith('-'):
#
#         TOKEN = arg.replace("-", " ", 1)
#
#
# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#
# client.run(TOKEN)