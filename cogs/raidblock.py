import discord
from discord.ext import commands
import re
import asyncio
from cogs.utils import checks

def calc_seconds(time):

    if time[2] == 's':
        return (int(time[1]))
    elif time[2] == 'm':
        return 60 * int(time[1])
    elif time[2] == 'hr' or time[2] == 'h':
        return 3600 * int(time[1])
    elif time[2] == 'd' or time[2] == 'days' or time[2] == 'day':
        return 86400 * int(time[1])
    else:
        return -1

class RaidBlockCog(commands.Cog, name='Raid Blocking'):
    def __init__(self, bot):
        self.bot = bot

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='raidblock', help="Blocks a user for a given amount of time, from the SV raid channels, specify `inf` for infinite time", aliases=['raidmute'])
    async def raidblockmember(self, ctx, member: discord.Member=None, duration='24h'):

        roleobject = discord.utils.get(ctx.guild.roles, id=1048480051336839238)
        infcheck = False
        #await ctx.send(roleobject)

        if duration != 'inf':
            # split time up
            try:
                dur_and_unit = re.split('(\d+)',duration)
            except:
                await ctx.send('An error occured when processing the `mute` command! If you\'re reading this means something fucked up big time, that something is `dur_and_unit = re.split(\'(\d+)\',duration)` and Logan will want to bash his head on the wall.')
                return
        elif duration == 'inf':
            infcheck = True
        else: # == None
            await ctx.send('An error occured when processing the `mute` command! Please ensure you\'ve entered a duration and it\'s correct.')
            return

        if calc_seconds(dur_and_unit) == -1:
            await ctx.send('Not a valid time unit, use `s` for seconds, `m` for minutes, `hr` or `h` for hours, `d` or `days` for days.')
            return

        elif infcheck == False and calc_seconds(dur_and_unit) != -1: #checks to make sure time is valid before muting

            # kicks from VC and assigns the raid muted command
            try:

                try:
                    await member.move_to(None)
                except:
                    pass

                await member.add_roles(roleobject)
                await ctx.send('{} was blocked from the SV raids for `{}`.'.format(member.mention, duration))

                print("{} was blocked".format(member.display_name))

                # waits the set time
                await asyncio.sleep(calc_seconds(dur_and_unit))

                if roleobject not in member.roles:
                    return
                elif roleobject in member.roles: #incase manual unblock
                # remove mute role and inform user
                    try:
                        await member.remove_roles(roleobject)
                        print("{} was auto unblocked".format(member.display_name))
                        await ctx.send('{} was unblocked from the SV raid channels after recieving a `{}` block.'.format(member.mention, duration))
                    except:
                        await ctx.send("I cannot remove the Raid Muted role from {}! They need manually unblocked.".format(member.mention))
                else:
                    pass

            except:
                await ctx.send('I could not add the Raid Muted role. Block failed. Please ensure I have the ability to assign the Raid Muted role and reattempt the block.') 

        elif infcheck == False:
            return


    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='raidunblock', help="Unblocks a user from the SV raid channels.", aliases=['raidunmute'])
    async def raidunblockmember(self, ctx, member: discord.Member=None):

        roleobject = discord.utils.get(ctx.message.guild.roles, id=1048480051336839238)

        if not member:
            member = ctx.message.author

        print("{} was manually unblocked".format(member.display_name))
        await member.remove_roles(roleobject)

        await ctx.send('{} has been unblocked from the SV raid channels.'.format(member.mention))


    @raidblockmember.error
    @raidunblockmember.error
    async def modcommands_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('User is not in this server or cannot be found..')
            return
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('You must provide a valid user ID.')
            return

async def setup(bot):
    await bot.add_cog(RaidBlockCog(bot))