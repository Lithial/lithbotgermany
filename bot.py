import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()
token = 'NjAzNzE5NDIzMzgzMDQ0MTA3.XTjfxg.TTuZDdHVriBz6abeLlAW2WjZXu8'
@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

client.run(token)