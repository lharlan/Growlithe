from gpiozero import CPUTemperature
import psutil
import discord
import asyncio
from discord.ext import commands

def GrabStats():
    cpu = CPUTemperature()
    cpu_per = psutil.cpu_percent()
    mem_per = psutil.virtual_memory().percent
    cpu_freq = psutil.cpu_freq().current
    cpu_avg = psutil.getloadavg()

    return cpu, cpu_per, mem_per, cpu_freq, cpu_avg

def CreateEmbed(cmdType, seconds):
    cpu, cpu_per, mem_per, cpu_freq, cpu_avg = GrabStats()

    if cmdType == 'system':
        embedTitle = "Current System Information"
    elif cmdType == 'livelogging':
        embedTitle = "Current System Information Over {} Seconds".format(str(seconds))

    embed = discord.Embed(title=embedTitle, color=0x992d22)
    embed.add_field(name='Current CPU Temperature', value=str(cpu.temperature) + ' C', inline=False)
    embed.add_field(name='Current CPU Load Avg', value=str(cpu_avg) + ' at ' + str(cpu_per) + '% used' , inline=False)
    embed.add_field(name='Current CPU Clock', value=str(cpu_freq) + ' MHz', inline=False)
    embed.add_field(name='Current Memory Usage', value=str(mem_per) + '%', inline=False) 

    return embed

class RpiCog(commands.Cog, name='RPi Commands'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='system')
    async def system(self, ctx):

        embed = CreateEmbed('system', 0)
        await ctx.send(embed=embed)

    @commands.command(name="serverslist")
    async def serverslist(self, ctx):
        activeservers = self.bot.guilds
        for guild in activeservers:
            await ctx.send(guild.name)
            print(guild.name)

    @commands.command(name="livelogging")
    async def livelogging(self, ctx, seconds = 2):
        if seconds > 10:
            await ctx.send("I cannot log for more than 10 seconds.")
            return
        elif seconds <= 1:
            await ctx.send("You must give a time between 2 and 10 seconds. For a current snapshot of the system use `!system`.")
            return
        else:
            embed = CreateEmbed('livelogging', seconds)
            loggingEmbed = await ctx.send(embed=embed)
            index = 0

            while index < seconds:
                await asyncio.sleep(1)
                embed = CreateEmbed('livelogging', seconds)
                await loggingEmbed.edit(embed=embed)
                index += 1

async def setup(bot):
    await bot.add_cog(RpiCog(bot))
