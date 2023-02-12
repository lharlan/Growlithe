import discord
from discord.ext import commands

class OwnerCog(commands.Cog, name='DM Logger'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.guild == None and not message.author.bot and not message.author.id == 462273017284919326:

            test_ch = 1057104601008062585
            growlithe_ch = 1057141425139105803
            channel = self.bot.get_channel(growlithe_ch)
            index = 0

            if len(message.content) > 0:
                content = message.content
            else:
                content = 'No text content, possible attachment.'

            await channel.send('Message recieved from {}!'.format(str(message.author)))
            await channel.send('**CONTENT:** `{}`'.format(content))

            if len(message.attachments) > 0:
                for attachment in message.attachments:
                    await channel.send(attachment.url)
                    index += 1

                    if index == 5:
                        break

            await channel.send('---------------------------')
            

async def setup(bot):
    await bot.add_cog(OwnerCog(bot))