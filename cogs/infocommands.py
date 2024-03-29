import discord
from discord.ext import commands
from cogs.utils import checks

class InfoCog(commands.Cog, name='Info Commands'):
    def __init__(self, bot):
        self.bot = bot

    # info command
    @commands.command(name='botinfo', help='Gives info about the bot', aliases=["ginfo", "info", "growlithe", "g"])
    async def botinfo(self, ctx):

        bot_version = '4.0.0'                # means nothing ngl, i just like it there LMFAO

        embed = discord.Embed(title="See our website for more info about us!\nhttps://zeraorasemporium.com/", color=0x992d22)
        embed.set_author(name='Growlithe v{}'.format(bot_version), icon_url=self.bot.user.display_avatar)
        embed.add_field(name='How to contact staff:', value='DM <@575252669443211264>')
        #info_embed.add_field(name="About Me:", value="I am a bot programmed in Python by <@462273017284919326> \nand hosted by <@686166019802136602>", inline=False)
        embed.add_field(name="About Me:", value="I am a bot hosted and developed by <@462273017284919326> and <@734119924464746637>.\nI am programmed in Python 3.10.7 and use v2.1.0 of Discord.py.", inline=False)
        embed.set_footer(text='Please contact LH#3527 for any bugs/issues with Growlithe')

        await ctx.send(embed=embed)

    #whois
    @commands.command(aliases=["whois"])
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def userinfo(self, ctx, * , member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
        embed.set_thumbnail(url=member.display_avatar)
        embed.set_footer(text=f"Requested by {ctx.author}")

        embed.add_field(name="Display Name:", value=member.display_name)
        embed.add_field(name="Mentionable Name:", value=member.mention)
        embed.add_field(name="ID:", value=member.id)
        global user_id
        user_id  = str(member)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="Roles:", value="".join([role.mention for role in member.roles[1:]]), inline=False)
        embed.add_field(name="Highest Role:", value=member.top_role.mention, inline=False)
        await ctx.send(embed=embed)
        await ctx.send(member.id)

    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send('user is not found.')

    #serverinfo shows information about the server serverinfo or server 
    @commands.command(aliases=["server"])
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def serverinfo(self, ctx, * , member: discord.Member = None):
        server = ctx.guild
        roles = str(len(server.roles))
        emojis = str(len(server.emojis))
        channels = str(len(server.channels))

        admin_role = ctx.guild.get_role(711901311234474054)
        moderator_role = ctx.guild.get_role(711901391555264514)
        supporter_role = ctx.guild.get_role(711904631852367974)

        embed = discord.Embed(title=server.name, colour=discord.Colour.blue())
        embed.set_thumbnail(url= ctx.guild.icon)
        embed.add_field(name="Server ID:", value=server.id, inline=False)
        embed.add_field(name="Total Users:", value=server.member_count, inline=True)
        embed.add_field(name="Server owner:", value='<@686166019802136602>', inline=True)
        embed.add_field(name="Verification Level:", value=server.verification_level, inline=True)
        embed.add_field(name="Roles:", value=roles, inline=True)
        embed.add_field(name='Server Admins', value=str(len(admin_role.members)), inline=True)
        embed.add_field(name='Server Moderators', value=str(len(moderator_role.members)), inline=True)
        embed.add_field(name='Server Supporters', value=str(len(supporter_role.members)), inline=True)
        embed.add_field(name='Channels', value=channels, inline=True)
        embed.add_field(name="Emoji:", value=emojis, inline=True)

        await ctx.reply(embed=embed)

    #membercount shows how many members in server
    @commands.command(aliases=["membercount"])
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def users(self, ctx, * , member: discord.Member = None):
        server = ctx.guild
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name="Total Server Members:", value=server.member_count, inline=True)
        return await ctx.reply(embed=embed)
  
    #show avatar from member 
    @commands.command(aliases=['av','avatar'])
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def showavatar(self, ctx, * , member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at, title=f"User Avatar - {member}")
        embed.set_image(url=member.display_avatar)
        embed.set_footer(text=f"Requested by {ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(name='rolecount')
    @commands.check_any(checks.is_logan(), checks.is_staff())
    async def rolecount(self, ctx, role: discord.Role = None):

        await ctx.send('There are `{}` members with the `{}` role.'.format(len(role.members), str(role)))


async def setup(bot):
    await bot.add_cog(InfoCog(bot))

    
