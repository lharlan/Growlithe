import discord
from discord.ext import commands

class LanShameCog(commands.Cog, name='Lan Shame'):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        muk_lan_ch = 906881436622159952

        swsh_ch = 711860459325882409
        bdsp_ch = 907682560002363472
        pla_ch = 928344876771311686
        channel = self.bot.get_channel(muk_lan_ch)

        #shame_content = 'Do kids not know what LAN is these days? Is that archaic now? I mean it\'s in the name. Even if you don\'t remember LAN parties there should be LAN options on consoles and stuff isn\'t there?'
        shame_content_1 = ', Why is it you decided not to read the pins or channel description or our website before trying the lan bot? It has \"lan\" in the channel name so surely it should have been obvious this bot is different.\n'
        shame_content_2 = 'Had you read any of those you would have known that this bot doesn\'t accept showdown formats, and only accepts pk8 files. I suggest reading the pins.'
        shame_content_3 = 'I\'ll even link the website for you: http://zeraorasemporium.com/#laninfo.'

        if message.author == self.bot.user or message.author.bot:
            return

        if message.channel.id == muk_lan_ch and '$trade' in message.content and len(message.content) > 7:
            await message.channel.send('Hello, ' + message.author.mention + shame_content_1 + shame_content_2)
        else:
            pass

        if (message.channel.id == swsh_ch or message.channel.id == bdsp_ch or message.channel.id == pla_ch) and '$trade' in message.content.lower():
            
            embed_title = "Looks like you\'re in the wrong place bucko, this ain\'t the place for tradin\'"
            embed_desc = "Here are the bot channels, pick the one for the game you\'re playing (tip read the channel names to discover which bot is for what game)\n<#711864261952929814>\n<#778329754642022460>\n<#771894077364764712>"

            embed=discord.Embed(title=embed_title, description=embed_desc, color=0x992d22)

            await message.channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(LanShameCog(bot))
