import discord
from discord.ext import commands

class RaidFinderCog(commands.Cog, name="Raid Tracker"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        thunderdome_ch = 714220630618275940
        raidlogs_ch = 1062767897497309265
        raidbans_ch = 1063597439698866267
        spam_ch = 732792223162433646

        if message.channel.id == raidlogs_ch:

            if "Banned User" in message.content:

                beforeName = message.content.split().index("User:")
                afterName = message.content.split().index("was")

                bannedUserList = message.content.split()[beforeName+1:afterName]
                bannedUser = ' '.join(bannedUserList)
                #print(bannedUser)
                channel = self.bot.get_channel(thunderdome_ch)

                await channel.send("{} was caught trying to join {}\'s raid: ".format(bannedUser, message.author.display_name) + message.jump_url)

                return

            elif "has been added to the banlist" in message.content:

                beforeName = message.content.split().index("Player:")
                afterName = message.content.split().index("has")

                bannedUserList = message.content.split()[beforeName+1:afterName]
                bannedUser = ' '.join(bannedUserList)
                #banBot = message.content.split()[3][:-8]

                channel = self.bot.get_channel(raidbans_ch)

                banReason = message.content.split()[-8:]
                banReason[1] = "**" + banReason[1] + "**"
                banReason = ' '.join(banReason)

                embedValue = "has been added to the banlist for {}\n\n**Ban Reason:** Player went over the catch limit.\n\nAppeal your ban in <#1061239837954428978>.".format(banReason)

                embed = discord.Embed(title="**{}**".format(bannedUser), description=embedValue, color=0xffffff)
                embed.set_thumbnail(url="https://i.imgur.com/ltJVcXT.png")
                #embed.add_field(name="Oopsie!", value="Appeal your ban in <#1061239837954428978>.", inline=False)

                await channel.send(embed=embed)

                #await channel.send("{} has been added to {}\'s banlist for {}\nPlease search your trainer name in <#1060631656584728616> to find the raid you are banned from and appeal your ban in <#1061239837954428978>.".format(bannedUser, banBot, banReason))
                #await channel.send('---------------------')

                return

            return

        else:
            pass

async def setup(bot):
    await bot.add_cog(RaidFinderCog(bot))