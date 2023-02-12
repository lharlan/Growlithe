import discord
from discord.ext import commands
import re
import os
import asyncio
from cogs.utils import checks


def calcSeconds(time): # time will be formatted as a 3 element list: ['', 'num', 'unit']

    time.pop(0)

    if time[1] == 's':
        return int(time[0])
    elif time[1] == 'm':
        return 60 * int(time[0])
    elif time[1] == 'h' or time[1] == 'hr':
        return 3600 * int(time[0])
    elif time[1] == 'd' or time[1] == 'days' or time[1] == 'day':
        return 86400 * int(time[0])
    else:
        return -1


async def messageUser(ctx, member, duration, message, status):

    if status == 'mute':
        mute_desc = 'You have been muted for {} for reason: '.format(duration) + message
        mute_embedVar = discord.Embed(title="**You have been muted in Zeraora\'s Emporium:**", description=mute_desc, color=0xe74c3c)

        try:
            await member.send(embed=mute_embedVar)
        except discord.errors.Forbidden:
            await ctx.send('I could not DM the user!')
            pass

    if status == 'unmute':
        unmute_desc = 'You have been unmuted. Please do take care to apply yourself to the rules in the future.'
        unmute_embedVar = discord.Embed(title="**You have been unmuted in Zeraora\'s Emporium:**", description=unmute_desc, color=0xe74c3c)

        try:
            await member.send(embed=unmute_embedVar)
        except discord.errors.Forbidden:
            await ctx.send('I could not DM the user!')
            pass


class MuteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='mute', help="Mutes a user for a given amount of time, specify `inf` for infinite time")
    async def mutemember(self, ctx, member: discord.Member = None, duration=None, *, mute_reason=None):

        roleobject = discord.utils.get(ctx.guild.roles, id=712569905043472426)
        infcheck = 0

        if mute_reason == None:
            mute_reason = 'No reason Given.'

        if duration != 'inf':
            # split time up
            try:
                durUnit = re.split('(\d+)',duration)
            except:
                await ctx.send('*ERROR:* Unable to split time correctly.')
                return
        elif duration == 'inf':
            infcheck = 1
        else:
            await ctx.send('*ERROR:* Unable to parse time correctly.')
            return

        if infcheck == 1:
            await member.add_roles(roleobject)
            await ctx.send('{} was given a permanent mute because reason: `{}`.'.format(member.mention, mute_reason))
            messageUser(ctx, member, 'infinite', mute_reason, 'mute')

            print("{} was muted".format(member.display_name))

        elif calcSeconds(durUnit) != -1 and infcheck == 0:
            await member.add_roles(roleobject)
            await ctx.send('{} was given a permanent mute because reason: `{}`.'.format(member.mention, mute_reason))
            await messageUser(ctx, member, duration, mute_reason, 'mute')

            print("{} was muted".format(member.display_name))

            await asyncio.sleep(calcSeconds(durUnit))

            if roleobject not in member.roles:
                return
            elif roleobject in member.roles:
                await member.remove_roles(roleobject)
                await ctx.send('{} was unmuted after recieving a `{}` mute because reason: `{}`'.format(member.mention, duration, mute_reason))
                await messageUser(ctx, member, duration, mute_reason, 'unmute')

                print("{} was unmuted".format(member.display_name))

        else:
            await ctx.send('*Error:* Could not process the mute command.')

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='unmute', help="Unmutes a user")
    async def unmutemember(self, ctx, member: discord.Member=None):

        roleobject = discord.utils.get(ctx.message.guild.roles, id=712569905043472426)

        if member == None:
            await ctx.send('*Error:* I need a user to unmute.')
        else:
            print("{} was unmuted".format(member.display_name))
            await member.remove_roles(roleobject)
            await ctx.send('{} has been unmuted.'.format(member.mention))

    @mutemember.error
    @unmutemember.error
    async def modcommands_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('User is not in this server or cannot be found..')
            return

async def setup(bot):
    await bot.add_cog(MuteCog(bot))