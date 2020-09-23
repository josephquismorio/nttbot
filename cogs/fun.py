#a bunch of random tasks that can be called by users.

from discord.ext import commands
from discord.utils import get
import os
import urllib.parse, urllib.request, re
import random

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #simple ping command
    @commands.command(name = 'ping')
    async def ping(self, ctx):
        print('"Ping" command successfully executed.')
        await ctx.send('Pong! `' + str(round(self.bot.latency * 1000)) + ' ms`',
        delete_after = 5.0) #auto deletes after 5 seconds

    #simple youtube search command
    @commands.command(name = 'yts')
    async def yts(self, ctx, *, search):
        query = urllib.parse.urlencode({'search_query': search})
        htm_content = urllib.request.urlopen(
            'http://www.youtube.com/results?' + query)
        searchResults = re.findall(r'/watch\?v=(.{11})',
        htm_content.read().decode())
        await ctx.send(f':white_check_mark: Here you go, {ctx.author.name}! First result for "{search}" was: http://www.youtube.com/watch?v=' +
        searchResults[0])

    #random number generator that takes two inputs
    @commands.command(name = 'rng')
    async def rng(self, ctx):
        def check(m):
            return m.author.id == ctx.author.id and m.content.isdigit() and \
                    m.channel.id == ctx.channel.id
        await ctx.send("Type a number.")
        msg1 = await self.bot.wait_for("message", check=check)
        await ctx.send("Type a second, larger number.")
        msg2 = await self.bot.wait_for("message", check=check)
        x = int(msg1.content)
        y = int(msg2.content)
        if x < y:
            value = random.randint(x,y)
            await ctx.send(f"You got {value}.")
        else:
            await ctx.send(":x: Make sure your first number is smaller than your second number.")

    #slot machine, implemented from/slightly modified version of alexflipnote's fun.py cog
    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]**\n{ctx.author.name},"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")

def setup(bot):
    bot.add_cog(Fun(bot))
