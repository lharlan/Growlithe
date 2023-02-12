import discord
from discord.ext import commands
import asyncio
import time

class RaidDeleteCog(commands.Cog, name='Raid Delete'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        #test_ch = 900615660508446760 # personal test server channel
        raid_ch = 990708557064331324 # ZE raid channel
        log_ch = 783636198832078848 # logging channel in ZE, set to #snake currently
        del_time = 324000 # must be in seconds, 108000 is 30 min, 324000 is 90 min
        #messages_to_ignore = [990708829639561256, 990709462274814062] # message id, must be int

        if message.channel.id != raid_ch:
            return
        else:
            # does the deleting if message IDs do not match ignored messages, probably not necessary but doesn't hurt
            # also logs to terminal
            #print('Awaiting to delete message: ' + message.content + '. ID: ' + str(message.id))
            await asyncio.sleep(del_time)
            try:
                await message.delete()
            except:
                #await message.channel.send('I could not delete the recent message!')
                pass

            embedVar=discord.Embed(title="Message Deleted", description="<#990708557064331324>", color=0x992d22)
            embedVar.add_field(name="Author: ", value=str(message.author) + " | " + str(message.author.id), inline=False)
            embedVar.add_field(name="Content: ", value=message.content, inline=False)
            timestamp = time.strftime("%Y-%m-%d %H%M%S", time.localtime())
            embedVar.set_footer(text='Message Deleted at: ' + str(timestamp))
            channel = self.bot.get_channel(log_ch)
            await channel.send(embed=embedVar)
            #print('Deleted message: ' + message.content + '. ID: ' + str(message.id))


async def setup(bot):
    await bot.add_cog(RaidDeleteCog(bot))