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

class MuteCog(commands.Cog, name='Mute'):
    def __init__(self, bot):
        self.bot = bot

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='mute', help="Mutes a user for a given amount of time, specify `inf` for infinite time")
    async def mutemember(self, ctx, member: discord.Member = None, duration=None, *, mute_reason=None):

        roleobject = discord.utils.get(ctx.guild.roles, id=712569905043472426)
        infcheck = False
        #await ctx.send(roleobject)

        if mute_reason == None:
            mute_reason = 'No reason Given.'
        elif '@everyone' in mute_reason or '@here' in mute_reason:
            await ctx.send('You cannot use me to ping everyone.')
            return

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

            # assigns the mute command
            try:
                await member.add_roles(roleobject)
                await ctx.send('{} was muted for `{}` because reason: `{}`'.format(member.mention, duration, mute_reason))

                # message user
                try:
                    mute_desc = 'You have been muted for {} for reason: '.format(duration) + mute_reason
                    mute_embedVar = discord.Embed(title="**You have been muted in Zeraora\'s Emporium:**", description=mute_desc, color=0xe74c3c)
                    await member.send(embed=mute_embedVar)
                except discord.errors.Forbidden:
                    await ctx.send('I could not DM the user!')
                    pass # dont fail incase user has blocked the bot

                print("{} was muted".format(member.display_name))

                # waits the set time
                await asyncio.sleep(calc_seconds(dur_and_unit))

                if roleobject not in member.roles:
                    return
                elif roleobject in member.roles: #incase manual unmute
                # remove mute role and inform user
                    await member.remove_roles(roleobject)
                    print("{} was auto unmuted".format(member.display_name))
                    await ctx.send('{} was unmuted after recieving a `{}` mute because reason: `{}`'.format(member.mention, duration, mute_reason))

                    try:
                        unmute_desc = 'You have been unmuted after `{}`.'.format(duration)
                        unmute_embedVar = discord.Embed(title="**You have been unmuted in Zeraora\'s Emporium:**", description=unmute_desc, color=0xe74c3c)
                        await member.send(embed=unmute_embedVar)
                    except discord.errors.Forbidden:
                        await ctx.send('I could not DM the user!')
                        pass # dont fail incase user has blocked the bot
                else:
                    pass

            except:
                await ctx.send('I could not add the muted role. Mute failed. Please ensure I have the ability to assign the Muted role and reattempt the mute.') 

        elif infcheck == False:
            return


    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='unmute', help="Unmutes a user")
    async def unmutemember(self, ctx, member: discord.Member=None):
        
        roleobject = discord.utils.get(ctx.message.guild.roles, id=712569905043472426)

        if not member:
            member = ctx.message.author

        unmute_embedVar = discord.Embed(title="**You have been unmuted in Zeraora\'s Emporium**", color=0xe74c3c)
        print("{} was manually unmuted".format(member.display_name))
        await member.remove_roles(roleobject)

        try:
            await member.send(embed=unmute_embedVar)
        except discord.errors.Forbidden:
            await ctx.send('I could not DM the user!')
            pass # dont fail incase user has blocked the bot

        await ctx.send('{} has been unmuted.'.format(member.mention))


    @mutemember.error
    @unmutemember.error
    async def modcommands_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('User is not in this server or cannot be found..')
            return
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('You need to give me a time! Use `inf` if you want an infinite mute\nOr there is a error parsing the userID, I am not sure because Logan isn\'t smart enough to code me <:slowshine:727863525007163452>.')
            return

async def setup(bot):
    await bot.add_cog(MuteCog(bot))