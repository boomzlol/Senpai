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

@waifu.event
async def on_ready():
    print('Waifu is ready!')

    
waifu.run(config['token'])
