import discord
from discord.ext import commands
import random
import os
import sympy
from cogs.utils import checks
import datetime as dt
import pytz

global switch
switch = 'neutral'
print('Does this repeat')

def randNum():
    k = random.randint(0, 1)
    return k

def switchOdds(oddCase):

    global switch

    if oddCase == 'neutral':
        switch = 'neutral'
    elif oddCase == 'heads':
        switch = 'heads'
    elif oddCase == 'tails':
        switch = 'tails'

    return switch

def getTime(timezone):

    if timezone == 'null':
        return 'Unknown'
    else:
        now = dt.datetime.now(tz = pytz.timezone(timezone))
        current_time = str(now.strftime("%I:%M:%S %p"))
        return current_time

class FunCog(commands.Cog, name='Fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='checkodds', hidden=True)
    async def checkodds(self, ctx):
        global switch
        await ctx.reply(switch)

    @commands.check_any(checks.is_logan(), checks.is_staff())
    @commands.command(name='switchodds', hidden=True)
    async def switchodds(self, ctx, oddCase=None):
        if oddCase == 'neutral' or oddCase == 'tails' or oddCase == 'heads':
            switchOdds(oddCase)
            await ctx.reply('Switched odds to be in favor of {}.'.format(oddCase))
        else:
            await ctx.reply('Please use one of these three inputs: `heads`, `tails`, or `neutral`.')

    @commands.command(name='flip')
    async def flipcoin(self, ctx):
        global switch
        k = randNum()
        favorOdds = switch
        if favorOdds == 'neutral': # default, or neutral, case for odds
            if k == 0:
                await ctx.reply('Heads')
            elif k == 1:
                await ctx.reply('Tails')
            else:
                await ctx.reply('There was an error processing the `flip` command.')
        elif favorOdds == 'heads':
            await ctx.reply('Heads')
        elif favorOdds == 'tails':
            await ctx.reply('Tails')
        else:
            await ctx.reply('There was an error processing the `flip` command.')

    @commands.command(name='convert')
    async def convert(self, ctx, arg, arg2):

        cmeasurement = 0

        if arg2 == 'F' or arg2 == 'f':
            cmeasurement = (float(arg) - 32) * (5 / 9)
            cunit = 'C'
            ctype = 'temperature'

        if arg2 == 'C' or arg2 == 'c':
            cmeasurement = (float(arg) * (9 / 5)) + 32
            cunit = 'F'
            ctype = 'temperature'

        if arg2 == 'M' or arg2 == 'm' or arg2 == 'miles':
            cmeasurement = (float(arg)) * 1.609344
            cunit = 'Km'
            ctype = 'length'

        if arg2 == 'Km' or arg2 == 'km' or arg2 == 'kms':
            cmeasurement = (float(arg)) * 0.62137119
            cunit = 'miles'
            ctype = 'length'

        await ctx.send('Your converted {} is {} {}'.format(ctype, str(round(cmeasurement, 2)), cunit))

    @commands.command(name='bozley')
    async def bozley(self, ctx):

        upload_msg = await ctx.send("uploading image...")
        await ctx.send(file=discord.File("bozley/" + random.choice(os.listdir("bozley"))))
        await upload_msg.delete()

    @commands.command(name='loganbot')
    async def loganbot(self, ctx):
        await ctx.send('Logan is not a bot! But I am')

    #@commands.command(name='suffer')
    #@commands.has_any_role('Admin', 'Moderator') 
    #async def suffer(self, ctx):

    #    await ctx.send('Ok fuck this iam leaving. He was spamming and i was trying to report it. And you say its me thats in the wrong here. This server staff dont know wtf they doing\n-Sufferlord May 27, 2017')

    @commands.command(name='whoisnt')
    async def whoisnt(self, ctx):
        await ctx.send('Shut up Cody')

    @commands.command(name='rps')
    async def rps(self, ctx, player):

        choices = ['rock', 'paper', 'scissors']

        if player.lower() not in choices:
            await ctx.send('That\'s illegal, you forefit')
        else:
            
            computer = random.choice(choices)
    
            await ctx.send('I\'ve picked ' + computer + ', you\'ve picked ' + player.lower() + '.')
    
            if computer == player.lower():
                await ctx.send('Tie!')
            
            elif player.lower() == 'rock':
                if computer == 'paper':
                    await ctx.send('You lose!')
                if computer == 'scissors':
                    await ctx.send('You win!')
    
            elif player.lower() == 'paper':
                if computer == 'rock':
                    await ctx.send('You win!')
                if computer == 'scissors':
                    await ctx.send('You lose!')
    
            elif player.lower() == 'scissors':
                if computer == 'rock':
                    await ctx.send('You lose!')
                if computer == 'paper':
                    await ctx.send('You win!')
    
    @commands.command(name='math')
    async def math_calculate(self, ctx, *, equation):
        await ctx.message.add_reaction('\u2705')
        await ctx.send('```c\n' + str(round(sympy.sympify(equation), 2)) + '\n```')

    @commands.command(name='time', hidden=True)
    async def timezone(self, ctx, staffmember):

        staffmember = staffmember.lower() # converts to lowercase to ensure compatability

        staffdict = {
            'insert'    : 'Europe/London',
            'andrew'    : 'America/Denver',
            'charlie'   : 'Europe/London',
            'genga'     : 'Europe/London',
            'hoov'      : 'Europe/London',
            'husk'      : 'America/New_York',
            'kad'       : 'America/Chicago',
            'kenji'     : 'Europe/Berlin',
            'marco'     : 'Europe/Madrid',
            'plazie'    : 'America/New_York',
            'prodigy'   : 'America/New_York',
            'sec'       : 'America/New_York',
            'shae'      : 'Canada/Eastern',
            'azula'     : 'America/New_York',
            'kait'      : 'Canada/Eastern',
            'venom'     : 'America/Los_Angeles',
            'viv'       : 'America/Chicago',
            'jim'       : 'America/New_York',
            'logan'     : 'America/Denver',
            'cody'      : 'America/Chicago',
            'simon'     : 'Europe/Brussels',
            'snake'     : 'Singapore',
            'wolf'      : 'Europe/London',
        }

        for key in staffdict:
            if key == staffmember:
                staffZone = staffdict[key]

        staff_time = getTime(staffZone)

        await ctx.reply("{}\'s current time is {}. They are in the {} timezone.".format(staffmember, staff_time, staffZone))

async def setup(bot):
    await bot.add_cog(FunCog(bot))
