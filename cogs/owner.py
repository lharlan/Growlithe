import discord
from discord.ext import commands
import socket
from cogs.utils import checks

class OwnerCog(commands.Cog, name='Maintence'):
    def __init__(self, bot):
        self.bot = bot

    # Hidden means it won't show up on the default help.
    @commands.command(name='load', hidden=True)
    @checks.is_logan()
    async def cogload(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        if cog[0:5] != "cogs.":
            cog = "cogs." + cog
        else:
            pass

        try:
            await self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**ERROR:** {type(e).__name__} - {e}')
        else:
            await ctx.send('Successfully loaded ' + cog)
            print('Successfully loaded ' + cog)

    @commands.command(name='unload', hidden=True)
    @checks.is_logan()
    async def cogunload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        if cog[0:5] != "cogs.":
            cog = "cogs." + cog
        else:
            pass

        try:
            await self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('Successfully unloaded ' + cog)
            print('Successfully unloaded ' + cog)

    @commands.command(name='reload', hidden=True)
    @checks.is_logan()
    async def cogreload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        if cog[0:5] != "cogs.":
            cog = "cogs." + cog
        else:
            pass

        try:
            await self.bot.unload_extension(cog)
            await self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**ERROR:** {type(e).__name__} - {e}')
        else:
            await ctx.send('Successfully reloaded ' + cog)
            print('Successfully reloaded ' + cog)

    @commands.command(name='listcogs', hidden=True)
    @checks.is_logan()
    async def listcogs(self, ctx, param=None):

        if param == 'technical' or param == 't':
            await ctx.send('There are {} cogs currently loaded: '.format(len(list(self.bot.cogs))))
            await ctx.send(self.bot.cogs)
        else:
            await ctx.send(list(self.bot.cogs))

    @commands.command('printip')
    @checks.is_logan()
    async def printip(self, ctx):
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname + ".local")
        await ctx.send('`' + str(ip_addr) + '`')

    @cogload.error
    @cogunload.error
    @cogreload.error
    async def cogowner_error(self, ctx, error):
        if isinstance(error, commands.MissingRole):
            await ctx.send('This command is only for my developers.')

async def setup(bot):
    await bot.add_cog(OwnerCog(bot))
