import discord
from discord.ext import commands
import json


with open('config.json') as f: config = json.load(f)

waifu = commands.Bot(
    command_prefix='$',
    intents=discord.Intents.all(),
    case_insensitive=True,
    help_command=None   
)

@senpai.event
async def on_ready():
    print('Senpai is ready!')
    
 @senpai.command
async def ping(channel):
    await channel.send("pong")

    
waifu.run(config['token'])
