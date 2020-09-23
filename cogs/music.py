from discord.ext import commands
from discord.utils import get
import os

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

  #allows for bot to join user's voice channel.
    @commands.command(pass_context=True)
    async def join(self, ctx):
        global voice

        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.move_to(channel)
            print(f'{self.bot.user} has connected to {channel}.\n')
            await ctx.send(f":white_check_mark: Joined {channel}.", delete_after = 5.0)

        else:
            voice = await channel.connect()
            print(f'{self.bot.user} has connected to {channel}.\n')
            await ctx.send(f":white_check_mark: Joined {channel}.", delete_after = 5.0)

        if voice and voice.is_connected():
            await voice.move_to(channel)

        else:
            voice = await channel.connect()
            print(f'{self.bot.user} has connected to {channel}.\n')
            await ctx.send(f":white_check_mark: Joined {channel}.", delete_after = 5.0)

    #allows for bot to disconnect from user's voice channel.
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        channel = ctx.message.author.voice.channel
        voice = get(self.bot.voice_clients, guild = ctx.guild)

        if voice and voice.is_connected():
            await voice.disconnect()
            print(f'{self.bot.user} has left {channel}.\n')
            await ctx.send(f":white_check_mark: Left {channel}.", delete_after = 5.0)

        else:
            print("Bot cannot leave channel.")
            await ctx.send("Cannot leave channel (no voice channel recognized).", delete_after = 5.0)
def setup(bot):
    bot.add_cog(Music(bot))
