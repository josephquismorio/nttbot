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

#help command, with
@bot.command()
async def h(ctx):
    embed = discord.Embed(title = 'Commands')
    embed.add_field(name = '!ping', value = 'Gives a user their ping value in ms.', inline = False)
    embed.add_field(name = '!rng', value = 'A random number generator that gives you a random number given two inputs.', inline = False)
    embed.add_field(name = '!8ball', value = 'An 8 ball emulator. Ask it a question!\n')
    embed.add_field(name = '!yts', value = 'A youtube search engine that provides users with the first result of a YouTube search.', inline = False)
    embed.add_field(name = '!juul', value = 'Juul\n')
    embed.add_field(name = '!hannibal', value = 'IM HANNIBAL, YEAH YEAH', inline = False)
    embed.add_field(name = '!pretzel', value = 'pretzels is the same', inline = False)
    embed.add_field(name = '!ql', value = 'Quiplash! This command creates a game; input !start to start the game; !a and !b to answer prompts.', inline = False)
    await ctx.message.author.send(content=f':white_check_mark: Here you go, {ctx.author.name}! A list of commands:', embed=embed)


#shutdown bot
@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()
    await login(TOKEN, bot=True)
#to do: implement spotipy compatibility; other bs
bot.run(TOKEN)
