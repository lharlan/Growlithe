import discord
from discord.ext import commands

class ErrorHandlerCog(commands.Cog, name='Error Handler'):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # This prevents any commands with local handlers being handled here in on_command_error.
        if hasattr(ctx.command, 'on_error'):
            return

        # This prevents any cogs with an overwritten cog_command_error being handled here.
        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        # This prevents console spam of "Command "blahblahblah" is not found"
        if isinstance(error, commands.CommandNotFound):
            pass

        # MissingPermissions
        if isinstance(error, commands.MissingPermissions):
            return await ctx.send("**ERROR:** You are missing the required permission(s).")

        if isinstance(error, commands.MissingAnyRole) or isinstance(error, commands.MissingRole):
            return await ctx.send("**ERROR:** You are missing the required role(s).")

        # FailedCustomChecks
        if isinstance(error, commands.CheckFailure):
            print('{} ({}) tried to use command {} but is not an allowed user.'.format(ctx.author.name, ctx.author.id, ctx.command.name))
            return await ctx.send('**ERROR:** ' + f'{error}' + ' You are not an allowed user for this command.') 

        # BotMissingPermissions
        if isinstance(error, commands.BotMissingPermissions):
            print('Missing Permissions for command {}'.format(ctx.command.name))
            return await ctx.send('**ERROR:** Missing Permissions for command {}'.format(ctx.command.name))

        # NotAllowed (idk)
        if isinstance(error, discord.Forbidden):
            print('Forbidden. {} could not be executed from user {} in {}.'.format(ctx.command.name, ctx.author.name, ctx.guild.name))
            return await ctx.send('**ERROR:** Forbidden. {} could not be executed.'.format(ctx.command.name))

async def setup(bot):
    await bot.add_cog(ErrorHandlerCog(bot))
