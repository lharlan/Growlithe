import discord
from discord.ext import commands
import random

class SayHello(commands.Cog, name='Say Hello'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user or message.author.bot:
            return

        if message.content.lower() == "hi" or message.content.lower() == "hello":
            await message.add_reaction("🐾")
        #elif message.content.lower() == "bye":
        #    await message.channel.send("https://tenor.com/view/fuck-this-im-out-alpaca-gif-11489785")
        elif message.content.lower() == 'hi growlithe' or message.content.lower() == 'hello growlithe':
            await message.channel.send('Hello {}!'.format(message.author.display_name))
        else:
            pass

async def setup(bot):
    await bot.add_cog(SayHello(bot))
