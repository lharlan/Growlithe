import discord
from discord.ext import commands

def roleid_to_name(roleid):
    if roleid == 764524310706257920:
        rolename = 'Announcements'
    elif roleid == 712560512730136616:
        rolename = 'Special Union Room'
    elif roleid == 714149413609799722:
        rolename = 'Giveaways'
    elif roleid == 748901587908558978:
        rolename = 'Server Events'
    elif roleid == 1047726132553842690:
        rolename = 'SV Raids'

    return rolename

def check_channel_id(channelid):
    channel_id_list = [906881436622159952, 771894077364764712, 778329754642022460, 711864261952929814]
    # muk, osha, mew, zera

    for channel in channel_id_list:
        if channelid == channel:
            return False

class GiveRoleCog(commands.Cog, name='Role Assigner'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='toggleannouncements', help='Gives/Removes the Announcements role.')
    async def toggleannouncements(self, ctx):

        if check_channel_id(ctx.channel.id) == False:
            await ctx.send("This is not the appropriate place! Please try again in <#711866446531002428>")
            return

        roleobject = discord.utils.get(ctx.guild.roles, id=764524310706257920)

        try:
            if roleobject not in ctx.author.roles:
                await ctx.author.add_roles(roleobject)
                await ctx.send('Successfully given the Announcements role.')
            elif roleobject in ctx.author.roles:
                await ctx.author.remove_roles(roleobject)
                await ctx.send('Successfully removed the Announcements role.')
        except:
            await ctx.send('**Error:** Could not execute the toggleannouncements function.')

    @commands.command(name='toggleunion', help='Gives/Removes the Special Union Room role.')
    async def toggleunion(self, ctx):

        if check_channel_id(ctx.channel.id) == False:
            await ctx.send("This is not the appropriate place! Please try again in <#711866446531002428>")
            return

        roleobject = discord.utils.get(ctx.guild.roles, id=712560512730136616)

        try:
            if roleobject not in ctx.author.roles:
                await ctx.author.add_roles(roleobject)
                await ctx.send('Successfully given the Special Union Room role.')
            elif roleobject in ctx.author.roles:
                await ctx.author.remove_roles(roleobject)
                await ctx.send('Successfully removed the Special Union Room role.')
        except:
            await ctx.send('**Error:** Could not execute the toggleunion function.')

    @commands.command(name='togglegiveaways', help='Gives/Removes the Giveaways role.')
    async def togglegiveaways(self, ctx):

        if check_channel_id(ctx.channel.id) == False:
            await ctx.send("This is not the appropriate place! Please try again in <#711866446531002428>")
            return

        roleobject = discord.utils.get(ctx.guild.roles, id=714116043072602144)

        try:
            if roleobject not in ctx.author.roles:
                await ctx.author.add_roles(roleobject)
                await ctx.send('Successfully given the Giveaways role.')
            elif roleobject in ctx.author.roles:
                await ctx.author.remove_roles(roleobject)
                await ctx.send('Successfully removed the Giveaways role.')
        except:
            await ctx.send('**Error:** Could not execute the togglegiveaways function.')

    @commands.command(name='toggleevents', help='Gives/Removes the Events role.')
    async def toggleevents(self, ctx):

        if check_channel_id(ctx.channel.id) == False:
            await ctx.send("This is not the appropriate place! Please try again in <#711866446531002428>")
            return

        roleobject = discord.utils.get(ctx.guild.roles, id=748901587908558978)

        try:
            if roleobject not in ctx.author.roles:
                await ctx.author.add_roles(roleobject)
                await ctx.send('Successfully given the Server Events role.')
            elif roleobject in ctx.author.roles:
                await ctx.author.remove_roles(roleobject)
                await ctx.send('Successfully removed the Server Events role.')
        except:
            await ctx.send('**Error:** Could not execute the toggleevents function.')

    @commands.command(name='toggleraids', help='Gives/Removes the SV Raids role')
    async def toggleraids(self, ctx):

        if check_channel_id(ctx.channel.id) == False:
            await ctx.send("This is not the appropriate place! Please try again in <#711866446531002428>")
            return

        roleobject = discord.utils.get(ctx.guild.roles, id=1047726132553842690)

        try:
            if roleobject not in ctx.author.roles:
                await ctx.author.add_roles(roleobject)
                await ctx.send('Successfully given the SV Raids role.')
            elif roleobject in ctx.author.roles:
                await ctx.author.remove_roles(roleobject)
                await ctx.send('Successfully removed the SV Raids role.')
        except:
            await ctx.send('**Error:** Could not execute the toggleraids function.')

    @commands.command(name='toggleall', help='Gives/Removes the SV Raids role')
    async def toggleall(self, ctx):

        if check_channel_id(ctx.channel.id) == False:
            await ctx.send("This is not the appropriate place! Please try again in <#711866446531002428>")
            return

        roleids = [764524310706257920, 712560512730136616, 714116043072602144, 748901587908558978, 1047726132553842690]

        for role in roleids:
            roleobject = discord.utils.get(ctx.guild.roles, id=role)

            rolename = roleid_to_name(role)

            try:
                if roleobject not in ctx.author.roles:
                    await ctx.author.add_roles(roleobject)
                    await ctx.send('Successfully given the {} role.'.format(rolename))
                elif roleobject in ctx.author.roles:
                    await ctx.author.remove_roles(roleobject)
                    await ctx.send('Successfully removed the {} role.'.format(rolename))
            except:
                await ctx.send('**Error:** Could not execute the toggleall function.')

    @commands.command(name='toggleroles', help='Gives a list of all the available roles to toggle.')
    async def toggleroles(self, ctx):

        if check_channel_id(ctx.channel.id) == False:
            await ctx.send("This is not the appropriate place! Please try again in <#711866446531002428>")
            return

        embedVar = discord.Embed(title="Toggleable Roles", description='', color=0xe74c3c)
        embedVar.add_field(name='!toggleannouncements', value='Gives/Removes the Annoucements role.', inline=False)
        embedVar.add_field(name='!toggleunion', value='Gives/Removes the Special Union Room role.', inline=False)
        embedVar.add_field(name='!togglegiveaways', value='Gives/Removes the Giveaways role.', inline=False)
        embedVar.add_field(name='!toggleevents', value='Gives/Removes the Server Events role.', inline=False)
        embedVar.add_field(name='!toggleraids', value='Gives/Removes the SV Raid Notification role.', inline=False)
        embedVar.add_field(name='!toggleall', value='Gives/Removes all the available toggleable roles.', inline=False)
        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(GiveRoleCog(bot))