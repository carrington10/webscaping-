#bot 

import os 
import discord
from  dotenv import load_dotenv

DISCORD_TOKEN=""
GUILD = ""
load_dotenv();
Token = DISCORD_TOKEN

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
        guild = discord.utils.find(lambda g: g.name == GUILD, client.guilds)
        print(f"{client.user} has connected to discord")
        print(f'{guild.name}(id: {guild.id})')

client.run(Token)       