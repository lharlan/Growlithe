from discord.ext import commands

class MuteFinderCog(commands.Cog, name="Bot Mute Tracker"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        command_ch = 714220630618275940
        mew_log_ch = 778331118420099072
        zera_log_ch = 711875874810757241
        osha_log_ch = 718843355706163262
        amphy_log_ch = 914991253999992843
        dj_log_ch = 1053922292662538250
        grumpy_log_ch = 1059178431952211978

        # FORMAT: > [21:37:56] - Zera-423113: Found trading partner: momo-691297-0937 (MomoBoustifly) (NID: 14735908300664952505) [CODE:00007793]
        # should, also work with 
        # FORMAT: > [07:41:23] - Zera-423113: Found Link Trade partner: Alex-543023 (ID: 9932227407921047645)

        if ((message.channel.id == osha_log_ch or message.channel.id == zera_log_ch or message.channel.id == mew_log_ch 
            or message.channel.id == amphy_log_ch or message.channel.id == dj_log_ch or message.channel.id == grumpy_log_ch) 
            and ('trade partner' in message.content.lower() or 'trading partner' in message.content.lower())):

            NintendoID = 0
            channel = self.bot.get_channel(command_ch)
            muted_users = open('mute_list.txt', 'r')
            muted_data = muted_users.readlines()
            new_muted_data = []

            for user in muted_data:
                new_muted_data.append(user.replace('\n', ''))

            splitmsg = message.content.split()

            for element in splitmsg:
                if (len(element) == 21 or len(element) == 20) and element.endswith(')') == True: # checks for 19 or 20 digit Nintendo ID, they'll all be in parenthesis
                    NintendoID = element
                    #print(element)
                    pass

            if len(str(NintendoID)) > 15:
                for line in new_muted_data:
                
                    splitline = line.split() # FORMAT: Nico-564136 (ID: 3220374192620143822)
                    #print(len(splitline))
                    if len(splitline) == 3: 
                        LoggedNID = splitline[2]
                        #print(LoggedNID)

                        #if NintendoID[:-1] == splitline and len(message.content) > 10:
                        if NintendoID[:-1] == LoggedNID[:-1] and len(message.content) > 10:
                            print('Match found! There are muted accounts trading!')
                            await channel.send('I\'ve found a muted account trading with an alt in <#{}>. Please manually verfiy before banning. The user I have found is `'.format(str(message.channel.id)) + line + '`')
                            await channel.send('Message link containing the user found is here: ' + message.jump_url)
                            return

            muted_users.close()
            return

async def setup(bot):
    await bot.add_cog(MuteFinderCog(bot))