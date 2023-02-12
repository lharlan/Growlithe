import os
import discord
from discord.ext import commands
import asyncio
import datetime
import pytz
from dotenv import load_dotenv

_intents = discord.Intents.default()
_intents.members = True
_intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=_intents, application_id='1015020701834555444')

async def load():
    bot_extensions = ['cogs.owner', 'cogs.botaltfinder', 'cogs.bothelpcommands', 'cogs.bothelpreplies', 'cogs.closeopen',  
    'cogs.errorhandler', 'cogs.eval', 'cogs.funcommands', 'cogs.giveroles', 'cogs.infocommands', 'cogs.lanshame', 
    'cogs.moderation', 'cogs.mute', 'cogs.note', 'cogs.pingreplies', 'cogs.raidblock', 'cogs.remind', 
    'cogs.warn', 'cogs.hello', 'cogs.dmlog', 'cogs.botmute', 'cogs.botmutefinder', 'cogs.rpi', 'cogs.raidbans']
    for extension in bot_extensions:
        await bot.load_extension(extension)

    print('There are {} cogs loaded.'.format(str(len(bot_extensions))))

@bot.event
async def on_ready():

    now = datetime.datetime.now(tz = pytz.timezone('America/Denver'))
    current_time = now.strftime("%H:%M:%S")
    print(f'{bot.user.name} is online, current time: ' + str(current_time) + '.')

# simple command to test latency
@bot.command(name='ping', help='Returns latency in ms.')
async def ping(ctx):
    await ctx.send(f'pong! Current latency is `{round(bot.latency * 1000)}ms`')

# assigns Trainer role on member join
@bot.event
async def on_member_join(person):
    Trainer_Role = 711901553568776223
    Announcement_Role = 764524310706257920
    channel = bot.get_channel(711900529722392596)
    await person.add_roles(person.guild.get_role(Trainer_Role))
    await person.add_roles(person.guild.get_role(Announcement_Role))
    await channel.send('Successfully given Trainer and Announcement roles to ' + person.mention)

async def main():
    await load()

asyncio.run(main())

load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)