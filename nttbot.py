import discord
import os
import praw

from discord.ext import commands

from dotenv import load_dotenv

#reads .env file for user discord token

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#command prefix is set to '!'. commands are not case sensitive
bot = commands.Bot(command_prefix = '!', case_insensitive = True)

#confirm ntt bot works
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("suh dude simulator"))
    print(f'{bot.user} successfully booted.')
    bot.load_extension('cogs.fun')
    bot.load_extension('cogs.music')
    bot.load_extension('cogs.quiplash')
#to do: implement spotipy compatibility; other bs
bot.run(TOKEN)
