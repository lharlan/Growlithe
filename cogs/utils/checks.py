import discord
from discord.ext import commands

logan_id = 462273017284919326
madweeb_id = 734119924464746637
sec_id = 571475470940504065

real_admin = 711901311234474054
real_mod = 711901391555264514

def is_logan():
    async def predicate(ctx):
        if ctx.author.id == logan_id or ctx.author.id == madweeb_id or ctx.author.id == sec_id:
            return True
    return commands.check(predicate)

def is_staff():
    async def predicate(ctx):

        mod_role = discord.utils.get(ctx.guild.roles, id=711901391555264514)
        admin_role = discord.utils.get(ctx.guild.roles, id=711901311234474054)

        if mod_role in ctx.author.roles or admin_role in ctx.author.roles:
            return True
    return commands.check(predicate)

def is_admin():
    async def predicate(ctx):

        admin_role = discord.utils.get(ctx.guild.roles, id=711901311234474054)
        
        if admin_role in ctx.author.roles:
            return True
    return commands.check(predicate)