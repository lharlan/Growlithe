import discord
from discord.ext import commands
import datetime as dt
import pytz
import re
import asyncio
import os

def add_time(current_time, time_addition):

    mysum = dt.timedelta()
    timelist = [current_time, time_addition]

    for i in timelist:
        (h, m, s) = i.split(':')

        if 'day' in h:
            day = h.split(' ')[0]
            h = h.split(' ')[-1]    
        else:
            day = 0

        d = dt.timedelta(days = int(day), hours = int(h), minutes = int(m), seconds = int(s))
        mysum += d
    return (str(mysum))

def sub_time(time_till, current_time):

    time_till = time_till.rstrip("\n")

    start_time = time_till.split(":")
    stop_time = current_time.split(":")

    if "day" in str(start_time[0]):

        day_format = start_time[0].split(" ") # 0 is days, 1 is "day", 2 is hours
        days = int(day_format[0]) * 24
        start_time[0] = int(day_format[2])

        start_time1 = dt.timedelta(hours=int(start_time[0] + days), minutes=int(start_time[1]), seconds=int(start_time[2]))
        stop_time1 = dt.timedelta(hours=int(stop_time[0]), minutes=int(stop_time[1]), seconds=int(stop_time[2]))

        time_elapsed = start_time1 - stop_time1

        return time_elapsed
    else:
        start_time1 = dt.time(int(start_time[0]), int(start_time[1]), int(start_time[2]))
        stop_time1 = dt.time(int(stop_time[0]), int(stop_time[1]), int(stop_time[2]))

        date = dt.date(1, 1, 1)
        datetime1 = dt.datetime.combine(date, start_time1)
        datetime2 = dt.datetime.combine(date, stop_time1)
        time_elapsed = datetime1 - datetime2
        return str(time_elapsed)

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

def SearchUsersPing(userID):
    SearchUsers = open('UsersToPing.txt', 'r')
    flag = False
    index = 0

    for line in SearchUsers:
        index += 1
        if userID in line:
            flag = True
            break

    SearchUsers.close()

    return flag

def SetUsersPing(userID):
    with open("UsersToPing.txt", "a") as myfile:
        myfile.write(userID + "\n")


def RemoveUsersPing(userID):
    RemoveUsers = open('UsersToPing.txt', 'r')
    UsersLines = RemoveUsers.readlines()
    RemoveUsers.close()

    DeleteUsers = open('UsersToPing.txt', 'w')
    for line in UsersLines:
        if userID not in line:
            DeleteUsers.write(line)

class RemindCog(commands.Cog, name='Reminders'):
    def __init__(self, bot):
        self.bot = bot

# management commands
    @commands.command(name='setping')
    async def setping(self, ctx):
        userID = str(ctx.author.id)

        SetUsersPing(userID)

        await ctx.send("I have added you as a user to ping. No reminder DM will be sent from now on. Undo this with `!removeping`.")

    @commands.command(name='removeping')
    async def removeping(self, ctx):
        userID = str(ctx.author.id)

        RemoveUsersPing(userID)

        await ctx.send("I have removed you as a user to ping. A reminder DM will be sent from now on. Undo this with `!setping`.")


# remind commands
    @commands.command(name='remindme')
    async def remindme(self, ctx, duration=None, *, reminder=None):

        if '@everyone' in reminder or '@here' in reminder:
            await ctx.send("You cannot use me to ping everyone. It does not work anyway")
            return


        # get current time to add later
        now = dt.datetime.now(tz = pytz.timezone('America/Denver'))
        current_time = str(now.strftime("%H:%M:%S"))

        # split time up
        try:
            dur_and_unit = re.split('(\d+)',duration)
        except:
            await ctx.send('An error occured when processing the `remindme` command! Please ensure you\'ve entered a duration and it\'s correct.')
            return
     
        # check if time is valid
        if dur_and_unit[0] == 'inf':
            await ctx.send('Not a valid time unit, use `s` for seconds, `m` for minutes, `hr` or `h` for hours, `d` or `days` for days.')
            return
        elif calc_seconds(dur_and_unit) != -1:
            pass
        else:
            await ctx.send('Not a valid time unit, use `s` for seconds, `m` for minutes, `hr` or `h` for hours, `d` or `days` for days.')
            return

        secs = calc_seconds(dur_and_unit)
        time_to_add = str(dt.timedelta(seconds=secs))
        
        added_time = add_time(current_time, time_to_add)

        if reminder == None:
            await ctx.send('You need to be reminded of something! Don\'t make me do this for no reason!')
            return
        else:
            remind_title = "Reminder set for `{}`".format(duration)
            remind_desc = "I\'ll remind you at `{} MST` for reminder: `{}`".format(str(added_time), reminder)
            reminder_embedVar = discord.Embed(title=remind_title, description=remind_desc, color=0xe74c3c)
            await ctx.send(embed=reminder_embedVar)

            # write to txt for storage
            set_reminder = "{}|{}|{}|{}".format(ctx.author.id, reminder, duration, str(added_time))
            remindwrite = open("reminders.txt",  "a")
            remindwrite.write(set_reminder + "\n")
            remindwrite.close()

            if duration == None or len(dur_and_unit) < 3:
                if dur_and_unit[0] == 'inf':
                    await ctx.send('There can be no infinite reminder time!')
                    return # pass because infinite time has len 1, all other real time has 3
                else:
                    await ctx.send('I need a time! Time format should be `##hr/m/s` and must be included.')
                    return
            else:
                pass

            if dur_and_unit[0] == 'inf':
                await ctx.send('Not a valid time unit, use `s` for seconds, `m` for minutes, `hr` or `h` for hours, `d` or `days` for days.')
                return
            elif calc_seconds(dur_and_unit) != -1:
                wait = calc_seconds(dur_and_unit)
                await asyncio.sleep(wait)
            else:
                await ctx.send('Not a valid time unit, use `s` for seconds, `m` for minutes, `hr` or `h` for hours, `d` or `days` for days.')
                return

            remind_embedVar = discord.Embed(title="**Your reminder has arrived!:**", description=reminder, color=0xe74c3c)

            # delete the reminder
            with open("reminders.txt", "r") as f:
                lines = f.readlines()
            with open("reminders.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != set_reminder:
                        f.write(line)

            DMUser = SearchUsersPing(str(ctx.author.id))

            try:
                if DMUser == False:
                    await ctx.author.send(embed=remind_embedVar) # DMs user
                else:
                    await ctx.send(ctx.author.mention)
                    await ctx.send(embed=remind_embedVar) # Pings in channel
            except discord.errors.Forbidden:
                pass # dont fail incase user has blocked the bot

    @commands.command(name='listreminders')
    async def listreminders(self, ctx):

        # get current time to add later
        now = dt.datetime.now(tz = pytz.timezone('America/Denver'))
        current_time = str(now.strftime("%H:%M:%S"))

        remind_id = str(ctx.author.id)
        reminds = []

        with open("reminders.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                splitlines = line.split("|")
                if splitlines[0] == remind_id:
                    time_till = sub_time(str(splitlines[3]), current_time)

                    reminds.append("`{}` set to remind in: `{}`.".format(splitlines[1], time_till))
                else:
                    pass

            reminds = '\n'.join(reminds)
            reminds_embedVar = discord.Embed(title="**Here are your current reminders:**", description=reminds, color=0xe74c3c)
            await ctx.send(embed=reminds_embedVar)
            
async def setup(bot):
    await bot.add_cog(RemindCog(bot))
