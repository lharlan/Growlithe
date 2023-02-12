import discord
from discord.ext import commands
from cogs.utils import checks

def calc_seconds(time):

    if time[2] == 's':
        return (int(time[1]))
    elif time[2] == 'm':
        return 60 * int(time[1])
    elif time[2] == 'hr' or time[2] == 'h':
        return 3600 * int(time[1])
    elif time[2] == 'd' or time[2] == 'days':
        return 86400 * int(time[1])
    else:
        return -1

class ModCommandsCog(commands.Cog, name='Moderation'):
    def __init__(self, bot):
        self.bot = bot

    # ban list test command
    @commands.command(name="banned")
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def banned(self, ctx, arg, arg2=None, arg3=None, arg4=None):

        if arg == 'add' or arg == 'a':
            banned_open = open('ban_list.txt', 'a')
            banned_open.write('\n' + arg2 + ' ' + arg3 + ' ' + arg4)
            banned_open.close()
            await ctx.send('Added `' + arg2 + '` to Banned Users!')

        elif arg == 'search' or arg == 's':
            banned = 0
            not_banned = 0
            with open('ban_list.txt', 'r') as banned_open_read:
                datasearch = banned_open_read.readlines()
            for line in datasearch:
                if arg2 in line:
                    banned = banned + 1
                    break
                else:
                    not_banned = not_banned + 1
            if not_banned >= len(datasearch):
                await ctx.send('`' + arg2 + '` is not a banned user!')
            if banned == 1:
                await ctx.send('`' + arg2 + '` is a banned user!')
            return

        elif arg == 'delete' or arg == 'd':
            with open('ban_list.txt', 'r') as banned_delete:
                datalines = banned_delete.readlines()
            with open('ban_list.txt', 'w') as banned_delete:  
                for line in datalines:
                    if arg2 not in line: #checks OT-TID, change to arg4 to check for nID
                        banned_delete.write(line)
                    else:
                        await ctx.send("Removed `" + line.rstrip() + "` from Banned Users!")
            return

        elif arg == 'list' or arg == 'l' or arg == 'users':
            banned_list = open("ban_list.txt", "r")
            banned_read = banned_list.read().splitlines()
            banned_read_new = list(filter(None, banned_read))

            banned_user = '\n'.join(banned_read_new)
            embed=discord.Embed(title="Banned Users", description=banned_user, color = 0x992d22)
            await ctx.send(embed=embed)
            return
        else: 
            embedVar = discord.Embed(title="Banned List Commands", description="Here are all the arguments I accept!", color=0xe74c3c)
            embedVar.add_field(name="Adding users to the banned list", value="Example: `&banned add OT-TID (ID: nintendo-id)`\nYou can also use `a` instead!", inline=False)
            embedVar.add_field(name="Removing users from the banned list", value="Example: `&banned delete OT-TID (ID: nintendo-id)`\nYou can also use `d` instead!", inline=False)
            embedVar.add_field(name="Searching users in the banned list", value="You don't have to include everything, you can just have the OT, TID, or nintendo-id, or any combination\nExample: `&banned search OT-TID (ID: discord-userid)`\nYou can also use `s` instead!", inline=False)
            embedVar.add_field(name="Viewing the whole banned list", value="Example: `&banned list`\nYou can also use `l` or `users` instead!", inline=False)
            await ctx.send(embed=embedVar)

    #purge command
    @commands.check_any(checks.is_logan(), checks.is_admin())
    @commands.command(name='purge')
    async def purge(self, ctx, limit: int, nomessage=False):
        await ctx.message.delete()
        await ctx.channel.purge(limit=limit)
        if nomessage == True:
            pass
        else:
            await ctx.send('Cleared by {}'.format(ctx.author.mention))
        print(str(ctx.author) + " purged " + str(limit) + " messages in channel " + str(ctx.channel))

    # kick
    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='removemember', aliases=['kick'])
    async def removemember(self, ctx, member: discord.Member=None, *, kickreason=None):

        if kickreason == None:
            responsereason = 'Reason has not been provided'
        if '@everyone' in kickreason or '@here' in kickreason:
            await ctx.send('You cannot use me to ping everyone.')
            return
        else:
            responsereason = 'Reason: ' + kickreason

        embedVar = discord.Embed(title="You have been kicked from Zeraora\'s Emporium", description=responsereason)
        memberstr = str(member)

        role3 = discord.utils.get(ctx.guild.roles, name="Moderator")
        role4 = discord.utils.get(ctx.guild.roles, name="Admin")

        if member in ctx.guild.members:

            if role3 in member.roles or role4 in member.roles:
                await ctx.send('I will not allow you to kick server staff!')
            else:
                await member.send(embed=embedVar)
                await member.kick(reason=kickreason)
                await ctx.send(memberstr + ' has been kicked `' + responsereason + '`')

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='banmember', aliases=['ban'])
    async def banmember(self, ctx, member: discord.Member=None, *, banreason=None):

        if banreason == None:
            responsereason = 'Reason has not been provided'
        elif '@everyone' in banreason or '@here' in banreason:
            await ctx.send('You cannot use me to ping everyone.')
            return
        else:
            responsereason = 'Reason: ' + banreason

        #banmessage = "You have been banned from Zeraora\'s Emporium:\n" + responsereason
        embedVar = discord.Embed(title="You have been banned from Zeraora\'s Emporium", description=responsereason)
        memberstr = str(member)

        role3 = discord.utils.get(ctx.guild.roles, name="Moderator")
        role4 = discord.utils.get(ctx.guild.roles, name="Admin")

        if member in ctx.guild.members:

            if role3 in member.roles or role4 in member.roles:
                await ctx.send('I will not allow you to ban server staff!')
            else:
                try:
                    await member.send(embed=embedVar)
                except:
                    await ctx.send('Could not DM user!')
                await member.ban(reason=banreason)
                await ctx.send(memberstr + ' has been banned `' + responsereason + '`')
                print(str(memberstr) + ' has been banned by ' + str(ctx.author))

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='nban')
    async def notinserverban(self, ctx, member_id):

        try:
            await ctx.guild.ban(discord.Object(id=member_id))

            user = await self.bot.fetch_user(member_id)

            await ctx.send(str(user) + ' | ' + str(member_id) + ' has been banned.')
            print(str(member_id) + ' was not in the server and has been banned by ' + str(ctx.author))
        except:
            await ctx.send('**Error:** Ban attempt failed, this command takes only a User ID.')

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='unbanmember', aliases=['unban'])
    async def unbanmember(self, ctx, member_id):

        await ctx.guild.unban(discord.Object(id=member_id))
        await ctx.send(str(member_id) + ' has been unbanned.')
        print(str(member_id) + ' has been unbanned by ' + str(ctx.author))

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='banall')
    async def banall(self, ctx, *, username=None):
        if username == None:
            await ctx.send('I need a username to match!')
            return
        else:
            guild = self.bot.get_guild(709788621896417370)
            member_count = 0
            
            for member in ctx.guild.members:
                if username in member.display_name:
                    try:
                        await member.ban(reason="Mass Ban Wave")
                        await ctx.send("Successfully banned " + member.mention)
                        member_count += 1
                        #await ctx.send('just a test no ban')
                    except:
                        await ctx.send("Ban failed for " + member.mention)
                        pass
                else:
                    pass

            await ctx.send("There are " + str(member_count) + " members that have been banned with " + username + " in their display name")

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='hide')
    async def hidechannel(self, ctx, channel: discord.TextChannel = None, role = None):
        if not channel:
            channel = ctx.channel

        if role == None:
            everyoneRole = ctx.guild.default_role
            await channel.set_permissions(everyoneRole, view_channel=False)
            await ctx.send('The View Channel permission for \@everyone is now turned off in <#{}>.'.format(str(channel.id)))
        else:
            customRole = ctx.guild.get_role(int(role))
            await channel.set_permissions(customRole, view_channel=False)
            await ctx.send('The View Channel permission for <@&{}> is now turned off in <#{}>.'.format(role, str(channel.id)))

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='unhide')
    async def unhidechannel(self, ctx, channel: discord.TextChannel = None, role = None, isNone = None):
        if not channel:
            channel = ctx.channel

        if role == None:
            everyoneRole = ctx.guild.default_role
            await channel.set_permissions(everyoneRole, view_channel=True)
            await ctx.send('The View Channel permission for \@everyone is now turned on in <#{}>.'.format(str(channel.id)))
        elif role == role.lower() == 'noneset' or role.lower() == 'setnone' or role.lower() == 'default' or role.lower() == 'setdefault' or role.lower() == 'defaultset':
            everyoneRole = ctx.guild.default_role
            await channel.set_permissions(everyoneRole, view_channel=None)
            await ctx.send('The View Channel permission for \@everyone is now set to default in <#{}>.'.format(str(channel.id)))
        else:
            customRole = ctx.guild.get_role(int(role))
            if isNone == None:
                await channel.set_permissions(customRole, view_channel=True)
                await ctx.send('The View Channel permission for <@&{}> is now turned on in <#{}>.'.format(role, str(channel.id)))
            elif isNone.lower() == 'noneset' or isNone.lower() == 'setnone' or isNone.lower() == 'default' or isNone.lower() == 'setdefault' or isNone.lower() == 'defaultset':
                await channel.set_permissions(customRole, view_channel=None)
                await ctx.send('The View Channel permission for <@&{}> is now set to default in <#{}>.'.format(role, str(channel.id)))
            


    @commands.has_any_role('Admin', 'Moderator')
    @commands.command(name='raid')
    async def raid(self, ctx):
        await ctx.message.delete()
        await ctx.send('<@&1047726132553842690>')

    @commands.has_any_role('Admin', 'Moderator', 'Giveaways Host 💰')
    @commands.command(name='giveaway')
    async def giveaway(self, ctx):
        await ctx.message.delete()
        await ctx.send('<@&714116043072602144>')
        await ctx.send('Want to get notified for this role? Use the command `!togglegiveaways`.')

    @removemember.error
    @banmember.error
    @unbanmember.error
    async def modcommands_error(self, ctx, error):
        if isinstance(error, commands.MemberNotFound):
            await ctx.send('User is not in this server or cannot be found. If you are attempting a ban on a user who is not in the server, please use `nban`.')
            return
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('You must provide a valid user ID')
            return

async def setup(bot):
    await bot.add_cog(ModCommandsCog(bot))
